#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2014, gamesun
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


__version__ = '1.0.2'
__date__ = '2014-1-30'
__author__ = 'gamesun'
__credits__ = ['Metallicow']
__url__ = 'https://github.com/gamesun/PopupColorSelector'



import wx


COLOR_PAD_ROW_NUM = 0
COLOR_PAD_COL_NUM = 5

ColorTable = (
    (wx.Colour(255, 255, 0),    u"Yellow"   ),      # 0
    (wx.Colour(0, 255, 0),      u"Lime"     ),      # 1
    (wx.Colour(0, 255, 255),    u"Aqua"     ),      # 2
    (wx.Colour(255, 0, 255),    u"Fuchsia"  ),      # 3
    (wx.Colour(0, 0, 255),      u"Blue"     ),      # 4
    (wx.Colour(255, 0, 0),      u"Red"      ),      # 5
    (wx.Colour(0, 0, 128),      u"Navy"     ),      # 6
    (wx.Colour(0, 128, 128),    u"Teal"     ),      # 7
    (wx.Colour(0, 128, 0),      u"Green"    ),      # 8
    (wx.Colour(128, 0, 128),    u"Purple"   ),      # 9
    (wx.Colour(128, 0, 0),      u"Maroon"   ),      # 10
    (wx.Colour(128, 128, 0),    u"Olive"    ),      # 11
    (wx.Colour(128, 128, 128),  u"Gray"     ),      # 12
    (wx.Colour(192, 192, 192),  u"Silver"   ),      # 13
    (wx.Colour(0, 0, 0),        u"Black"    ),      # 14
)


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
    def __init__(self, parent):
        wx.PopupTransientWindow.__init__(self, parent, wx.NO_BORDER)
        self.parent = parent

        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        gSizer1 = wx.GridSizer(COLOR_PAD_ROW_NUM, COLOR_PAD_COL_NUM, 0, 0)

        for i in range(15):
            exec("self.m_staticText%d = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(24, 24), 0)" % i)
            exec("self.m_staticText%d.Wrap(-1)" % i)
            exec("self.m_staticText%d.SetBackgroundColour(ColorTable[%d][0])" % (i, i))
            exec("self.m_staticText%d.SetToolTipString(ColorTable[%d][1])" % (i, i))
            exec("gSizer1.Add(self.m_staticText%d, 0, wx.ALL, 3)" % i)

        bSizer1.Add(gSizer1, 0, wx.ALL, 2)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)
        self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.LI_HORIZONTAL)
        bSizer2.Add(self.m_staticline1, 0, wx.EXPAND |wx.ALL, 0)
        bSizer1.Add(bSizer2, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 3)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)
        self.m_btnCustom = wx.Button(self, wx.ID_ANY, u"Custom", wx.DefaultPosition, wx.Size(-1, 25), 0)
        self.m_btnCustom.SetToolTipString(u"Create custom color")
        bSizer3.Add(self.m_btnCustom, 0, wx.ALL|wx.EXPAND, 2)
        bSizer1.Add(bSizer3, 1, wx.EXPAND, 5)
        self.SetSizer(bSizer1)
        bSizer1.Fit(self)

        self.m_btnCustom.Bind(wx.EVT_BUTTON, self.OnBtnCustom)
        self.Bind(wx.EVT_PAINT, self.OnPaint_Window)

        for i in range(15):
            eval("self.m_staticText%d.Bind(wx.EVT_PAINT, lambda evt, self = self: self.OnPaint_StaticText(evt, %d))" % (i, i))
            eval("self.m_staticText%d.Bind(wx.EVT_LEFT_UP, lambda evt, self = self: self.OnLeftUp_StaticText(evt, %d))" % (i, i))
            eval("self.m_staticText%d.Bind(wx.EVT_ENTER_WINDOW, lambda evt, self = self: self.OnEnterWindow(evt, %d))" % (i, i))
            eval("self.m_staticText%d.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindow)" % i)

        self.focus = None

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
            dc.SetBrush(wx.Brush(ColorTable[idx][0], wx.SOLID))
        else:
            dc.SetPen(wx.TRANSPARENT_PEN)
            dc.SetBrush(wx.Brush(ColorTable[idx][0], wx.SOLID))
        
        rect = eval("self.m_staticText%d.GetClientRect()" % idx)
        dc.DrawRectangle(*rect)
        
        evt.Skip()

    def OnPaint_Window(self, evt = None):
        dc = wx.BufferedPaintDC(self)
        dc.Clear()

        # Draw the border of PopupWindow
        dc.SetPen(wx.Pen(wx.Colour(134, 134, 134)))
        dc.SetBrush(wx.TRANSPARENT_BRUSH)
        rect = self.GetClientRect()
        dc.DrawRectangle(*rect)

        for i in range(15):
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
