#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2013-2014, gamesun
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

from wx.lib.embeddedimage import PyEmbeddedImage

icon16 = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAo1J"
    "REFUWIXt1s1rlFcUx/HPPJOZSTImhhIlIGhqsjAGU0mMRvEFN7oRkbZqNYiilLaC9GXVTV/+"
    "AUWKiyIuhIm6EBS3EjEWihW6UImohGihpBB8m6jRxJlkXDyJONKEaCM+UM/m3nM55/7O/T73"
    "Pvfyf7fYeGdLe3sz5PPP9oRtvnw6hUriiYeQTqV+hUwmcx2C6RR5E4ttaW9vg9aW5guwtLU1"
    "CcPDw9MqVFpaBroudD2Gnhs3lxIBAiVBPPgaljS3JOHAwYNvRSgWC7fbd998OwMuX7n6JVEg"
    "UFVZUQP37t+fNLC6uhr8uG8zuNjdD06cPDUloUKhAIaGnoL8SK6SKBCYauCubR+D2T3fg9UL"
    "fwAn/mMB0SfQ2NgIls38Mxyo+gTMSt4F5ek0eDI4+EYFRIdAPB7WkkgmwrYkbPd8uiYMGOoE"
    "g3M/B+m/DoH5tbWg+9o10LRoEaibXwdiwYvrBtTOqy3yo0Ng46qw4g0L1oUDhVEw2n8MXE1s"
    "AzfOXwKb5zwC9fWLwfq1y0Fbxe9hfv7y2MzFBOKVdUV+dAg8GEqBO9kPQGGs8lsPN4LjJzOg"
    "vm7s235YAT7bFBILrvwE+lJbwZmL4Z7I5XJFguvTFUV+dAh0/dENMsc6Jk3o6e0FsarwdMQu"
    "7QV353wFft4f7plsNvuv+R81NRX50SEwVRv/453tqQLzar4Avxw6jYlXPpG9ewLZgYE+mDV2"
    "3784toXJEw8fPf5aQkEQrrWsLHwbJkqSWSJAILZ9584WaGxo+A1WrlhRDsPPpvdVnEqVgs5z"
    "nQNw++/eJUSBwHhn644dDTCSz+2GIIhXvxw4XunoKxO8Oj5R3OhI7h8onZE8Ah1HOm6/HP/e"
    "3pk9B32koxlI8fdWAAAAAElFTkSuQmCC")
geticon16Data = icon16.GetData
geticon16Image = icon16.GetImage
geticon16Bitmap = icon16.GetBitmap
geticon16Icon = icon16.GetIcon

