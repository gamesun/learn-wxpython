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
import layout2 as layout
import re
from bisect import bisect_left
import codecs
import ConfigParser

# waveform parameters
WF_LEFT_MARGIN = 5
WF_TOP_MARGIN = 18
WF_H = 9
WF_H_OFFSET = 15
GRID_OFFSET = (WF_H_OFFSET - WF_H) / 2 + 4

MEASURE_LINE_TOP = WF_TOP_MARGIN - 6
MEASURE_LINE_BTM = WF_TOP_MARGIN + 32 * WF_H_OFFSET + 1

regex_sig = re.compile('^(?P<index>\d+):(?P<signalLabel>.*)[\r\n]')

#def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
#    hi = hi if hi is not None else len(a) # hi defaults to len(a)
#    pos = bisect_left(a,x,lo,hi)          # find insertion position
#    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

#---------------------------------------------------------------------------

class TestTransientPopup(wx.PopupTransientWindow):
    """Adds a bit of text and mouse movement to the wx.PopupWindow"""
    def __init__(self, parent, style):
        wx.PopupTransientWindow.__init__(self, parent, style)

        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        gSizer1 = wx.GridSizer( 0, 5, 0, 0 )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText1.Wrap( -1 )
        self.m_staticText1.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )
        self.m_staticText1.SetToolTipString( u"Yellow" )

        gSizer1.Add( self.m_staticText1, 0, wx.ALL, 3 )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText2.Wrap( -1 )
        self.m_staticText2.SetBackgroundColour( wx.Colour( 0, 255, 0 ) )
        self.m_staticText2.SetToolTipString( u"Lime" )

        gSizer1.Add( self.m_staticText2, 0, wx.ALL, 3 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText3.Wrap( -1 )
        self.m_staticText3.SetBackgroundColour( wx.Colour( 0, 255, 255 ) )
        self.m_staticText3.SetToolTipString( u"Aqua" )

        gSizer1.Add( self.m_staticText3, 0, wx.ALL, 3 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText4.Wrap( -1 )
        self.m_staticText4.SetBackgroundColour( wx.Colour( 255, 0, 255 ) )
        self.m_staticText4.SetToolTipString( u"Fuchsia" )

        gSizer1.Add( self.m_staticText4, 0, wx.ALL, 3 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText5.Wrap( -1 )
        self.m_staticText5.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
        self.m_staticText5.SetToolTipString( u"Blue" )

        gSizer1.Add( self.m_staticText5, 0, wx.ALL, 3 )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText6.Wrap( -1 )
        self.m_staticText6.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        self.m_staticText6.SetToolTipString( u"Red" )

        gSizer1.Add( self.m_staticText6, 0, wx.ALL, 3 )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText7.Wrap( -1 )
        self.m_staticText7.SetBackgroundColour( wx.Colour( 0, 0, 128 ) )
        self.m_staticText7.SetToolTipString( u"Navy" )

        gSizer1.Add( self.m_staticText7, 0, wx.ALL, 3 )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText8.Wrap( -1 )
        self.m_staticText8.SetBackgroundColour( wx.Colour( 0, 128, 128 ) )
        self.m_staticText8.SetToolTipString( u"Teal" )

        gSizer1.Add( self.m_staticText8, 0, wx.ALL, 3 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText9.Wrap( -1 )
        self.m_staticText9.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
        self.m_staticText9.SetToolTipString( u"Green" )

        gSizer1.Add( self.m_staticText9, 0, wx.ALL, 3 )

        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText10.Wrap( -1 )
        self.m_staticText10.SetBackgroundColour( wx.Colour( 128, 0, 128 ) )
        self.m_staticText10.SetToolTipString( u"Purple" )

        gSizer1.Add( self.m_staticText10, 0, wx.ALL, 3 )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText11.Wrap( -1 )
        self.m_staticText11.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
        self.m_staticText11.SetToolTipString( u"Maroon" )

        gSizer1.Add( self.m_staticText11, 0, wx.ALL, 3 )

        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText12.Wrap( -1 )
        self.m_staticText12.SetBackgroundColour( wx.Colour( 128, 128, 0 ) )
        self.m_staticText12.SetToolTipString( u"Olive" )

        gSizer1.Add( self.m_staticText12, 0, wx.ALL, 3 )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText13.Wrap( -1 )
        self.m_staticText13.SetBackgroundColour( wx.Colour( 128, 128, 128 ) )
        self.m_staticText13.SetToolTipString( u"Gray" )

        gSizer1.Add( self.m_staticText13, 0, wx.ALL, 3 )

        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText14.Wrap( -1 )
        self.m_staticText14.SetBackgroundColour( wx.Colour( 192, 192, 192 ) )
        self.m_staticText14.SetToolTipString( u"Silver" )

        gSizer1.Add( self.m_staticText14, 0, wx.ALL, 3 )

        self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText15.Wrap( -1 )
        self.m_staticText15.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
        self.m_staticText15.SetToolTipString( u"Black" )

        gSizer1.Add( self.m_staticText15, 0, wx.ALL, 3 )


        bSizer1.Add( gSizer1, 0, wx.ALL, 2 )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LI_HORIZONTAL )
        bSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 0 )


        bSizer1.Add( bSizer2, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 3 )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Custom", wx.DefaultPosition, wx.Size( -1,25 ), 0 )
        bSizer3.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 2 )


        bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

        self.SetSizer( bSizer1 )

        bSizer1.Fit(self)

        self.focus = None

        self.m_button1.Bind(wx.EVT_BUTTON, self.OnBtnCustom)

        self.Bind(wx.EVT_PAINT, self.OnPaint_Window)

        for i in range(1, 16):
            eval("self.m_staticText%d.Bind(wx.EVT_PAINT, lambda evt, self = self: self.OnPaint_StaticText(evt, %d))" % (i, i))
            eval("self.m_staticText%d.Bind(wx.EVT_LEFT_UP, lambda evt, self = self: self.OnLeftUp_StaticText(evt, %d))" % (i, i))
            eval("self.m_staticText%d.Bind(wx.EVT_ENTER_WINDOW, lambda evt, self = self: self.OnEnterWindow(evt, %d))" % (i, i))
            eval("self.m_staticText%d.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)" % i)

        self.Layout()

    def OnLeftUp_StaticText(self, evt, idx):
        self.color = eval("self.m_staticText%d.GetBackgroundColour()" % idx)
        # TODO: set event

        self.Destroy()

    def OnPaint_StaticText(self, evt, idx):
        dc = eval("wx.BufferedPaintDC(self.m_staticText%d)" % idx)
        dc.Clear()

        if self.focus is idx:
            rect = eval("self.m_staticText%d.GetClientRect()" % idx)
            dc.SetPen(wx.Pen(wx.Colour(255, 226, 148)))
            dc.SetBrush(wx.Brush(wx.Colour(255, 255, 255), wx.BRUSHSTYLE_TRANSPARENT))
            dc.DrawRectangle(*rect)

        evt.Skip()

    def OnPaint_Window(self, evt = None):
        dc = wx.BufferedPaintDC(self)
        dc.Clear()

        # Draw the border of PopupWindow
        rect = self.GetClientRect()
        dc.SetPen(wx.Pen(wx.Colour(134, 134, 134)))
        dc.SetBrush(wx.Brush(wx.Colour(255, 255, 255), wx.BRUSHSTYLE_TRANSPARENT))
        dc.DrawRectangle(*rect)

        # Draw the border of every color
        dc.SetPen(wx.Pen(wx.Colour(197, 197, 197)))
        for i in range(1, 16):
            rect = eval("self.m_staticText%d.GetRect()" % i)
            rect.Inflate(1, 1)
            dc.DrawRectangle(*rect)

        # Draw the border of focused color
        if self.focus is not None:
            rect = eval("self.m_staticText%d.GetRect()" % self.focus)
            rect.Inflate(1, 1)
            dc.SetPen(wx.Pen(wx.Colour(242, 148, 54)))
            dc.DrawRectangle(*rect)

        evt.Skip()

    def OnEnterWindow(self, evt, idx):
        self.focus = idx
        self.Refresh(False)

    def OnLeaveWindow(self, evt):
        self.focus = None
        self.Refresh(False)

    def OnBtnCustom(self, evt = None):
        data = wx.ColourData()
        data.SetChooseFull(True)

        # set the first custom color (index 0)
#        data.SetCustomColour(0, (255, 170, 128))
        # set indexes 1-N here if you like.

        # set the default color in the chooser
#        data.SetColour(wx.Colour(128, 255, 170))

        # construct the chooser
        dlg = wx.ColourDialog(self, data)

        if dlg.ShowModal() == wx.ID_OK:
            # set the panel background color
            color = dlg.GetColourData().Colour

            # TODO: set event

        dlg.Destroy()

        self.Destroy()

class MyApp(wx.App):
    def OnInit(self):
        self.frame = layout.myFrame(None)

        self.frame.wdTitle.SetScrollRate(10, WF_H_OFFSET / 2)
        self.frame.wdCanvas.SetScrollRate(10, WF_H_OFFSET / 2)

        colorDatabase = wx.ColourDatabase()
        self.Tcolor = [
          colorDatabase.Find('ORANGE RED'),
          (255, 165, 0),#colorDatabase.Find('ORANGE1'),
          colorDatabase.Find('SKY BLUE'),
          colorDatabase.Find('SPRING GREEN'),
          (191, 62, 255),#colorDatabase.Find('DARKORCHID1'),
          (255, 106, 106),#colorDatabase.Find('INDIANRED1'),
          (0, 229, 238),#colorDatabase.Find('TURQUOISE2'),
          colorDatabase.Find('GREY'),
        ]

        # Make a menu
        menuBar = wx.MenuBar()

        # 1st menu from left
        menu = wx.Menu()
        menu.Append(wx.ID_OPEN,    "&Open log", "Open a log file to display.")
        menu.Append(wx.ID_CLOSE,   "&Close", "Close the log file.")
        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT,    "&Exit", "Exit The Tool")
        menu.Enable(wx.ID_CLOSE, False)
        menuBar.Append(menu, "&File")

        # and a file history
        self.filehistory = wx.FileHistory()
        self.filehistory.UseMenu(menu)

        # 2nd menu
        menuSignLabel = wx.Menu()
        id_openSigFile = wx.NewId()
        menuSignLabel.Append(id_openSigFile, "&Open Sig", "Load signal labels form a *.sig file.")
        menuBar.Append(menuSignLabel, "&Signal")

        # 3rd menu
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

        # 4th menu
        menuFunc = wx.Menu()
        idAutoAlign = wx.NewId()
        menuFunc.AppendCheckItem(idAutoAlign, "&AutoAlign", "Auto align a measure line to rising edge or falling edge.")
        menuBar.Append(menuFunc, "Fun&c")

        # 5th menu
        menuHelp = wx.Menu()
        menuHelp.Append(wx.ID_ABOUT, "&About")
        menuBar.Append(menuHelp, "&Help")

        self.frame.SetMenuBar(menuBar)

        menuBar.Check(idZoom7, True)
        menuBar.Check(idAutoAlign, True)

        self.zoomFactor = 1.0
        self.autoAlign = True
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.timer.Start(10)    # ms

        self.frame.window_1.Bind(wx.EVT_SPLITTER_DCLICK, self.OnSplitterDClick)

        self.frame.pnlCanvas.Bind(wx.EVT_PAINT, self.OnPaint)
        self.frame.wdTitle.Bind(wx.EVT_SCROLLWIN, self.OnTitleScroll)
        self.frame.wdCanvas.Bind(wx.EVT_SCROLLWIN, self.OnCanvasScroll)

        self.frame.pnlCanvas.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)
        self.frame.pnlCanvas.Bind(wx.EVT_RIGHT_UP, self.OnMouseRightUp)

        self.frame.Bind(wx.EVT_MENU, self.OnOpenFile, id=wx.ID_OPEN)
        self.frame.Bind(wx.EVT_MENU, self.OnOpenSigFile, id=id_openSigFile)

        self.frame.Bind(wx.EVT_MENU, self.OnExitApp, id=wx.ID_EXIT)
        self.frame.Bind(wx.EVT_MENU_RANGE, self.OnFileHistory, id=wx.ID_FILE1, id2=wx.ID_FILE9)
        self.frame.Bind(wx.EVT_WINDOW_DESTROY, self.Cleanup)

        for i in range(1, 17):
            eval('self.frame.Bind(wx.EVT_MENU, self.OnZoom%d, id = idZoom%d)' % (i, i))

        self.frame.Bind(wx.EVT_MENU, self.OnAutoAlign, id = idAutoAlign)

        self.frame.Bind(wx.EVT_MENU, self.OnAbout, id = wx.ID_ABOUT)

        for i in range(1, 9):
            eval('self.frame.lblMeasure_T%d.Bind(wx.EVT_LEFT_DOWN, self.OnClickMeasure_T%d)' % (i, i))
            eval('self.frame.lblMeasure_T%d.Bind(wx.EVT_ENTER_WINDOW, lambda evt, self = self: self.OnEnterMeasure_T(evt, %d))' % (i, i))
            eval('self.frame.lblMeasure_T%d.Bind(wx.EVT_LEAVE_WINDOW, lambda evt, self = self: self.OnLeaveMeasure_T(evt, %d))' % (i, i))
            exec('self.frame.lblMeasure_T%d.SetForegroundColour(self.Tcolor[i-1])' % i)
            exec('self.frame.lblMeasure_T%d.SetCursor(wx.StockCursor(wx.CURSOR_HAND))' % i)
            eval("self.frame.label_T%d.SetLabel('')" % i)

        for i in range(1, 8):
            eval("self.frame.label_sub%d%d.SetLabel('')" % (i, i + 1))

        for i in range(1, 33):
            label = "%02d:        " % (33 - i)
            eval("self.frame.label_%d.SetLabel(label)" % i)
            eval("self.frame.label_%d.SetMinSize((-1, %d))" % (i, WF_H_OFFSET))
        self.frame.label_topSpacer.SetMinSize((-1, WF_TOP_MARGIN - 3))
        self.frame.wdTitle.GetSizer().Layout()

        self.frame.label_1.Bind(wx.EVT_LEFT_DOWN, self.OnClickLabel1)
        self.frame.label_1.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterLabel)
        self.frame.label_1.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveLabel)

        self.sizerSigLabel = self.frame.wdTitle.GetSizer()

        self.SetTopWindow(self.frame)
        self.frame.Show()

        self.canvasSize = wx.Size()
        self.canvasFullSize = wx.Size(0, 32 * WF_H_OFFSET + WF_TOP_MARGIN)
        self.mousePosOld = None
        self.originWave = []
        self.waveform = []
        self.arrow = None

        self.movingT = None
        self.movingT_x = 0

        self.MeasureT_x = [[None, None] for i in range(8)]

        self.mouseEntered1 = False

        self.sigFilePath = ""
        self.signalLabel = ["%02d:" % i for i in range(1, 33)][::-1]

        self.config = ConfigParser.RawConfigParser()
        self.LoadSettings()
