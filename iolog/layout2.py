# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2013)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.combo

###########################################################################
## Class myFrame
###########################################################################

class myFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tool", pos = wx.DefaultPosition, size = wx.Size( 925,680 ), style = wx.DEFAULT_FRAME_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.mainframe_statusbar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.pnlmain = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 850, 610 ), wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.window_1 = wx.SplitterWindow( self.pnlmain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3DBORDER|wx.SP_BORDER|wx.SP_LIVE_UPDATE )
		self.window_1.Bind( wx.EVT_IDLE, self.window_1OnIdle )
		
		self.wdTitle = wx.ScrolledWindow( self.window_1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 70,-1 ), wx.HSCROLL|wx.VSCROLL )
		self.wdTitle.SetScrollRate( 5, 5 )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.label_topSpacer = wx.StaticText( self.wdTitle, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_topSpacer.Wrap( 0 )
		bSizer4.Add( self.label_topSpacer, 0, 0, 0 )
		
		self.label_1 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"31:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_1.Wrap( 0 )
		bSizer4.Add( self.label_1, 0, wx.EXPAND, 0 )
		
		self.bcombo1 = wx.combo.BitmapComboBox( self.wdTitle, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,17 ), "", wx.CB_READONLY ) 
		bSizer4.Add( self.bcombo1, 0, wx.EXPAND, 5 )
		
		self.label_2 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"30:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_2.Wrap( 0 )
		bSizer4.Add( self.label_2, 0, wx.EXPAND, 0 )
		
		self.label_3 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"29:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_3.Wrap( 0 )
		bSizer4.Add( self.label_3, 0, wx.EXPAND, 0 )
		
		self.label_4 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"28:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_4.Wrap( 0 )
		bSizer4.Add( self.label_4, 0, wx.EXPAND, 0 )
		
		self.label_5 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"27:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_5.Wrap( 0 )
		bSizer4.Add( self.label_5, 0, wx.EXPAND, 0 )
		
		self.label_6 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"26:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_6.Wrap( 0 )
		bSizer4.Add( self.label_6, 0, wx.EXPAND, 0 )
		
		self.label_7 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"25:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_7.Wrap( 0 )
		bSizer4.Add( self.label_7, 0, wx.EXPAND, 0 )
		
		self.label_8 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"24:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_8.Wrap( 0 )
		bSizer4.Add( self.label_8, 0, wx.EXPAND, 0 )
		
		self.label_9 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"23:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_9.Wrap( 0 )
		bSizer4.Add( self.label_9, 0, wx.EXPAND, 0 )
		
		self.label_10 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"22:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_10.Wrap( 0 )
		bSizer4.Add( self.label_10, 0, wx.EXPAND, 0 )
		
		self.label_11 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"21:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_11.Wrap( 0 )
		bSizer4.Add( self.label_11, 0, wx.EXPAND, 0 )
		
		self.label_12 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"20:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_12.Wrap( 0 )
		bSizer4.Add( self.label_12, 0, wx.EXPAND, 0 )
		
		self.label_13 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"19:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_13.Wrap( 0 )
		bSizer4.Add( self.label_13, 0, wx.EXPAND, 0 )
		
		self.label_14 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"18:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_14.Wrap( 0 )
		bSizer4.Add( self.label_14, 0, wx.EXPAND, 0 )
		
		self.label_15 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"17:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_15.Wrap( 0 )
		bSizer4.Add( self.label_15, 0, wx.EXPAND, 0 )
		
		self.label_16 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"16:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_16.Wrap( 0 )
		bSizer4.Add( self.label_16, 0, wx.EXPAND, 0 )
		
		self.label_17 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"15:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_17.Wrap( 0 )
		bSizer4.Add( self.label_17, 0, wx.EXPAND, 0 )
		
		self.label_18 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"14:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_18.Wrap( 0 )
		bSizer4.Add( self.label_18, 0, wx.EXPAND, 0 )
		
		self.label_19 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"13:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_19.Wrap( 0 )
		bSizer4.Add( self.label_19, 0, wx.EXPAND, 0 )
		
		self.label_20 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"12:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_20.Wrap( 0 )
		bSizer4.Add( self.label_20, 0, wx.EXPAND, 0 )
		
		self.label_21 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"11:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_21.Wrap( 0 )
		bSizer4.Add( self.label_21, 0, wx.EXPAND, 0 )
		
		self.label_22 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"10:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_22.Wrap( 0 )
		bSizer4.Add( self.label_22, 0, wx.EXPAND, 0 )
		
		self.label_23 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"09:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_23.Wrap( 0 )
		bSizer4.Add( self.label_23, 0, wx.EXPAND, 0 )
		
		self.label_24 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"08:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_24.Wrap( 0 )
		bSizer4.Add( self.label_24, 0, wx.EXPAND, 0 )
		
		self.label_25 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"07:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_25.Wrap( 0 )
		bSizer4.Add( self.label_25, 0, wx.EXPAND, 0 )
		
		self.label_26 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"06:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_26.Wrap( 0 )
		bSizer4.Add( self.label_26, 0, wx.EXPAND, 0 )
		
		self.label_27 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"05:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_27.Wrap( 0 )
		bSizer4.Add( self.label_27, 0, wx.EXPAND, 0 )
		
		self.label_28 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"04:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_28.Wrap( 0 )
		bSizer4.Add( self.label_28, 0, wx.EXPAND, 0 )
		
		self.label_29 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"03:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_29.Wrap( 0 )
		bSizer4.Add( self.label_29, 0, wx.EXPAND, 0 )
		
		self.label_30 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"02:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_30.Wrap( 0 )
		bSizer4.Add( self.label_30, 0, wx.EXPAND, 0 )
		
		self.label_31 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"01:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_31.Wrap( 0 )
		bSizer4.Add( self.label_31, 0, wx.EXPAND, 0 )
		
		self.label_32 = wx.StaticText( self.wdTitle, wx.ID_ANY, u"00:", wx.DefaultPosition, wx.Size( -1, 16 ), 0 )
		self.label_32.Wrap( 0 )
		bSizer4.Add( self.label_32, 0, wx.EXPAND, 0 )
		
		
		self.wdTitle.SetSizer( bSizer4 )
		self.wdTitle.Layout()
		self.wdCanvas = wx.ScrolledWindow( self.window_1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 527, 526 ), wx.SIMPLE_BORDER|wx.HSCROLL|wx.VSCROLL )
		self.wdCanvas.SetScrollRate( 5, 5 )
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.pnlCanvas = wx.Panel( self.wdCanvas, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pnlCanvas.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer5.Add( self.pnlCanvas, 1, wx.EXPAND|wx.FIXED_MINSIZE, 0 )
		
		
		self.wdCanvas.SetSizer( bSizer5 )
		self.wdCanvas.Layout()
		self.window_1.SplitVertically( self.wdTitle, self.wdCanvas, 50 )
		bSizer3.Add( self.window_1, 1, wx.EXPAND, 0 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.pnlMeasure = wx.Panel( self.pnlmain, wx.ID_ANY, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblInfo1 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblInfo1.Wrap( 0 )
		self.lblInfo1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer7.Add( self.lblInfo1, 0, 0, 0 )
		
		self.lblInfo2 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblInfo2.Wrap( 0 )
		self.lblInfo2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer7.Add( self.lblInfo2, 0, 0, 0 )
		
		self.lblInfo3 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblInfo3.Wrap( 0 )
		self.lblInfo3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer7.Add( self.lblInfo3, 0, 0, 0 )
		
		self.lblInfo4 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblInfo4.Wrap( 0 )
		self.lblInfo4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer7.Add( self.lblInfo4, 0, 0, 0 )
		
		self.lblInfo5 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblInfo5.Wrap( 0 )
		self.lblInfo5.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer7.Add( self.lblInfo5, 0, 0, 0 )
		
		self.lblInfo6 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblInfo6.Wrap( 0 )
		self.lblInfo6.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer7.Add( self.lblInfo6, 0, 0, 0 )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.lblMeasure_T1 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"   T1   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblMeasure_T1.Wrap( -1 )
		self.lblMeasure_T1.SetFont( wx.Font( 10, 74, 90, 92, True, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.lblMeasure_T1, 0, wx.ALIGN_CENTER_HORIZONTAL, 1 )
		
		self.label_T1 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_T1.Wrap( 0 )
		self.label_T1.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_T1, 0, 0, 1 )
		
		self.lblMeasure_T2 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"   T2   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblMeasure_T2.Wrap( -1 )
		self.lblMeasure_T2.SetFont( wx.Font( 10, 74, 90, 92, True, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.lblMeasure_T2, 0, wx.ALIGN_CENTER_HORIZONTAL, 1 )
		
		self.label_T2 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_T2.Wrap( 0 )
		self.label_T2.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_T2, 0, 0, 1 )
		
		self.lblMeasure_T3 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"   T3   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblMeasure_T3.Wrap( -1 )
		self.lblMeasure_T3.SetFont( wx.Font( 10, 74, 90, 92, True, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.lblMeasure_T3, 0, wx.ALIGN_CENTER_HORIZONTAL, 1 )
		
		self.label_T3 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_T3.Wrap( 0 )
		self.label_T3.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_T3, 0, 0, 1 )
		
		self.lblMeasure_T4 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"   T4   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblMeasure_T4.Wrap( -1 )
		self.lblMeasure_T4.SetFont( wx.Font( 10, 74, 90, 92, True, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.lblMeasure_T4, 0, wx.ALIGN_CENTER_HORIZONTAL, 1 )
		
		self.label_T4 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_T4.Wrap( 0 )
		self.label_T4.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_T4, 0, 0, 1 )
		
		self.lblMeasure_T5 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"   T5   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblMeasure_T5.Wrap( -1 )
		self.lblMeasure_T5.SetFont( wx.Font( 10, 74, 90, 92, True, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.lblMeasure_T5, 0, wx.ALIGN_CENTER_HORIZONTAL, 1 )
		
		self.label_T5 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_T5.Wrap( 0 )
		self.label_T5.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_T5, 0, 0, 1 )
		
		self.lblMeasure_T6 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"   T6   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblMeasure_T6.Wrap( -1 )
		self.lblMeasure_T6.SetFont( wx.Font( 10, 74, 90, 92, True, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.lblMeasure_T6, 0, wx.ALIGN_CENTER_HORIZONTAL, 1 )
		
		self.label_T6 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_T6.Wrap( 0 )
		self.label_T6.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_T6, 0, 0, 1 )
		
		self.lblMeasure_T7 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"   T7   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblMeasure_T7.Wrap( -1 )
		self.lblMeasure_T7.SetFont( wx.Font( 10, 74, 90, 92, True, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.lblMeasure_T7, 0, wx.ALIGN_CENTER_HORIZONTAL, 1 )
		
		self.label_T7 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_T7.Wrap( 0 )
		self.label_T7.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_T7, 0, 0, 1 )
		
		self.lblMeasure_T8 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"   T8   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblMeasure_T8.Wrap( -1 )
		self.lblMeasure_T8.SetFont( wx.Font( 10, 74, 90, 92, True, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.lblMeasure_T8, 0, wx.ALIGN_CENTER_HORIZONTAL, 1 )
		
		self.label_T8 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_T8.Wrap( 0 )
		self.label_T8.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_T8, 0, 0, 1 )
		
		self.label_33 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"|T1-T2|=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_33.Wrap( 0 )
		self.label_33.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_33, 0, 0, 1 )
		
		self.label_sub12 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"sub12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_sub12.Wrap( 0 )
		self.label_sub12.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_sub12, 0, 0, 1 )
		
		self.label_34 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"|T2-T3|=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_34.Wrap( 0 )
		self.label_34.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_34, 0, 0, 1 )
		
		self.label_sub23 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"sub23", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_sub23.Wrap( 0 )
		self.label_sub23.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_sub23, 0, 0, 1 )
		
		self.label_35 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"|T3-T4|=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_35.Wrap( 0 )
		self.label_35.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_35, 0, 0, 1 )
		
		self.label_sub34 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"sub34", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_sub34.Wrap( 0 )
		self.label_sub34.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_sub34, 0, 0, 1 )
		
		self.label_36 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"|T4-T5|=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_36.Wrap( 0 )
		self.label_36.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_36, 0, 0, 1 )
		
		self.label_sub45 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"sub45", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_sub45.Wrap( 0 )
		self.label_sub45.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_sub45, 0, 0, 1 )
		
		self.label_37 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"|T5-T6|=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_37.Wrap( 0 )
		self.label_37.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_37, 0, 0, 1 )
		
		self.label_sub56 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"sub56", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_sub56.Wrap( 0 )
		self.label_sub56.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_sub56, 0, 0, 1 )
		
		self.label_38 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"|T6-T7|=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_38.Wrap( 0 )
		self.label_38.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_38, 0, 0, 1 )
		
		self.label_sub67 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"sub67", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_sub67.Wrap( 0 )
		self.label_sub67.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_sub67, 0, 0, 1 )
		
		self.label_39 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"|T7-T8|=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_39.Wrap( 0 )
		self.label_39.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_39, 0, 0, 1 )
		
		self.label_sub78 = wx.StaticText( self.pnlMeasure, wx.ID_ANY, u"sub78", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_sub78.Wrap( 0 )
		self.label_sub78.SetFont( wx.Font( 10, 74, 90, 90, False, "Segoe UI Symbol" ) )
		
		gSizer2.Add( self.label_sub78, 0, 0, 1 )
		
		
		bSizer7.Add( gSizer2, 1, 0, 1 )
		
		
		bSizer7.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.pnlMeasure.SetSizer( bSizer7 )
		self.pnlMeasure.Layout()
		bSizer6.Add( self.pnlMeasure, 1, wx.BOTTOM|wx.EXPAND, 1 )
		
		
		bSizer3.Add( bSizer6, 0, wx.EXPAND, 0 )
		
		
		self.pnlmain.SetSizer( bSizer3 )
		self.pnlmain.Layout()
		bSizer2.Add( self.pnlmain, 1, wx.EXPAND, 0 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	
	def window_1OnIdle( self, event ):
		self.window_1.SetSashPosition( 50 )
		self.window_1.Unbind( wx.EVT_IDLE )
	

