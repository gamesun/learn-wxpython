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

icon32 = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAABO5J"
    "REFUWIXll2tQVGUYx3/n7MVdZGHXBUQC5SKkKSiCpiUGOs6gE1IjongbHSunaRy1EdNuiqBS"
    "jbfKhW6upqQzjRnSNDVKaJpKzCijSxSQcnOgdNjl6u6yZ7cPJmFAAm5f6v/tvOd9nv9v/ufM"
    "eZ8D/3cJf1/YsmWL/89VVWOsVqtbjbRaLcHjx5dmrF9v6RVgzcY1gY11t/c4JEeKU5Lcat5l"
    "JghWtYf6oM7TK91gMLR1AaxevTr4VrPlYoC/v/+yxUuIioxEpVK51bytrY3ikh85nJdHR0dH"
    "qa9uWJzBYGgTABakLSoKDAyM374tk8tXLnO6sJD2jg63Aui0OpKTkvD19SV90yvYO+25Rz89"
    "8qLw0rp1sfV1tSVv78ympraG/Tk5bjXuLplMRubWDBoaG3jfYLBOeHL6CLHZ0jRVq9MRER7O"
    "ifz8f80cQJIkTn5VwJTYybhcLlW1yTRRrlarfRQKJQDNzc3/2EAQRZYsSmNybCymsjKMhw7i"
    "cDgGBNFkNqPRaACwWCyIAylOTkpi/tzpBPxmYO5TE5iTmDgg894k7+9Gb603qfNTcJS+ilT9"
    "JYJ2LBGjwx8aoN8JLFu8BFXHT0g1+SAIuFqqCAoKemiAfiUwOiyMWfHx2E8nI+gnISg1OM0m"
    "giYGolQqsdvtgwZ4cAKCwPOrVuGs/hyXpRxFbBaifhIuSzkyEUaNHDlo834BxM+YQUTICDqv"
    "voMsfAWidiyiPhocVlwtvxIaGvpQAPc9Ag8Pj/tu6nQ6li9disO0D0Q5isiX+f7cOeKmTgBB"
    "wGkuIzTkLwBBEHhi2jRmxicQGhKCUqnsYSjKZH0DfJST26NAqi2gs/IQiql7uVp+nY+NB5gR"
    "Z0TwCsNpNhEakgaARqNhU3o6j4UFIF0/hvPae+C406OfoBkFk9/qHcB2ah5Ym7quXdIdsJmR"
    "j1uDY/hsPty9kZaWFhoaG/HRR+MymwgePwpPT0+2vvEmIZ6/Y/t6JsjVyAITERRePQFUvn0n"
    "IH/0BZC6zQGiAtEnBrN9KLt3bKe+vh6AisoK/AKi6az7BpVCTnbWdgI8mrAXrUI2ch6KmAwq"
    "r9fQ1GTuAeApejKuL4BT5Qo6u31ZJUniRvVxLhUXY7PZutYrKiqJi5wGna242mp4xNuJrXAF"
    "shEzESdtI3vXXi4VX+phDhAREcHbO3b2DnD4szza29t7LeyuXyorEL1XgNwD6WYhUsUBRO04"
    "5I/v4t2c3D7Ne9OAzoJ7qq2rxYWI4B2OozQLVL4op3/AwbyjFJ05M6Be/T4Lustus3O59ArR"
    "MdtwNp5HHr6c4wXfkn/y5IB7DQoAYM++fSxcsIDhflO4kGvkzNmzg+ojt9kdt61WGy5c+Oj1"
    "/XoH4O6M94nROGDD4X5+WCx3B+Nhei+HqFLLTre0tnDtmomFqakIQo9J3W0aolLxbPIz/HDx"
    "AjK53BoTFVMqAKQuTSvQ6/RP78zMov7mTQqLvut3Ev2VTqdjbuIcADa//hpOpyv72JEjmwWA"
    "DRs2+N+orS3y1nqPSU1JISoyqs+xXABcDzC7l2H3fW2trRSXlHD8xBeIonB+dsKs2StXrrR2"
    "5b127Vptw61bmQ6p8znJIbn3p+BPyWSy22q1x/7RwcFZGRkZju6wXTIajarSsrIxnkOHaN1p"
    "3tx6p3F+UlJVQkLCwKbY/7z+AHJ0wHxvK0NnAAAAAElFTkSuQmCC")
geticon32Data = icon32.GetData
geticon32Image = icon32.GetImage
geticon32Bitmap = icon32.GetBitmap
geticon32Icon = icon32.GetIcon