#        self.LoadSigFile(".\sample.sig")

        return True

    def OnEnterMeasure_T(self, evt, idx):
        ctrl = evt.GetEventObject()
        font = ctrl.GetFont()
        font.SetUnderlined(True)
        ctrl.SetFont(font)

    def OnLeaveMeasure_T(self, evt, idx):
        ctrl = evt.GetEventObject()
        font = ctrl.GetFont()
        font.SetUnderlined(False)
        ctrl.SetFont(font)

    def OnEnterLabel(self, evt = None):
        f = self.frame.label_1.GetFont()
        f.SetUnderlined(True)
        self.frame.label_1.SetFont(f)

    def OnLeaveLabel(self, evt = None):
        f = self.frame.label_1.GetFont()
        f.SetUnderlined(False)
        self.frame.label_1.SetFont(f)

    def OnClickLabel1(self, evt):
        win = TestTransientPopup(self.frame, wx.NO_BORDER)
        pos = wx.GetMousePosition()
        win.Position(pos, (0, 0))

        win.Popup()

    def LoadSettings(self):
        self.config.read('setting.ini')
        try:
            if self.config.has_section('sig_file'):
                self.LoadSigFile(self.config.get('sig_file', 'path'))
        except:
            pass

    def SaveSettings(self):
        if not self.config.has_section('sig_file'):
            self.config.add_section('sig_file')

        self.config.set('sig_file', 'path', self.sigFilePath)

        with open('setting.ini', 'w') as configfile:
            self.config.write(configfile)

    def OnSplitterDClick(self, evt):
        evt.Veto()  # disable the feature "unsplit a splitter"

    def OnOpenSigFile(self, evt):
        dlg = wx.FileDialog(self.frame,
                           defaultDir = os.getcwd(),
                           wildcard = "Sig Files|*.sig",
                           style = wx.OPEN | wx.CHANGE_DIR)

        if dlg.ShowModal() == wx.ID_OK:
            self.LoadSigFile(dlg.GetPath())

        dlg.Destroy()


    def LoadSigFile(self, path):
        self.sigFilePath = path
        file = codecs.open(path, 'r', 'shift-jis')

        lines = file.readlines()

        file.close()

        for line in lines:
            r = regex_sig.search(line)
            if r:
                idx = int(r.group('index'))
                lbl = '%02d:%s' % (idx + 1, r.group('signalLabel'))
                self.signalLabel[31 - idx] = lbl
                idx = 32 - idx
                if 1 <= idx <= 32:
                    self.signalLabel
                    eval('self.frame.label_%d.SetLabel(lbl)' % idx)

    def OnAutoAlign(self, evt = None):
        if evt.Selection == 1:
            self.autoAlign = True
        elif evt.Selection == 0:
            self.autoAlign = False

    def OnClickMeasure_T1(self, evt):
        self.SelectT(0)

    def OnClickMeasure_T2(self, evt):
        self.SelectT(1)

    def OnClickMeasure_T3(self, evt):
        self.SelectT(2)

    def OnClickMeasure_T4(self, evt):
        self.SelectT(3)

    def OnClickMeasure_T5(self, evt):
        self.SelectT(4)

    def OnClickMeasure_T6(self, evt):
        self.SelectT(5)

    def OnClickMeasure_T7(self, evt):
        self.SelectT(6)

    def OnClickMeasure_T8(self, evt):
        self.SelectT(7)

    def SelectT(self, idx):
        if self.movingT is not None:
            self.OnMouseRightUp()
        self.movingT = idx
        self.MeasureT_x[self.movingT][0] = None
        self.frame.pnlCanvas.Refresh(False)

    def OnMouseLeftUp(self, evt):
        if self.movingT is not None:
            self.MeasureT_x[self.movingT] = [self.movingT_x, (self.movingT_x - WF_LEFT_MARGIN) / self.zoomFactor]
            self.movingT = None

    def OnMouseRightUp(self, evt = None):
        if self.movingT is not None:
            self.MeasureT_x[self.movingT] = [None, None]
            eval("self.frame.label_T%d.SetLabel('')" % (self.movingT + 1))
            if 0 < self.movingT < 7:
                eval("self.frame.label_sub%d%d.SetLabel('')" % (self.movingT, self.movingT + 1))
                eval("self.frame.label_sub%d%d.SetLabel('')" % (self.movingT + 1, self.movingT + 2))
            elif self.movingT == 0:
                eval("self.frame.label_sub%d%d.SetLabel('')" % (self.movingT + 1, self.movingT + 2))
            elif self.movingT == 7:
                eval("self.frame.label_sub%d%d.SetLabel('')" % (self.movingT, self.movingT + 1))
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
                    line = (pos.y - WF_TOP_MARGIN) / WF_H_OFFSET

                    if -1 < line < len(self.waveform[1]):
                        idx = self.SearchIndex(pos.x - WF_LEFT_MARGIN, line)
                        if idx < len(self.waveform[1][line]):
                            if 0 < idx:
                                arrowNew = [0,0,0,0]
                                arrowNew[0] = self.waveform[1][line][idx-1][0] + 2 + WF_LEFT_MARGIN
                                arrowNew[2] = self.waveform[1][line][idx][0] - 2 + WF_LEFT_MARGIN
                                arrowNew[1] = arrowNew[3] = line * WF_H_OFFSET + WF_H / 2 + WF_TOP_MARGIN
                                if self.arrow != arrowNew:
                                    self.arrow = arrowNew[:]
                                    self.frame.pnlCanvas.Refresh(False)
                                    str1 = 'T1:      %d' % self.originWave[1][line][idx-1][0]
                                    str2 = 'T2:      %d' % self.originWave[1][line][idx][0]
                                    str3 = '|T1-T2|= %d' % (self.originWave[1][line][idx][0] - self.originWave[1][line][idx-1][0])
                                    str4 = self.signalLabel[line]
                                    self.frame.lblInfo1.SetLabel(str1)
                                    self.frame.lblInfo2.SetLabel(str2)
                                    self.frame.lblInfo3.SetLabel(str3)
                                    self.frame.lblInfo4.SetLabel(str4)

                            if self.autoAlign:
                                if 0 < idx:
                                    distanceToBefore = pos.x - self.waveform[1][line][idx-1][0] - WF_LEFT_MARGIN
                                    distanceToAfter = self.waveform[1][line][idx][0] - pos.x + WF_LEFT_MARGIN
                                    if distanceToBefore < distanceToAfter:
                                        if distanceToBefore < 30:
                                            #self.movingT_x = self.waveform[1][line][idx-1][0] + WF_LEFT_MARGIN
                                            self.movingT_x = pos.x - distanceToBefore
                                    else:
                                        if distanceToAfter < 30:
                                            #self.movingT_x = self.waveform[1][line][idx][0] + WF_LEFT_MARGIN
                                            self.movingT_x = pos.x + distanceToAfter
                                else:
                                    distanceToAfter = self.waveform[1][line][idx][0] - pos.x + WF_LEFT_MARGIN
                                    if distanceToAfter < 20:
                                        self.movingT_x = pos.x + distanceToAfter

                if self.movingT is not None:
                    self.MeasureT_x[self.movingT][1] = (self.movingT_x - WF_LEFT_MARGIN) / self.zoomFactor
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
        dc.SetFont(wx.Font(9, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "Consolas"))

        # TODO: use DrawLineList(sequence, pens=None) to optimize.
        self.DrawGrid(dc)
        if 0 < len(self.waveform):
            for i, w in enumerate(self.waveform[1]):
                self.DrawRect(dc, w, WF_LEFT_MARGIN, (WF_H_OFFSET * i + WF_TOP_MARGIN))
        for i, x in enumerate(self.MeasureT_x):
            if x[0] is not None:
                self.DrawMeasureLine(dc, x[0], i)
        if 0 < len(self.waveform):
            for i, w in enumerate(self.waveform[1]):
                self.DrawWave(dc, w, WF_LEFT_MARGIN, (WF_H_OFFSET * i + WF_TOP_MARGIN))
            if self.arrow is not None:
                self.DrawArrow(dc, self.arrow)
        if self.movingT is not None:
            self.DrawMeasureLine(dc, self.movingT_x, self.movingT)

    def DrawGrid(self, dc):
        dc.SetPen(wx.Pen((150,150,150), 1))
        for i in range(32):
            dc.DrawLine(1, i * WF_H_OFFSET + WF_H + WF_TOP_MARGIN, self.canvasFullSize.GetWidth() - 1, i * WF_H_OFFSET + WF_H + WF_TOP_MARGIN)

    def DrawWave(self, dc, coord, x_margin, y_offset):
        for c0, c1 in zip(coord[0:], coord[1:]):
            x0 = c0[0] + x_margin
            y0 = c0[1] * WF_H + y_offset
            x1 = c1[0] + x_margin
            y1 = c1[1] * WF_H + y_offset
            dc.SetPen(wx.Pen(wx.BLACK, 1))
            dc.DrawLine(x0, y0, x1, y0)
            dc.DrawLine(x1, y0, x1, y1)

    def DrawRect(self, dc, coord, x_margin, y_offset):
        for c0, c1 in zip(coord[0:], coord[1:]):
            x0 = c0[0] + x_margin
            y0 = c0[1] * WF_H + y_offset
            x1 = c1[0] + x_margin
            y1 = c1[1] * WF_H + y_offset
            if c0[1] is 0:
                dc.SetPen(wx.TRANSPARENT_PEN)
                dc.SetBrush(wx.Brush((224, 224, 224), wx.SOLID))
                dc.DrawRectangle(x0 + 1, y0 + 1, x1 - x0 - 1, WF_H - 1)

    def DrawArrow(self, dc, coord):
        dc.DrawLine(coord[0], coord[1], coord[2], coord[3])
        dc.DrawLines([[coord[0]+2,coord[1]-2],[coord[0],coord[1]],[coord[0]+3,coord[1]+3]])
        dc.DrawLines([[coord[2]-2,coord[3]-2],[coord[2],coord[3]],[coord[2]-3,coord[3]+3]])

    def DrawMeasureLine(self, dc, x, id):
        dc.SetPen(wx.Pen(self.Tcolor[id], 2, style = wx.SHORT_DASH))
        dc.DrawText('%d' % (id + 1), x - 3, -1)
        dc.DrawLine(x, MEASURE_LINE_TOP, x, MEASURE_LINE_BTM)
        dc.DrawText('%d' % (id + 1), x - 3, MEASURE_LINE_BTM - 2)

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
        self.SaveSettings()
        #del self.filehistory

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
        self.canvasFullSize = wx.Size(self.waveform[0] + 2 * WF_LEFT_MARGIN, 32 * WF_H_OFFSET + 2 * WF_TOP_MARGIN)
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
#        matrix = [[(int(l[0], 16), int(v)) for v in bits(int(l[1], 16), 32)] for l in list]
        matrix = [[(int(l[0], 16), (int(v) + 1) & 1) for v in bits(int(l[1], 16), 32)] for l in list]
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
