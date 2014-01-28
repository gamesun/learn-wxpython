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

        # sent event
        evt = ColorSelectEvent(self.parent.GetId(), self.color)
        self.parent.GetEventHandler().AddPendingEvent(evt)

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
        dlg = wx.ColourDialog(self.parent, data)

        if dlg.ShowModal() == wx.ID_OK:
            # set the panel background color
            self.color = dlg.GetColourData().Colour

            # sent event
            evt = ColorSelectEvent(self.parent.GetId(), self.color)
            self.parent.GetEventHandler().AddPendingEvent(evt)

        dlg.Destroy()

        self.Destroy()
