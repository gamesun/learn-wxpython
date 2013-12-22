#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2013, gamesun
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of gamesun nor the names of its contributors
# may be used to endorse or promote products derived from this software
# without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY GAMESUN "AS IS" AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL GAMESUN BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

import appInfo
from wx.lib.wordwrap import wordwrap
import sys,os
import wx
import layout
import re
from bisect import bisect_left

WAVEFORM_X_MARGIN = 5
WAVEFORM_H = 12
WAVEFORM_H_OFFSET = 16

#def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
#    hi = hi if hi is not None else len(a) # hi defaults to len(a)
#    pos = bisect_left(a,x,lo,hi)          # find insertion position
#    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

#---------------------------------------------------------------------------

class MyApp(wx.App):
    def OnInit(self):
        self.frame = layout.myFrame(None, wx.ID_ANY, "")

        self.frame.wdTitle.SetScrollRate(10, WAVEFORM_H_OFFSET)
        self.frame.wdCanvas.SetScrollRate(10, WAVEFORM_H_OFFSET)

        # Make a menu
        menuBar = wx.MenuBar()

        # 1st menu from left
        menu = wx.Menu()
        menu.Append(wx.ID_OPEN,    "&Open...")
        menu.Append(wx.ID_CLOSE,   "&Close")
        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT,    "&Exit", "Exit The Tool")
        menu.Enable(wx.ID_CLOSE, False)
        menuBar.Append(menu, "&File")

        # 2nd menu
        menuZoom = wx.Menu()
        for i in range(1, 17):
            exec('idZoom%d = wx.NewId()' % i)
        menuZoom.AppendRadioItem(idZoom1, "500%" )
        menuZoom.AppendRadioItem(idZoom2, "400%" )
        menuZoom.AppendRadioItem(idZoom3, "300%" )
        menuZoom.AppendRadioItem(idZoom4, "250%" )
        menuZoom.AppendRadioItem(idZoom5, "200%" )
        menuZoom.AppendRadioItem(idZoom6, "150%" )
        menuZoom.AppendRadioItem(idZoom7, "100%" )
        menuZoom.AppendRadioItem(idZoom8, "90%"  )
        menuZoom.AppendRadioItem(idZoom9, "80%"  )
        menuZoom.AppendRadioItem(idZoom10, "70%" )
        menuZoom.AppendRadioItem(idZoom11, "60%" )
        menuZoom.AppendRadioItem(idZoom12, "50%" )
        menuZoom.AppendRadioItem(idZoom13, "40%" )
        menuZoom.AppendRadioItem(idZoom14, "30%" )
        menuZoom.AppendRadioItem(idZoom15, "20%" )
        menuZoom.AppendRadioItem(idZoom16, "10%" )
        menuBar.Append(menuZoom, "&Zoom")

        # 3rd menu
        menuFunc = wx.Menu()
        idAutoAlign = wx.NewId()
        menuFunc.AppendCheckItem(idAutoAlign, "AutoAlign")
        menuBar.Append(menuFunc, "&Func")

        # 4th menu
        menuHelp = wx.Menu()
        menuHelp.Append(wx.ID_ABOUT, "About")
        menuBar.Append(menuHelp, "&Help")

        self.frame.SetMenuBar(menuBar)

        # and a file history
        self.filehistory = wx.FileHistory()
        self.filehistory.UseMenu(menu)

        menuBar.Check(idZoom7, True)
        menuBar.Check(idAutoAlign, True)

        self.zoomFactor = 1.0
        self.autoAlign = True
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.timer.Start(10)    # ms

        self.frame.pnlCanvas.Bind(wx.EVT_PAINT, self.OnPaint)
        self.frame.wdTitle.Bind(wx.EVT_SCROLLWIN, self.OnTitleScroll)
        self.frame.wdCanvas.Bind(wx.EVT_SCROLLWIN, self.OnCanvasScroll)

        self.frame.pnlCanvas.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)
        self.frame.pnlCanvas.Bind(wx.EVT_RIGHT_UP, self.OnMouseRightUp)

        self.frame.Bind(wx.EVT_MENU, self.OnOpenFile, id=wx.ID_OPEN)
        self.frame.Bind(wx.EVT_MENU, self.OnExitApp, id=wx.ID_EXIT)
        self.frame.Bind(wx.EVT_MENU_RANGE, self.OnFileHistory, id=wx.ID_FILE1, id2=wx.ID_FILE9)
        self.frame.Bind(wx.EVT_WINDOW_DESTROY, self.Cleanup)

        for i in range(1, 17):
            eval('self.frame.Bind(wx.EVT_MENU, self.OnZoom%d, id = idZoom%d)' % (i, i))

        self.frame.Bind(wx.EVT_MENU, self.OnAutoAlign, id = idAutoAlign)

        self.frame.Bind(wx.EVT_MENU, self.OnAbout, id = wx.ID_ABOUT)

        for i in range(1, 9):
            eval('self.frame.hyperlink_%d.Bind(wx.EVT_HYPERLINK, self.OnHypeLink%d)' % (i, i))
            exec('self.frame.hyperlink_%d.VisitedColour = self.frame.hyperlink_%d.NormalColour' % (i, i))
            eval("self.frame.label_T%d.SetLabel('')" % i)

        for i in range(1, 8):
            eval("self.frame.label_sub%d%d.SetLabel('')" % (i, i + 1))

