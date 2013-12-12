# -*- coding:utf-8 -*-

import sys,os
import wx
# from wx import xrc
# import OpenGLMdl as glmdl
import layout
import re
# from operator import add
# from functools import partial
from bisect import bisect_left

""" 

"""
WAVEFORM_X_MARGIN = 5
WAVEFORM_H = 12
WAVEFORM_H_OFFSET = 16

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end
#---------------------------------------------------------------------------

class MyApp(wx.App):
    def OnInit(self):
        self.frame = layout.myFrame(None, wx.ID_ANY, "")
        
        self.frame.pnlCanvas.Bind(wx.EVT_PAINT, self.OnPaint)
        self.frame.wdTitle.Bind(wx.EVT_SCROLLWIN, self.OnTitleScroll)
        self.frame.wdCanvas.Bind(wx.EVT_SCROLLWIN, self.OnCanvasScroll)
        
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
        
        # 2rd menu
        menuZoom = wx.Menu()
        idZoom1 = wx.NewId()
        idZoom2 = wx.NewId()
        idZoom3 = wx.NewId()
        idZoom4 = wx.NewId()
        idZoom5 = wx.NewId()
        idZoom6 = wx.NewId()
        idZoom7 = wx.NewId()
        idZoom8 = wx.NewId()
        idZoom9 = wx.NewId()
        idZoom10 = wx.NewId()
        idZoom11 = wx.NewId()
        idZoom12 = wx.NewId()
        idZoom13 = wx.NewId()
        idZoom14 = wx.NewId()
        idZoom15 = wx.NewId()
        idZoom16 = wx.NewId()
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
        
        self.frame.SetMenuBar(menuBar)

        # and a file history
        self.filehistory = wx.FileHistory()
        self.filehistory.UseMenu(menu)

        self.zoom = 1
        self.arrow = [0, 0, 0, 0]
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.timer.Start(100)    # ms
        
        self.frame.Bind(wx.EVT_MENU, self.OnOpenFile, id=wx.ID_OPEN)
        self.frame.Bind(wx.EVT_MENU, self.OnExitApp, id=wx.ID_EXIT)
        self.frame.Bind(
            wx.EVT_MENU_RANGE, self.OnFileHistory, id=wx.ID_FILE1, id2=wx.ID_FILE9
            )
        self.frame.Bind(wx.EVT_WINDOW_DESTROY, self.Cleanup)
        
        self.frame.Bind(wx.EVT_MENU, self.OnZoom1, id = idZoom1)
        self.frame.Bind(wx.EVT_MENU, self.OnZoom2, id = idZoom2)
        self.frame.Bind(wx.EVT_MENU, self.OnZoom3, id = idZoom3)
        self.frame.Bind(wx.EVT_MENU, self.OnZoom4, id = idZoom4)
        self.frame.Bind(wx.EVT_MENU, self.OnZoom5, id = idZoom5)
        self.frame.Bind(wx.EVT_MENU, self.OnZoom6, id = idZoom6)
        self.frame.Bind(wx.EVT_MENU, self.OnZoom7, id = idZoom7)
        self.frame.Bind(wx.EVT_MENU, self.OnZoom8, id = idZoom8)
        self.frame.Bind(wx.EVT_MENU, self.OnZoom9, id = idZoom9)
        self.frame.Bind(wx.EVT_MENU, self.OnZoom10, id = idZoom10)
        self.frame.Bind(wx.EVT_MENU, self.OnZoom11, id = idZoom11)
        self.frame.Bind(wx.EVT_MENU, self.OnZoom12, id = idZoom12)
        self.frame.Bind(wx.EVT_MENU, self.OnZoom13, id = idZoom13)
        self.frame.Bind(wx.EVT_MENU, self.OnZoom14, id = idZoom14)
        self.frame.Bind(wx.EVT_MENU, self.OnZoom15, id = idZoom15)
        self.frame.Bind(wx.EVT_MENU, self.OnZoom16, id = idZoom16)

#        self.frame.Center(wx.HORIZONTAL | wx.VERTICAL)
        
        self.SetTopWindow(self.frame)
        self.frame.Show()
        
        self.originWave = []
        self.waveform = []
############################################
#         file = open('.\\dummy.txt', 'rU')
#         lstData = file.readlines()
#         file.close()
#         self.waveform = Parser(lstData)
#         self.frame.pnlCanvas.SetMinSize((self.waveform[0][0], 32 * WAVEFORM_H_OFFSET))
        
