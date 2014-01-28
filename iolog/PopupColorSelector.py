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

import wx


ColorTable = [
    [wx.Colour(255, 255, 0),    u"Yellow"   ],      # 1
    [wx.Colour(0, 255, 0),      u"Lime"     ],      # 2
    [wx.Colour(0, 255, 255),    u"Aqua"     ],      # 3
    [wx.Colour(255, 0, 255),    u"Fuchsia"  ],      # 4
    [wx.Colour(0, 0, 255),      u"Blue"     ],      # 5
    [wx.Colour(255, 0, 0),      u"Red"      ],      # 6
    [wx.Colour(0, 0, 128),      u"Navy"     ],      # 7
    [wx.Colour(0, 128, 128),    u"Teal"     ],      # 8
    [wx.Colour(0, 128, 0),      u"Green"    ],      # 9
    [wx.Colour(128, 0, 128),    u"Purple"   ],      # 10
    [wx.Colour(128, 0, 0),      u"Maroon"   ],      # 11
    [wx.Colour(128, 128, 0),    u"Olive"    ],      # 12
    [wx.Colour(128, 128, 128),  u"Gray"     ],      # 13
    [wx.Colour(192, 192, 192),  u"Silver"   ],      # 14
    [wx.Colour(0, 0, 0),        u"Black"    ],      # 15
]


COLOR_SELECT = wx.NewEventType()
EVT_COLOR_SELECT = wx.PyEventBinder(COLOR_SELECT, 0)


class ColorSelectEvent(wx.PyCommandEvent):
    eventType = COLOR_SELECT
    def __init__(self, windowID, color):
        wx.PyCommandEvent.__init__(self, self.eventType ,windowID)
        self.color = color

    def Clone(self):
        self.__class__(self.GetId(), self.color)


