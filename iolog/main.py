# -*- coding:utf-8 -*-

import sys,os
import wx
# from wx import xrc
# import OpenGLMdl as glmdl
import layout
import DataParser as dp
# from operator import add
# from functools import partial

""" 

"""
WAVEFORM_W = 5
WAVEFORM_H = 12
WAVEFORM_H_OFFSET = 16
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

        self.frame.SetMenuBar(menuBar)

        # and a file history
        self.filehistory = wx.FileHistory()
        self.filehistory.UseMenu(menu)


        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.timer.Start(100)    # ms
        
        self.frame.Bind(wx.EVT_MENU, self.OnOpenFile, id=wx.ID_OPEN)
        self.frame.Bind(wx.EVT_MENU, self.OnExitApp, id=wx.ID_EXIT)
        self.frame.Bind(
            wx.EVT_MENU_RANGE, self.OnFileHistory, id=wx.ID_FILE1, id2=wx.ID_FILE9
            )
        self.frame.Bind(wx.EVT_WINDOW_DESTROY, self.Cleanup)

#        self.frame.Center(wx.HORIZONTAL | wx.VERTICAL)
        
        self.SetTopWindow(self.frame)
        self.frame.Show()
        
        self.waveform = []
############################################
#         file = open('.\\dummy.txt', 'rU')
#         lstData = file.readlines()
#         file.close()
#         self.waveform = dp.Parser(lstData)
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
            print pos.x, pos.y
    
    def OnPaint(self, evt = None):
        dc = wx.PaintDC(self.frame.pnlCanvas)
        dc.Clear()
        if 0 < len(self.waveform):
            for i, w in enumerate(self.waveform[1]):
                dc.SetPen(wx.Pen(wx.BLACK, 1))
                self.DrawWave(dc, w, WAVEFORM_W, WAVEFORM_H_OFFSET * (31-i))

    def DrawWave(self, dc, coord, x_offset, y_offset):
        for c0, c1 in zip(coord[0:], coord[1:]):
            dc.DrawLine(c0[0] + x_offset, c0[1] * WAVEFORM_H + y_offset, c1[0] + x_offset, c0[1] * WAVEFORM_H + y_offset)
            dc.DrawLine(c1[0] + x_offset, c0[1] * WAVEFORM_H + y_offset, c1[0] + x_offset, c1[1] * WAVEFORM_H + y_offset)
    
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
            self.waveform = dp.Parser(lstData)
            self.frame.pnlCanvas.SetSize((self.waveform[0] + 2 * WAVEFORM_W, 32 * WAVEFORM_H_OFFSET))
            self.frame.pnlCanvas.SetMinSize((self.waveform[0] + 2 * WAVEFORM_W, 32 * WAVEFORM_H_OFFSET))
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
    Parser(list) -> [ duration,    info
                      [((x1,y1), (x2,y2), ... (xn,yn)),    #wave 1
                      (...),                               #wave 2
                      ...  ]]
    """

    RawData = [g_match.search(l) for l in lines]                                    # get the origin data
    list = [(r.group('time'), r.group('value')) for r in RawData if r is not None]  # filter the null data
    list.sort()
    
    if 0 < len(list):
        matrix = [[(int(l[0], 16), int(v)) for v in bits(int(l[1], 16), 32)] for l in list]
        return (int(list[-1][0], 16) - int(list[0][0], 16), zip(*matrix))
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