#         self.frame.label1.SetLabel('')
        
#         self.OnExitApp()
############################################
        
        return True
    
    def OnTimer(self, evt):
        pos = wx.GetMousePosition()
        rect = self.frame.wdCanvas.GetRect()
        pos = self.frame.ScreenToClient(pos)
        if rect.Contains(pos):
            if 0 < len(self.waveform):
                (pos.x, pos.y) = self.frame.wdCanvas.CalcUnscrolledPosition((pos.x, pos.y))
                line = pos.y / WAVEFORM_H_OFFSET
                idx = self.SearchIndex(pos.x - WAVEFORM_X_MARGIN - rect.x, line)
                arrowNew = [0,0,0,0]
                arrowNew[0] = self.waveform[1][line][idx-1][0] + 2 + WAVEFORM_X_MARGIN
                arrowNew[2] = self.waveform[1][line][idx][0] - 2 + WAVEFORM_X_MARGIN
                arrowNew[1] = arrowNew[3] = line * WAVEFORM_H_OFFSET + WAVEFORM_H / 2
                if self.arrow != arrowNew:
                    self.arrow = arrowNew
                    self.frame.wdCanvas.Refresh(False)
    
    def SearchIndex(self, px, py):
        l_x = [p[0] for p in self.waveform[1][py]]
        return bisect_left(l_x, px)
    
    def OnPaint(self, evt = None):
        dc = wx.PaintDC(self.frame.pnlCanvas)
        dc.Clear()
        if 0 < len(self.waveform):
            for i, w in enumerate(self.waveform[1]):
                dc.SetPen(wx.Pen(wx.BLACK, 1))
                self.DrawWave(dc, w, WAVEFORM_X_MARGIN, WAVEFORM_H_OFFSET * i)