#        self.frame.Center(wx.HORIZONTAL | wx.VERTICAL)

        self.SetTopWindow(self.frame)
        self.frame.Show()

        self.canvasSize = wx.Size()
        self.canvasFullSize = wx.Size(0, 32 * WAVEFORM_H_OFFSET)
        self.mousePosOld = None
        self.originWave = []
        self.waveform = []
        self.arrow = None

        self.movingT = None
        self.movingT_x = 0

        self.MeasureT_x = [[None, None], [None, None], [None, None], [None, None],
                          [None, None], [None, None], [None, None], [None, None]]

        return True

    def OnAutoAlign(self, evt = None):
        if evt.Selection == 1:
            self.autoAlign = True
        elif evt.Selection == 0:
            self.autoAlign = False

    def OnHypeLink1(self, evt):
        self.SelectT(0)

    def OnHypeLink2(self, evt):
        self.SelectT(1)

    def OnHypeLink3(self, evt):
        self.SelectT(2)

    def OnHypeLink4(self, evt):
        self.SelectT(3)

    def OnHypeLink5(self, evt):
        self.SelectT(4)

    def OnHypeLink6(self, evt):
        self.SelectT(5)

    def OnHypeLink7(self, evt):
        self.SelectT(6)

    def OnHypeLink8(self, evt):
        self.SelectT(7)

    def SelectT(self, idx):
        self.movingT = idx
        self.MeasureT_x[self.movingT][0] = None
        self.frame.pnlCanvas.Refresh(False)

    def OnMouseLeftUp(self, evt):
        if self.movingT is not None:
            self.MeasureT_x[self.movingT] = [self.movingT_x, self.movingT_x / self.zoomFactor - WAVEFORM_X_MARGIN]
            self.movingT = None

    def OnMouseRightUp(self, evt):
        if self.movingT is not None:
            self.MeasureT_x[self.movingT] = [None, None]
            eval("self.frame.label_T%d.SetLabel('')" % (self.movingT + 1))
            self.movingT = None

    def OnTimer(self, evt):
        pos = wx.GetMousePosition()
        try:
            rect = self.frame.wdCanvas.GetRect()
        except wx.PyDeadObjectError:
            return
        self.canvasSize = rect.GetSize()
        pos = self.frame.ScreenToClient(pos)
        if rect.Contains(pos):
            if self.mousePosOld != pos:
                self.mousePosOld = pos

                (pos.x, pos.y) = self.frame.wdCanvas.CalcUnscrolledPosition((pos.x, pos.y))
                (pos.x, pos.y) = (pos.x - rect.x, pos.y)
                self.movingT_x = pos.x

                if 0 < len(self.waveform):
                    line = pos.y / WAVEFORM_H_OFFSET

                    if line < len(self.waveform[1]):
                        idx = self.SearchIndex(pos.x - WAVEFORM_X_MARGIN, line)
                        if idx < len(self.waveform[1][line]):
                            if 0 < idx:
                                arrowNew = [0,0,0,0]
                                arrowNew[0] = self.waveform[1][line][idx-1][0] + 2 + WAVEFORM_X_MARGIN
                                arrowNew[2] = self.waveform[1][line][idx][0] - 2 + WAVEFORM_X_MARGIN
                                arrowNew[1] = arrowNew[3] = line * WAVEFORM_H_OFFSET + WAVEFORM_H / 2
                                if self.arrow != arrowNew:
                                    self.arrow = arrowNew[:]
                                    self.frame.pnlCanvas.Refresh(False)
                                    str11 = 'T1:      %d' % self.originWave[1][line][idx-1][0]
                                    str12 = 'T2:      %d' % self.originWave[1][line][idx][0]
                                    str13 = '|T1-T2|= %d' % (self.originWave[1][line][idx][0] - self.originWave[1][line][idx-1][0])
                                    self.frame.lblMeasure11.SetLabel(str11)
                                    self.frame.lblMeasure12.SetLabel(str12)
                                    self.frame.lblMeasure13.SetLabel(str13)

                            if self.autoAlign:
                                if 0 < idx:
                                    distanceToBefore = pos.x - self.waveform[1][line][idx-1][0] - WAVEFORM_X_MARGIN
                                    distanceToAfter = self.waveform[1][line][idx][0] - pos.x + WAVEFORM_X_MARGIN
                                    if distanceToBefore < distanceToAfter:
                                        if distanceToBefore < 30:
                                            #self.movingT_x = self.waveform[1][line][idx-1][0] + WAVEFORM_X_MARGIN
                                            self.movingT_x = pos.x - distanceToBefore
                                    else:
                                        if distanceToAfter < 30:
                                            #self.movingT_x = self.waveform[1][line][idx][0] + WAVEFORM_X_MARGIN
                                            self.movingT_x = pos.x + distanceToAfter
                                else:
                                    distanceToAfter = self.waveform[1][line][idx][0] - pos.x + WAVEFORM_X_MARGIN
                                    if distanceToAfter < 20:
                                        self.movingT_x = pos.x + distanceToAfter

                if self.movingT is not None:
                    self.MeasureT_x[self.movingT][1] = self.movingT_x - WAVEFORM_X_MARGIN
                    strLabel = '%dms' % self.MeasureT_x[self.movingT][1]
                    eval("self.frame.label_T%d.SetLabel(strLabel)" % (self.movingT + 1))
                    x_current = self.MeasureT_x[self.movingT][1]
                    if 0 < self.movingT < 7:
                        x_before = self.MeasureT_x[self.movingT - 1][1]
                        x_after = self.MeasureT_x[self.movingT + 1][1]
                        if x_current is not None:
                            if x_before is not None:
                                strLabel = '%dms' % abs(x_current - x_before)
                                eval('self.frame.label_sub%d%d.SetLabel(strLabel)' % (self.movingT, self.movingT + 1))
                            if x_after is not None:
                                strLabel = '%dms' % abs(x_current - x_after)
                                eval('self.frame.label_sub%d%d.SetLabel(strLabel)' % (self.movingT + 1, self.movingT + 2))
                    elif self.movingT == 0:
                        x_after = self.MeasureT_x[self.movingT + 1][1]
                        if x_after is not None:
                            strLabel = '%dms' % abs(x_current - x_after)
                            eval('self.frame.label_sub%d%d.SetLabel(strLabel)' % (self.movingT + 1, self.movingT + 2))
                    elif self.movingT == 7:
                        x_before = self.MeasureT_x[self.movingT - 1][1]
                        if x_before is not None:
                            strLabel = '%dms' % abs(x_current - x_before)
                            eval('self.frame.label_sub%d%d.SetLabel(strLabel)' % (self.movingT, self.movingT + 1))

                self.frame.pnlCanvas.Refresh(False)

    def SearchIndex(self, px, py):
        l_x = [p[0] for p in self.waveform[1][py]]
        return bisect_left(l_x, px)

    def OnPaint(self, evt = None):
        dc = wx.BufferedPaintDC(self.frame.pnlCanvas)
        dc.Clear()
        if 0 < len(self.waveform):
            for i, w in enumerate(self.waveform[1]):
                dc.SetPen(wx.Pen(wx.BLACK, 1))
                self.DrawWave(dc, w, WAVEFORM_X_MARGIN, WAVEFORM_H_OFFSET * i)
            if self.arrow is not None:
                self.DrawArrow(dc, self.arrow)
        if self.movingT is not None:
            self.DrawMeasureLine(dc, self.movingT_x)
        for x in self.MeasureT_x:
            if x[0] is not None:
                self.DrawMeasureLine(dc, x[0])

    def DrawWave(self, dc, coord, x_margin, y_offset):
        for c0, c1 in zip(coord[0:], coord[1:]):
            dc.DrawLine(c0[0] + x_margin, c0[1] * WAVEFORM_H + y_offset, c1[0] + x_margin, c0[1] * WAVEFORM_H + y_offset)
            dc.DrawLine(c1[0] + x_margin, c0[1] * WAVEFORM_H + y_offset, c1[0] + x_margin, c1[1] * WAVEFORM_H + y_offset)

    def DrawArrow(self, dc, coord):
        dc.DrawLine(coord[0], coord[1], coord[2], coord[3])
        dc.DrawLines([[coord[0]+2,coord[1]-2],[coord[0],coord[1]],[coord[0]+3,coord[1]+3]])
        dc.DrawLines([[coord[2]-2,coord[3]-2],[coord[2],coord[3]],[coord[2]-3,coord[3]+3]])

    def DrawMeasureLine(self, dc, x):
        dc.SetPen(wx.Pen(wx.RED, 1, style=wx.DOT))
        dc.DrawLine(x, 0, x, self.canvasFullSize.GetHeight())

    def OnZoom1(self, evt):
        self.Zoom( 5.0 )
    def OnZoom2(self, evt):
        self.Zoom( 4.0 )
    def OnZoom3(self, evt):
        self.Zoom( 3.0 )
    def OnZoom4(self, evt):
        self.Zoom( 2.5 )
    def OnZoom5(self, evt):
        self.Zoom( 2.0 )
    def OnZoom6(self, evt):
        self.Zoom( 1.5 )
    def OnZoom7(self, evt):
        self.Zoom( 1.0 )
    def OnZoom8(self, evt):
        self.Zoom( 0.9 )
    def OnZoom9(self, evt):
        self.Zoom( 0.8 )
    def OnZoom10(self, evt):
        self.Zoom( 0.7 )
    def OnZoom11(self, evt):
        self.Zoom( 0.6 )
    def OnZoom12(self, evt):
        self.Zoom( 0.5 )
    def OnZoom13(self, evt):
        self.Zoom( 0.4 )
    def OnZoom14(self, evt):
        self.Zoom( 0.3 )
    def OnZoom15(self, evt):
        self.Zoom( 0.2 )
    def OnZoom16(self, evt):
        self.Zoom( 0.1 )

    def Zoom(self, factor):
        self.arrow = None
        self.zoomFactor = factor
        if 0 < len(self.waveform):
            self.ZoomWaveform()

    def OnTitleScroll(self, evt = None):
        wx.CallAfter(self.OnTitleScrolled)
        evt.Skip()

    def OnTitleScrolled(self):
        x,y = self.frame.wdTitle.GetViewStart()
        self.frame.wdCanvas.Scroll(-1, y)

    def OnCanvasScroll(self, evt = None):
        wx.CallAfter(self.OnCanvasScrolled)
        evt.Skip()

    def OnCanvasScrolled(self):
        x,y = self.frame.wdCanvas.GetViewStart()
        self.frame.wdTitle.Scroll(-1, y)

    def Cleanup(self, *args):
        # A little extra cleanup is required for the FileHistory control
        del self.filehistory

    def OnOpenFile(self, evt):
        dlg = wx.FileDialog(self.frame,
                           defaultDir = os.getcwd(),
                           wildcard = "All Files|*",
                           style = wx.OPEN | wx.CHANGE_DIR)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
