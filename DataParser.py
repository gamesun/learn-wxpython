# -*- coding:utf-8 -*-

# import regex module
import re

"""

"""

g_match = re.compile('(?P<time>[0-9a-fA-F]{4}) (?P<value>[0-9a-fA-F]{8})')

def Parser(pnl, canvas, list):
    """
    parser the data and display results at the canvas.
    """
    
#    for l in list:
#        print l,
    
    tmp = [g_match.search(l) for l in list ]
    lstData = [t for t in tmp if t is not None]

    for d in lstData:
        print d.group('time') , d.group('value')
    
    if 0 < len(lstData): 
        duration = int(lstData[-1].group('time'),16) - int(lstData[0].group('time'),16)
        print duration
        w,h = pnl.GetSize()
        pnl.SetSize((duration,h))
        canvas.Line()

def DrawLine(data):
    """
    
    """
    pass


def Scale(factor):
    """
    scale the canvas using the factor.
    """
    
    #by resize the boxsizer?
    pass
