
import sys,os
import wx

""" 

"""

#---------------------------------------------------------------------------

class MyFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, -1, title, size = (800,500), 
            style=wx.DEFAULT_FRAME_STYLE|wx.NO_FULL_REPAINT_ON_RESIZE)


        # make a statusbar
        self.CreateStatusBar()
        self.SetStatusText("This is the statusbar")

        # Make a menu
        menuBar = wx.MenuBar()

        # 1st menu from left
        menu = wx.Menu()
        menu.Append(wx.ID_NEW,     "&New")
        menu.Append(wx.ID_OPEN,    "&Open...")
        menu.Append(wx.ID_CLOSE,   "&Close")
        menu.Append(wx.ID_SAVE,    "&Save")
        menu.Append(wx.ID_SAVEAS,  "Save &as...")
        menu.Enable(wx.ID_NEW, False)
        menu.Enable(wx.ID_CLOSE, False)
        menu.Enable(wx.ID_SAVE, False)
        menu.Enable(wx.ID_SAVEAS, False)
        menuBar.Append(menu, "&File")

        self.SetMenuBar(menuBar)

        # and a file history
        self.filehistory = wx.FileHistory()
        self.filehistory.UseMenu(menu)

        self.Bind(wx.EVT_MENU, self.OnFileOpenDialog, id=wx.ID_OPEN)
        self.Bind(
            wx.EVT_MENU_RANGE, self.OnFileHistory, id=wx.ID_FILE1, id2=wx.ID_FILE9
            )
        self.Bind(wx.EVT_WINDOW_DESTROY, self.Cleanup)


        self.Show(True)


    def Cleanup(self, *args):
        # A little extra cleanup is required for the FileHistory control
        del self.filehistory
        self.menu.Destroy()

    def OnFileOpenDialog(self, evt):
        dlg = wx.FileDialog(self,
                           defaultDir = os.getcwd(),
                           wildcard = "All Files|*",
                           style = wx.OPEN | wx.CHANGE_DIR)

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            print "You selected %s\n" % path,

            # add it to the history
            self.filehistory.AddFileToHistory(path)

        dlg.Destroy()

    def OnFileHistory(self, evt):
        # get the file based on the menu ID
        fileNum = evt.GetId() - wx.ID_FILE1
        path = self.filehistory.GetHistoryFile(fileNum)
        print "You selected %s\n" % path,

        # add it back to the history so it will be moved up the list
        self.filehistory.AddFileToHistory(path)



#---------------------------------------------------------------------------

class App(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, "test")
        self.SetTopWindow(frame)

        return True

#---------------------------------------------------------------------------


overview = """\
"""


if __name__ == '__main__':
    app = App(0)
    app.MainLoop()