#            print "You selected %s\n" % path,

            # add it to the history
            self.filehistory.AddFileToHistory(path)

            self.ReadFile(path)

        dlg.Destroy()


    def OnFileHistory(self, evt):
        # get the file based on the menu ID
        fileNum = evt.GetId() - wx.ID_FILE1
        path = self.filehistory.GetHistoryFile(fileNum)
#        print "You selected %s\n" % path,

        self.ReadFile(path)

        # add it back to the history so it will be moved up the list
        self.filehistory.AddFileToHistory(path)

    def ReadFile(self, path):
        # read file
        file = open(path, 'rU')

        # read file's all lines to a list
        lstData = file.readlines()

        file.close()

        self.frame.pnlCanvas.Refresh()      # clear the canvas
        self.originWave = Parser(lstData)
        self.ZoomWaveform()

    def ZoomWaveform(self):
        self.waveform = [self.originWave[0]*self.zoomFactor,[[(p[0]*self.zoomFactor, p[1]) for p in line] for line in self.originWave[1]]]
        self.canvasFullSize = wx.Size(self.waveform[0] + 2 * WAVEFORM_X_MARGIN, 32 * WAVEFORM_H_OFFSET)
        self.frame.pnlCanvas.SetSize(self.canvasFullSize)
        self.frame.pnlCanvas.SetMinSize(self.canvasFullSize)
        self.frame.wdCanvas.SetScrollbar(wx.HORIZONTAL | wx.VERTICAL, 1, 1, 10)
        self.frame.pnlCanvas.Refresh(False)

    def OnAbout(self, evt = None):
        # First we create and fill the info object
        info = wx.AboutDialogInfo()
        info.Name = appInfo.title
        info.Version = appInfo.version
        info.Copyright = appInfo.copyright
        info.Description = wordwrap(
            '                              ...'
            '                               \n'
            '                              ...'
            '                               \n'
            '                              ...'
            '                                 ',
            335, wx.ClientDC(self.frame))
        #info.WebSite = (appInfo.url, "Home Page")
        info.Developers = [ appInfo.author ]
        info.License = wordwrap(appInfo.copyright, 500, wx.ClientDC(self.frame))

