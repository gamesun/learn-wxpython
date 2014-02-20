import wx
from wx.lib.delayedresult import startWorker
import array

#=============================================================================
class DrawPanel(wx.Panel):
    """
    Basic panel with graphics drawn in Pain Event
    """
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

    #-------------------------------------------------------------------------
    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.SetBackground(wx.Brush(wx.BLACK))
        dc.Clear()
        w, h = self.GetClientSizeTuple()
        dc.DrawCirclePoint((w / 2, h / 2), 50)

    #-------------------------------------------------------------------------
    def OnSize(self, event):
        self.Refresh()
        self.Update()

    #-------------------------------------------------------------------------
    def OnEraseBackground(self, event):
        pass # Or None

#============================================================================= 
class DrawPanelDB(wx.Panel):
    """
    Basic panel with graphics drawn in Pain Event using Double Buffering
    """
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

    #-------------------------------------------------------------------------
    def OnPaint(self, event):
        # Switches the buffers when 'dc' goes out of scope
        dc = wx.BufferedPaintDC(self)
        dc.SetBackground(wx.Brush(wx.BLACK))
        dc.Clear()
        w, h = self.GetClientSizeTuple()
        dc.DrawCirclePoint((w / 2, h / 2), 50)

    #-------------------------------------------------------------------------
    def OnSize(self, event):
        self.Refresh()
        self.Update()

    #-------------------------------------------------------------------------
    def OnEraseBackground(self, event):
        pass # Or None

#=============================================================================
class DrawPanelDBT(wx.Panel):
    """
    Complex panel with its content drawn in another thread
    """
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)

        self.t = None
        self.w, self.h = self.GetClientSizeTuple()
        self.buffer = wx.EmptyBitmap(self.w, self.h)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)

        self.SizeUpdate()

    #-------------------------------------------------------------------------
    def OnPaint(self, event):
        # Just draw prepared bitmap
        wx.BufferedPaintDC(self, self.buffer)

    #-------------------------------------------------------------------------
    def OnSize(self, event):
        self.w, self.h = self.GetClientSizeTuple()
        self.buffer = wx.EmptyBitmap(self.w, self.h)
        self.Refresh()
        self.Update()
        # After drawing empty bitmap start update
        self.SizeUpdate()

    #-------------------------------------------------------------------------
    def OnEraseBackground(self, event):
        pass # Or None

    #-------------------------------------------------------------------------
    def OnTimer(self, event):
        # Start another thread which will update the bitmap
        # But only if another is not still running!
        if self.t is None:
            self.timer.Stop()
            self.t = startWorker(self.ComputationDone, self.Compute)

    #-------------------------------------------------------------------------
    def SizeUpdate(self):
        # The timer is used to wait for last thread to finish
        self.timer.Stop()
        self.timer.Start(100)

    #-------------------------------------------------------------------------
    def Compute(self):
        # Compute Fractal
        MI = 20

        def mapme(x, minimal, maximal, newmin, newmax):
            return(((float(x) - minimal) / (maximal - minimal)) 
                   * (newmax - newmin) + newmin)

        def compute(x, y):
            z = complex(0, 0)
            c = complex(x, y)
            for i in range(MI):
                z = z**2 + c
                if abs(z) > 2:
                    return i+1
            return 0

        def color(i):
            a = int(mapme(i, 1, MI, 0, 255))
            return(a, a, a)

        def compute_buff(x1, x2, y1, y2, w, h):
            buffer = array.array('B') 
            for y in range(h):
                for x in range(w):
                    i = compute(mapme(x, 0, w, x1, x2),
                                mapme(y, 0, h, y2, y1))
                    if i == 0:
                        buffer.extend((255, 255, 255))
                    else:
                        buffer.extend(color(i))
            return buffer

        width, height = self.w, self.h
        x = -0.5
        y =  0.0
        w =  2.4
        h = w * height / width
        data = compute_buff(x - w/2, x + w/2, y - h/2, y + h/2, width, height)
        temp_buffer = wx.BitmapFromBuffer(width, height, data)
        return temp_buffer

    #-------------------------------------------------------------------------
    def ComputationDone(self, r):
        # When done, take bitmap and place it to the drawing buffer
        # Invalidate panel, so it is redrawn
        # But not if the later thread is waiting!
        temp = r.get()
        if not self.timer.IsRunning():
            self.buffer = temp
            self.Refresh()
            self.Update()
        self.t = None

#=============================================================================
class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.panel = wx.Panel(self)
        self.drawing = DrawPanel(self.panel, size=(300, 300))
        self.drawingDB = DrawPanelDB(self.panel, size=(300, 300))
        self.drawingDBT = DrawPanelDBT(self.panel, size=(300, 300))
        self.sizerPanel = wx.BoxSizer()
        self.sizerPanel.Add(self.panel, proportion=1, flag=wx.EXPAND)
        self.sizerMain = wx.BoxSizer()
        self.sizerMain.Add(self.drawing, 1, wx.ALL | wx.EXPAND, 5)
        self.sizerMain.Add(self.drawingDB, 1, wx.ALL | wx.EXPAND, 5)
        self.sizerMain.Add(self.drawingDBT, 1, wx.ALL | wx.EXPAND, 5)
        self.panel.SetSizerAndFit(self.sizerMain)
        self.SetSizerAndFit(self.sizerPanel)      
        self.Show()

app = wx.App(False)
win = MainWindow(None)
app.MainLoop()