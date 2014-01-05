#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.7 (standalone edition) on Sun Jan 05 22:38:59 2014
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class myFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: myFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.mainframe_statusbar = self.CreateStatusBar(1, wx.ST_SIZEGRIP)
        self.pnlmain = wx.Panel(self, wx.ID_ANY)
        self.window_1 = wx.SplitterWindow(self.pnlmain, wx.ID_ANY, style=wx.SP_3DBORDER | wx.SP_BORDER | wx.SP_LIVE_UPDATE)
        self.wdTitle = wx.ScrolledWindow(self.window_1, wx.ID_ANY, style=wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        self.label_1 = wx.StaticText(self.wdTitle, wx.ID_ANY, "31:")
        self.label_2 = wx.StaticText(self.wdTitle, wx.ID_ANY, "30:")
        self.label_3 = wx.StaticText(self.wdTitle, wx.ID_ANY, "29:")
        self.label_4 = wx.StaticText(self.wdTitle, wx.ID_ANY, "28:")
        self.label_5 = wx.StaticText(self.wdTitle, wx.ID_ANY, "27:")
        self.label_6 = wx.StaticText(self.wdTitle, wx.ID_ANY, "26:")
        self.label_7 = wx.StaticText(self.wdTitle, wx.ID_ANY, "25:")
        self.label_8 = wx.StaticText(self.wdTitle, wx.ID_ANY, "24:")
        self.label_9 = wx.StaticText(self.wdTitle, wx.ID_ANY, "23:")
        self.label_10 = wx.StaticText(self.wdTitle, wx.ID_ANY, "22:")
        self.label_11 = wx.StaticText(self.wdTitle, wx.ID_ANY, "21:")
        self.label_12 = wx.StaticText(self.wdTitle, wx.ID_ANY, "20:")
        self.label_13 = wx.StaticText(self.wdTitle, wx.ID_ANY, "19:")
        self.label_14 = wx.StaticText(self.wdTitle, wx.ID_ANY, "18:")
        self.label_15 = wx.StaticText(self.wdTitle, wx.ID_ANY, "17:")
        self.label_16 = wx.StaticText(self.wdTitle, wx.ID_ANY, "16:")
        self.label_17 = wx.StaticText(self.wdTitle, wx.ID_ANY, "15:")
        self.label_18 = wx.StaticText(self.wdTitle, wx.ID_ANY, "14:")
        self.label_19 = wx.StaticText(self.wdTitle, wx.ID_ANY, "13:")
        self.label_20 = wx.StaticText(self.wdTitle, wx.ID_ANY, "12:")
        self.label_21 = wx.StaticText(self.wdTitle, wx.ID_ANY, "11:")
        self.label_22 = wx.StaticText(self.wdTitle, wx.ID_ANY, "10:")
        self.label_23 = wx.StaticText(self.wdTitle, wx.ID_ANY, "09:")
        self.label_24 = wx.StaticText(self.wdTitle, wx.ID_ANY, "08:")
        self.label_25 = wx.StaticText(self.wdTitle, wx.ID_ANY, "07:")
        self.label_26 = wx.StaticText(self.wdTitle, wx.ID_ANY, "06:")
        self.label_27 = wx.StaticText(self.wdTitle, wx.ID_ANY, "05:")
        self.label_28 = wx.StaticText(self.wdTitle, wx.ID_ANY, "04:")
        self.label_29 = wx.StaticText(self.wdTitle, wx.ID_ANY, "03:")
        self.label_30 = wx.StaticText(self.wdTitle, wx.ID_ANY, "02:")
        self.label_31 = wx.StaticText(self.wdTitle, wx.ID_ANY, "01:")
        self.label_32 = wx.StaticText(self.wdTitle, wx.ID_ANY, "00:")
        self.label_blank = wx.StaticText(self.wdTitle, wx.ID_ANY, "")
        self.wdCanvas = wx.ScrolledWindow(self.window_1, wx.ID_ANY, style=wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        self.pnlCanvas = wx.Panel(self.wdCanvas, wx.ID_ANY)
        self.pnlMeasure = wx.Panel(self.pnlmain, wx.ID_ANY, style=wx.STATIC_BORDER | wx.TAB_TRAVERSAL)
        self.lblMeasure11 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "Measure")
        self.lblMeasure12 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "Measure")
        self.lblMeasure13 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "Measure")
        self.lblMeasure21 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "Measure")
        self.lblMeasure22 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "Measure")
        self.lblMeasure23 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "Measure")
        self.lblMeasure_T1 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "    T1    ")
        self.lblMeasure_T2 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "    T2    ")
        self.lblMeasure_T3 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "    T3    ")
        self.lblMeasure_T4 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "    T4    ")
        self.lblMeasure_T5 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "    T5    ")
        self.lblMeasure_T6 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "    T6    ")
        self.lblMeasure_T7 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "    T7    ")
        self.lblMeasure_T8 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "    T8    ")
        self.label_33 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "|T1-T2|=")
        self.label_34 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "|T2-T3|=")
        self.label_35 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "|T3-T4|=")
        self.label_36 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "|T4-T5|=")
        self.label_37 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "|T5-T6|=")
        self.label_38 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "|T6-T7|=")
        self.label_39 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "|T7-T8|=")
        self.label_T1 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "1")
        self.label_T2 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "2")
        self.label_T3 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "3")
        self.label_T4 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "4")
        self.label_T5 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "5")
        self.label_T6 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "6")
        self.label_T7 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "7")
        self.label_T8 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "8")
        self.label_sub12 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "sub12")
        self.label_sub23 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "sub23")
        self.label_sub34 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "sub34")
        self.label_sub45 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "sub45")
        self.label_sub56 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "sub56")
        self.label_sub67 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "sub67")
        self.label_sub78 = wx.StaticText(self.pnlMeasure, wx.ID_ANY, "sub78")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: myFrame.__set_properties
        self.SetTitle("Tool")
        self.mainframe_statusbar.SetStatusWidths([-1])
        # statusbar fields
        mainframe_statusbar_fields = ["mainframe_statusbar"]
        for i in range(len(mainframe_statusbar_fields)):
            self.mainframe_statusbar.SetStatusText(mainframe_statusbar_fields[i], i)
        self.label_1.SetMinSize((-1, 16))
        self.label_2.SetMinSize((-1, 16))
        self.label_3.SetMinSize((-1, 16))
        self.label_4.SetMinSize((-1, 16))
        self.label_5.SetMinSize((-1, 16))
        self.label_6.SetMinSize((-1, 16))
        self.label_7.SetMinSize((-1, 16))
        self.label_8.SetMinSize((-1, 16))
        self.label_9.SetMinSize((-1, 16))
        self.label_10.SetMinSize((-1, 16))
        self.label_11.SetMinSize((-1, 16))
        self.label_12.SetMinSize((-1, 16))
        self.label_13.SetMinSize((-1, 16))
        self.label_14.SetMinSize((-1, 16))
        self.label_15.SetMinSize((-1, 16))
        self.label_16.SetMinSize((-1, 16))
        self.label_17.SetMinSize((-1, 16))
        self.label_18.SetMinSize((-1, 16))
        self.label_19.SetMinSize((-1, 16))
        self.label_20.SetMinSize((-1, 16))
        self.label_21.SetMinSize((-1, 16))
        self.label_22.SetMinSize((-1, 16))
        self.label_23.SetMinSize((-1, 16))
        self.label_24.SetMinSize((-1, 16))
        self.label_25.SetMinSize((-1, 16))
        self.label_26.SetMinSize((-1, 16))
        self.label_27.SetMinSize((-1, 16))
        self.label_28.SetMinSize((-1, 16))
        self.label_29.SetMinSize((-1, 16))
        self.label_30.SetMinSize((-1, 16))
        self.label_31.SetMinSize((-1, 16))
        self.label_32.SetMinSize((-1, 16))
        self.label_blank.SetMinSize((100, 17))
        self.wdTitle.SetMinSize((105, -1))
        self.wdTitle.SetScrollRate(1, 1)
        self.pnlCanvas.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.wdCanvas.SetMinSize((326, 337))
        self.wdCanvas.SetScrollRate(10, 1)
        self.lblMeasure11.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "Consolas"))
        self.lblMeasure12.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "Consolas"))
        self.lblMeasure13.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "Consolas"))
        self.lblMeasure21.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "Consolas"))
        self.lblMeasure22.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "Consolas"))
        self.lblMeasure23.SetFont(wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "Consolas"))
        self.lblMeasure_T1.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 1, ""))
        self.lblMeasure_T2.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 1, ""))
        self.lblMeasure_T3.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 1, ""))
        self.lblMeasure_T4.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 1, ""))
        self.lblMeasure_T5.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 1, ""))
        self.lblMeasure_T6.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 1, ""))
        self.lblMeasure_T7.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 1, ""))
        self.lblMeasure_T8.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.BOLD, 1, ""))
        self.pnlmain.SetMinSize((850, 580))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: myFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_3.Add((20, 10), 0, 0, 0)
        sizer_3.Add(self.label_1, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_2, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_3, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_4, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_5, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_6, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_7, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_8, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_9, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_10, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_11, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_12, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_13, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_14, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_15, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_16, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_17, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_18, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_19, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_20, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_21, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_22, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_23, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_24, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_25, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_26, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_27, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_28, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_29, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_30, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_31, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_32, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_blank, 1, wx.SHAPED, 0)
        self.wdTitle.SetSizer(sizer_3)
        sizer_4.Add(self.pnlCanvas, 1, wx.EXPAND | wx.FIXED_MINSIZE, 0)
        self.wdCanvas.SetSizer(sizer_4)
        self.window_1.SplitVertically(self.wdTitle, self.wdCanvas, 105)
        sizer_2.Add(self.window_1, 1, wx.EXPAND, 0)
        sizer_6.Add(self.lblMeasure11, 0, 0, 0)
        sizer_6.Add(self.lblMeasure12, 0, 0, 0)
        sizer_6.Add(self.lblMeasure13, 0, 0, 0)
        sizer_6.Add(self.lblMeasure21, 0, 0, 0)
        sizer_6.Add(self.lblMeasure22, 0, 0, 0)
        sizer_6.Add(self.lblMeasure23, 0, 0, 0)
        sizer_8.Add(self.lblMeasure_T1, 0, wx.LEFT | wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 1)
        sizer_8.Add(self.lblMeasure_T2, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 1)
        sizer_8.Add(self.lblMeasure_T3, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 1)
        sizer_8.Add(self.lblMeasure_T4, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 1)
        sizer_8.Add(self.lblMeasure_T5, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 1)
        sizer_8.Add(self.lblMeasure_T6, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 1)
        sizer_8.Add(self.lblMeasure_T7, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 1)
        sizer_8.Add(self.lblMeasure_T8, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 1)
        sizer_8.Add(self.label_33, 0, wx.BOTTOM, 1)
        sizer_8.Add(self.label_34, 0, wx.BOTTOM, 1)
        sizer_8.Add(self.label_35, 0, wx.BOTTOM, 1)
        sizer_8.Add(self.label_36, 0, wx.BOTTOM, 1)
        sizer_8.Add(self.label_37, 0, wx.BOTTOM, 1)
        sizer_8.Add(self.label_38, 0, wx.BOTTOM, 1)
        sizer_8.Add(self.label_39, 0, wx.BOTTOM, 1)
        sizer_7.Add(sizer_8, 1, wx.ALL | wx.EXPAND, 2)
        sizer_9.Add(self.label_T1, 0, wx.BOTTOM, 1)
        sizer_9.Add(self.label_T2, 0, wx.BOTTOM, 1)
        sizer_9.Add(self.label_T3, 0, wx.BOTTOM, 1)
        sizer_9.Add(self.label_T4, 0, wx.BOTTOM, 1)
        sizer_9.Add(self.label_T5, 0, wx.BOTTOM, 1)
        sizer_9.Add(self.label_T6, 0, wx.BOTTOM, 1)
        sizer_9.Add(self.label_T7, 0, wx.BOTTOM, 1)
        sizer_9.Add(self.label_T8, 0, wx.BOTTOM, 1)
        sizer_9.Add(self.label_sub12, 0, wx.BOTTOM, 1)
        sizer_9.Add(self.label_sub23, 0, wx.BOTTOM, 1)
        sizer_9.Add(self.label_sub34, 0, wx.BOTTOM, 1)
        sizer_9.Add(self.label_sub45, 0, wx.BOTTOM, 1)
        sizer_9.Add(self.label_sub56, 0, wx.BOTTOM, 1)
        sizer_9.Add(self.label_sub67, 0, wx.BOTTOM, 1)
        sizer_9.Add(self.label_sub78, 0, wx.BOTTOM, 1)
        sizer_7.Add(sizer_9, 1, wx.ALL | wx.EXPAND, 2)
        sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)
        self.pnlMeasure.SetSizer(sizer_6)
        sizer_5.Add(self.pnlMeasure, 1, wx.BOTTOM | wx.EXPAND, 1)
        sizer_2.Add(sizer_5, 0, wx.EXPAND, 0)
        self.pnlmain.SetSizer(sizer_2)
        sizer_1.Add(self.pnlmain, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade

# end of class myFrame
class MyApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        mainframe = myFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(mainframe)
        mainframe.Show()
        return 1

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()