#        info.Icon = icon32.geticon32Icon()

        wx.AboutBox(info)

    def OnExitApp(self, evt = None):
        self.timer.Stop()
        self.frame.Close(True)

#---------------------------------------------------------------------------

g_match = re.compile('(?P<time>[0-9a-fA-F]{4}) (?P<value>[0-9a-fA-F]{8})')

def Parser(lines):
    """
    parser the data and display results at the canvas.
    Parser(list) -> [ duration,                            #info
                      [((x1,y1), (x2,y2), ... (xn,yn)),    #wave 1
                      (...),                               #wave 2
                      ...  ]]
    """

    RawData = [g_match.search(l) for l in lines]                                    # get the origin data
    list = [(r.group('time'), r.group('value')) for r in RawData if r is not None]  # filter the null data
    list.sort()

    if 0 < len(list):
        matrix = [[(int(l[0], 16), int(v)) for v in bits(int(l[1], 16), 32)] for l in list]
        matrix = zip(*matrix)           # zip(*matrix): Transpose the matrix
        matrix = [[line[0],] + [p1 for p0, p1 in zip(line[0:], line[1:]) if p0[1] != p1[1]] + [line[-1],] for line in matrix[::-1]]
#        print matrix
        return (int(list[-1][0], 16) - int(list[0][0], 16), matrix)
    return

def bits(data):
    while data:
        yield data & 1
        data >>= 1

def bits(data, bits):
    for i in xrange(bits):
        yield data & 1
        data >>= 1



overview = """\
"""


if __name__ == '__main__':
    app = MyApp(0)
    app.MainLoop()
