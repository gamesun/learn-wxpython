# -*- coding:utf-8 -*-

import sys,os
import wx
from wx import xrc
import OpenGLMdl as glmdl
import layout as lyt
import DataParser as dp
from operator import add
from functools import partial

""" 

"""

#---------------------------------------------------------------------------

class MyApp(wx.App):
    def OnInit(self):
#        self.res = xrc.XmlResource('res.xrc')
#        self.frame = self.res.LoadFrame(None, 'mainframe')
#        scrollwin = xrc.XRCCTRL(self.frame, 'scrollwin')
#        scrollwin.SetScrollbars(1,1,1,1)
#        self.pnlCanvas = xrc.XRCCTRL(self.frame, 'pnlCanvas')
        
        #wx.InitAllImageHandlers()
        self.frame = lyt.myFrame(None, wx.ID_ANY, "")
        
#         sizer = wx.BoxSizer(wx.HORIZONTAL)
#         self.canvas = glmdl.CubeCanvas(self.frame.pnlCanvas)
#         self.canvas.SetMinSize((1500, 450))
# #        sizer.Add(self.canvas, 1, wx.EXPAND|wx.ALL, 0)
#         sizer.Add(self.canvas, 1, wx.SHAPED|wx.ALL, 0)
#         self.frame.pnlCanvas.SetAutoLayout(True)
#         self.frame.pnlCanvas.SetSizer(sizer)
        
#         self.frame.pnlCanvas.Bind(wx.EVT_SCROLLWIN, self.OnScroll)
#         self.frame.pnlCanvas.Bind(wx.EVT_PAINT, self.OnEraseBakGnd)
#         self.frame.pnlmain.Bind(wx.EVT_SCROLLWIN, self.OnScroll)
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

        self.frame.Bind(wx.EVT_MENU, self.OnOpenFile, id=wx.ID_OPEN)
        self.frame.Bind(wx.EVT_MENU, self.OnExitApp, id=wx.ID_EXIT)
        self.frame.Bind(
            wx.EVT_MENU_RANGE, self.OnFileHistory, id=wx.ID_FILE1, id2=wx.ID_FILE9
            )
        self.frame.Bind(wx.EVT_WINDOW_DESTROY, self.Cleanup)

#        self.frame.SetSize((100,100))
#        self.frame.Center(wx.HORIZONTAL | wx.VERTICAL)
        
        self.SetTopWindow(self.frame)
        self.frame.Show()
        
############################################
        file = open('.\\dummy.txt', 'rU')
        lstData = file.readlines()
        file.close()
        waveform = dp.Parser(lstData)
        print waveform

#         self.frame.label1.SetLabel('')
        
#        self.OnExitApp(None)
############################################
        
        return True
    
    def OnPaint(self, evt=None):
        dc = wx.PaintDC(self.frame.pnlCanvas)
        dc.Clear()
        dc.SetPen(wx.Pen(wx.BLACK, 2))
        dc.DrawLine(0, 0, 500, 500)
    
#     def OnEraseBakGnd(self, evt):
#         #dc = wx.PaintDC(self.frame.pnlCanvas)
#         #dc.Clear()
#         #dc.SetPen(wx.Pen(wx.BLACK, 4))
#         #dc.DrawLine(0, 0, 50, 50)
#         wx.CallLater(100, self.OnScrolled)
#         evt.Skip()
#     
#     def OnScroll(self, evt):
#         wx.CallAfter(self.OnScrolled)
#         evt.Skip()
# #        self.frame.scrollwin.Scroll( x=0, y=self.frame.scrollwin.CalcScrollInc(evt))
# 
#     def OnScrolled(self):
#         if (self.canvas):
#             self.canvas.Refresh(False)
    
    def OnTitleScroll(self, evt=None):
        wx.CallAfter(self.OnTitleScrolled)
        evt.Skip()
        
    def OnTitleScrolled(self):
        x,y = self.frame.wdTitle.GetViewStart()
        self.frame.wdCanvas.Scroll(-1, y)

    def OnCanvasScroll(self, evt=None):
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
            
            dp.Parser(self.frame.pnlCanvas, self.canvas, lstData)
            
        dlg.Destroy()
        
        
        
    def OnFileHistory(self, evt):
        # get the file based on the menu ID
        fileNum = evt.GetId() - wx.ID_FILE1
        path = self.filehistory.GetHistoryFile(fileNum)
        print "You selected %s\n" % path,

        # add it back to the history so it will be moved up the list
        self.filehistory.AddFileToHistory(path)
   
    def OnExitApp(self, evt):
        self.frame.Close(True)

#---------------------------------------------------------------------------


overview = """\
"""


if __name__ == '__main__':
    app = MyApp(0)
#    app = glmdl.RunDemoApp()
    app.MainLoop()