#            dc.DrawLine(self.arrow[0], self.arrow[1], self.arrow[2], self.arrow[3])
            self.DrawArrow(dc, self.arrow)

    def DrawWave(self, dc, coord, x_margin, y_offset):
        for c0, c1 in zip(coord[0:], coord[1:]):
            dc.DrawLine(c0[0] + x_margin, c0[1] * WAVEFORM_H + y_offset, c1[0] + x_margin, c0[1] * WAVEFORM_H + y_offset)
            dc.DrawLine(c1[0] + x_margin, c0[1] * WAVEFORM_H + y_offset, c1[0] + x_margin, c1[1] * WAVEFORM_H + y_offset)
    
    def DrawArrow(self, dc, coord):
        dc.DrawLine(coord[0], coord[1], coord[2], coord[3])
        dc.DrawLines([[coord[0]+2,coord[1]-2],[coord[0],coord[1]],[coord[0]+3,coord[1]+3]])
        dc.DrawLines([[coord[2]-2,coord[3]-2],[coord[2],coord[3]],[coord[2]-3,coord[3]+3]])
            
            
    def OnZoom1(self, evt):
        self.zoom = 500.0 / 100
        self.waveform[1] = [[(p[0]*self.zoom, p[1]) for p in line] for line in self.originWave[1]]
        self.frame.wdCanvas.Refresh(False)
    def OnZoom2(self, evt):
        self.zoom = 400.0 / 100
        self.waveform[1] = [[(p[0]*self.zoom, p[1]) for p in line] for line in self.originWave[1]]
        self.frame.wdCanvas.Refresh(False)
    def OnZoom3(self, evt):
        self.zoom = 300.0 / 100
        self.waveform[1] = [[(p[0]*self.zoom, p[1]) for p in line] for line in self.originWave[1]]
        self.frame.wdCanvas.Refresh(False)
    def OnZoom4(self, evt):
        self.zoom = 250.0 / 100
        self.waveform[1] = [[(p[0]*self.zoom, p[1]) for p in line] for line in self.originWave[1]]
        self.frame.wdCanvas.Refresh(False)
    def OnZoom5(self, evt):
        self.zoom = 200.0 / 100
        self.waveform[1] = [[(p[0]*self.zoom, p[1]) for p in line] for line in self.originWave[1]]
        self.frame.wdCanvas.Refresh(False)
    def OnZoom6(self, evt):
        self.zoom = 150.0 / 100
        self.waveform[1] = [[(p[0]*self.zoom, p[1]) for p in line] for line in self.originWave[1]]
        self.frame.wdCanvas.Refresh(False)
    def OnZoom7(self, evt):
        self.zoom = 100.0 / 100
        self.waveform[1] = [[(p[0]*self.zoom, p[1]) for p in line] for line in self.originWave[1]]
        self.frame.wdCanvas.Refresh(False)
    def OnZoom8(self, evt):
        self.zoom = 90.0 / 100
        self.waveform[1] = [[(p[0]*self.zoom, p[1]) for p in line] for line in self.originWave[1]]
        self.frame.wdCanvas.Refresh(False)
    def OnZoom9(self, evt):
        self.zoom = 80.0 / 100
        self.waveform[1] = [[(p[0]*self.zoom, p[1]) for p in line] for line in self.originWave[1]]
        self.frame.wdCanvas.Refresh(False)
    def OnZoom10(self, evt):
        self.zoom = 70.0 / 100
        self.waveform[1] = [[(p[0]*self.zoom, p[1]) for p in line] for line in self.originWave[1]]
        self.frame.wdCanvas.Refresh(False)
    def OnZoom11(self, evt):
        self.zoom = 60.0 / 100
        self.waveform[1] = [[(p[0]*self.zoom, p[1]) for p in line] for line in self.originWave[1]]
        self.frame.wdCanvas.Refresh(False)
    def OnZoom12(self, evt):
        self.zoom = 50.0 / 100
        self.waveform[1] = [[(p[0]*self.zoom, p[1]) for p in line] for line in self.originWave[1]]
        self.frame.wdCanvas.Refresh(False)
    def OnZoom13(self, evt):
        self.zoom = 40.0 / 100
        self.waveform[1] = [[(p[0]*self.zoom, p[1]) for p in line] for line in self.originWave[1]]
        self.frame.wdCanvas.Refresh(False)
    def OnZoom14(self, evt):
        self.zoom = 30.0 / 100
        self.waveform[1] = [[(p[0]*self.zoom, p[1]) for p in line] for line in self.originWave[1]]
        self.frame.wdCanvas.Refresh(False)
    def OnZoom15(self, evt):
        self.zoom = 20.0 / 100
        self.waveform[1] = [[(p[0]*self.zoom, p[1]) for p in line] for line in self.originWave[1]]
        self.frame.wdCanvas.Refresh(False)
    def OnZoom16(self, evt):
        self.zoom = 10.0 / 100
        self.waveform[1] = [[(p[0]*self.zoom, p[1]) for p in line] for line in self.originWave[1]]
        self.frame.wdCanvas.Refresh(False)
        
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
#        self.menu.Destroy()
    
    def OnOpenFile(self, evt):
        dlg = wx.FileDialog(self.frame,
                           defaultDir = os.getcwd(),
                           wildcard = "All Files|*",
                           style = wx.OPEN | wx.CHANGE_DIR)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            print "You selected %s\n" % path,

            # add it to the history
            self.filehistory.AddFileToHistory(path)
            
            # read file
            file = open(path, 'rU')
            
            # read file's all lines to a list
            lstData = file.readlines()
            
            file.close()
            
            self.frame.pnlCanvas.Refresh()      # clear the canvas
            self.originWave = Parser(lstData)
            self.waveform = self.originWave[:]
            self.frame.pnlCanvas.SetSize((self.waveform[0] + 2 * WAVEFORM_X_MARGIN, 32 * WAVEFORM_H_OFFSET))
            self.frame.pnlCanvas.SetMinSize((self.waveform[0] + 2 * WAVEFORM_X_MARGIN, 32 * WAVEFORM_H_OFFSET))
            self.frame.wdCanvas.SetScrollbar(wx.HORIZONTAL | wx.VERTICAL, 1, 1, 10)
            
        dlg.Destroy()
        
        
    def OnFileHistory(self, evt):
        # get the file based on the menu ID
        fileNum = evt.GetId() - wx.ID_FILE1
        path = self.filehistory.GetHistoryFile(fileNum)
        print "You selected %s\n" % path,

        # add it back to the history so it will be moved up the list
        self.filehistory.AddFileToHistory(path)

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
        print matrix
        return [int(list[-1][0], 16) - int(list[0][0], 16), matrix]
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