class PopupColorSelector(wx.PopupTransientWindow):
    """Adds a bit of text and mouse movement to the wx.PopupWindow"""
    def __init__(self, parent, style):
        wx.PopupTransientWindow.__init__(self, parent, style)

        self.parent = parent

        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        gSizer1 = wx.GridSizer( 0, 5, 0, 0 )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText1.Wrap( -1 )
        self.m_staticText1.SetBackgroundColour( ColorTable[0][0] )
        self.m_staticText1.SetToolTipString( ColorTable[0][1] )

        gSizer1.Add( self.m_staticText1, 0, wx.ALL, 3 )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText2.Wrap( -1 )
        self.m_staticText2.SetBackgroundColour( ColorTable[1][0] )
        self.m_staticText2.SetToolTipString( ColorTable[1][1] )

        gSizer1.Add( self.m_staticText2, 0, wx.ALL, 3 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText3.Wrap( -1 )
        self.m_staticText3.SetBackgroundColour( ColorTable[2][0] )
        self.m_staticText3.SetToolTipString( ColorTable[2][1] )

        gSizer1.Add( self.m_staticText3, 0, wx.ALL, 3 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText4.Wrap( -1 )
        self.m_staticText4.SetBackgroundColour( ColorTable[3][0] )
        self.m_staticText4.SetToolTipString( ColorTable[3][1] )

        gSizer1.Add( self.m_staticText4, 0, wx.ALL, 3 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText5.Wrap( -1 )
        self.m_staticText5.SetBackgroundColour( ColorTable[4][0] )
        self.m_staticText5.SetToolTipString( ColorTable[4][1] )

        gSizer1.Add( self.m_staticText5, 0, wx.ALL, 3 )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText6.Wrap( -1 )
        self.m_staticText6.SetBackgroundColour( ColorTable[5][0] )
        self.m_staticText6.SetToolTipString( ColorTable[5][1] )

        gSizer1.Add( self.m_staticText6, 0, wx.ALL, 3 )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText7.Wrap( -1 )
        self.m_staticText7.SetBackgroundColour( ColorTable[6][0] )
        self.m_staticText7.SetToolTipString( ColorTable[6][1] )

        gSizer1.Add( self.m_staticText7, 0, wx.ALL, 3 )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText8.Wrap( -1 )
        self.m_staticText8.SetBackgroundColour( ColorTable[7][0] )
        self.m_staticText8.SetToolTipString( ColorTable[7][1] )

        gSizer1.Add( self.m_staticText8, 0, wx.ALL, 3 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText9.Wrap( -1 )
        self.m_staticText9.SetBackgroundColour( ColorTable[8][0] )
        self.m_staticText9.SetToolTipString( ColorTable[8][1] )

        gSizer1.Add( self.m_staticText9, 0, wx.ALL, 3 )

        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText10.Wrap( -1 )
        self.m_staticText10.SetBackgroundColour( ColorTable[9][0] )
        self.m_staticText10.SetToolTipString( ColorTable[9][1] )

        gSizer1.Add( self.m_staticText10, 0, wx.ALL, 3 )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText11.Wrap( -1 )
        self.m_staticText11.SetBackgroundColour( ColorTable[10][0] )
        self.m_staticText11.SetToolTipString( ColorTable[10][1] )

        gSizer1.Add( self.m_staticText11, 0, wx.ALL, 3 )

        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText12.Wrap( -1 )
        self.m_staticText12.SetBackgroundColour( ColorTable[11][0] )
        self.m_staticText12.SetToolTipString( ColorTable[11][1] )

        gSizer1.Add( self.m_staticText12, 0, wx.ALL, 3 )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText13.Wrap( -1 )
        self.m_staticText13.SetBackgroundColour( ColorTable[12][0] )
        self.m_staticText13.SetToolTipString(  ColorTable[12][1] )

        gSizer1.Add( self.m_staticText13, 0, wx.ALL, 3 )

        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText14.Wrap( -1 )
        self.m_staticText14.SetBackgroundColour( ColorTable[13][0] )
        self.m_staticText14.SetToolTipString( ColorTable[13][1] )

        gSizer1.Add( self.m_staticText14, 0, wx.ALL, 3 )

        self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 24,24 ), 0 )
        self.m_staticText15.Wrap( -1 )
        self.m_staticText15.SetBackgroundColour( ColorTable[14][0] )
        self.m_staticText15.SetToolTipString( ColorTable[14][1] )

        gSizer1.Add( self.m_staticText15, 0, wx.ALL, 3 )


        bSizer1.Add( gSizer1, 0, wx.ALL, 2 )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LI_HORIZONTAL )
        bSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 0 )


        bSizer1.Add( bSizer2, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 3 )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_btnCustom = wx.Button( self, wx.ID_ANY, u"Custom", wx.DefaultPosition, wx.Size( -1,25 ), 0 )
        self.m_btnCustom.SetToolTipString( u"Create custom color" )
        bSizer3.Add( self.m_btnCustom, 0, wx.ALL|wx.EXPAND, 2 )


        bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

        self.SetSizer( bSizer1 )

        bSizer1.Fit(self)

        self.focus = None

        self.m_btnCustom.Bind(wx.EVT_BUTTON, self.OnBtnCustom)

        self.Bind(wx.EVT_PAINT, self.OnPaint_Window)

        for i in range(1, 16):
            eval("self.m_staticText%d.Bind(wx.EVT_PAINT, lambda evt, self = self: self.OnPaint_StaticText(evt, %d))" % (i, i))
            eval("self.m_staticText%d.Bind(wx.EVT_LEFT_UP, lambda evt, self = self: self.OnLeftUp_StaticText(evt, %d))" % (i, i))
            eval("self.m_staticText%d.Bind(wx.EVT_ENTER_WINDOW, lambda evt, self = self: self.OnEnterWindow(evt, %d))" % (i, i))
            eval("self.m_staticText%d.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)" % i)

        self.Layout()

    def OnLeftUp_StaticText(self, evt, idx):
        self.color = eval("self.m_staticText%d.GetBackgroundColour()" % idx)

        # sent event
        evt = ColorSelectEvent(self.parent.GetId(), self.color)
        self.parent.GetEventHandler().AddPendingEvent(evt)

        self.Hide()
        self.Destroy()

    def OnPaint_StaticText(self, evt, idx):
        dc = eval("wx.BufferedPaintDC(self.m_staticText%d)" % idx)
        dc.Clear()

        if self.focus is idx:
            # Draw the inner border of focused color
            dc.SetPen(wx.Pen(wx.Colour(255, 226, 148)))
            dc.SetBrush(wx.Brush(wx.Colour(255, 255, 255), wx.BRUSHSTYLE_TRANSPARENT))
            rect = eval("self.m_staticText%d.GetClientRect()" % idx)
            dc.DrawRectangle(*rect)

        evt.Skip()

    def OnPaint_Window(self, evt = None):
        dc = wx.BufferedPaintDC(self)
        dc.Clear()

        # Draw the border of PopupWindow
        dc.SetPen(wx.Pen(wx.Colour(134, 134, 134)))
        dc.SetBrush(wx.Brush(wx.Colour(255, 255, 255), wx.BRUSHSTYLE_TRANSPARENT))
        rect = self.GetClientRect()
        dc.DrawRectangle(*rect)

        for i in range(1, 16):
            if self.focus is i:
                dc.SetPen(wx.Pen(wx.Colour(242, 148, 54)))      # Draw the border of focused color
            else:
                dc.SetPen(wx.Pen(wx.Colour(197, 197, 197)))     # Draw the border of not focused ones

            rect = eval("self.m_staticText%d.GetRect()" % i)
            rect.Inflate(1, 1)
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
        #data.SetCustomColour(0, (255, 170, 128))

        # set the default color in the chooser
        #data.SetColour(wx.Colour(128, 255, 170))

        # construct the chooser
        dlg = wx.ColourDialog(self.parent, data)

        if dlg.ShowModal() == wx.ID_OK:
            self.color = dlg.GetColourData().Colour

            # sent event
            evt = ColorSelectEvent(self.parent.GetId(), self.color)
            self.parent.GetEventHandler().AddPendingEvent(evt)

        dlg.Destroy()

        self.Hide()
        self.Destroy()
