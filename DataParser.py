# -*- coding:utf-8 -*-

# import regex module
import re

"""

"""

g_match = re.compile('(?P<time>[0-9a-fA-F]{4}) (?P<value>[0-9a-fA-F]{8})')

def Parser(list):
    """
    parser the data and display results at the canvas.
    Parser(list) -> [ (duration),    info
                      ((x1,y1), (x2,y2), ... (xn,yn)),    wave 1
                      (...),    wave 2
                      ...
                      (...))]    wave 32
    """
    
#    for l in list:
#        print l,
    result = []
    
    tmp = [g_match.search(l) for l in list ]
    lstData = [t for t in tmp if t is not None]
    
    if 0 < len(lstData): 
        duration = int(lstData[-1].group('time'), 16) - int(lstData[0].group('time'), 16)
        result = [[duration]]
#         print result
        matrix = []
        for d in lstData:
#             print d.group('time') , #d.group('value'),
            matrix.append([(int(d.group('time'), base = 16), int(v)) for v in bits(int(d.group('value'), base = 16), 32)])
                
        result.append(zip(*matrix))
            
    return result

def bits(data):
    while data:
        b = data & 0x01
        yield b
        data >>= 1

def bits(data, bits):
    for i in xrange(bits):
        b = data & 0x01
        yield b
        data >>= 1
    
def Scale(factor):
    """
    scale the canvas using the factor.
    """
    
    #by resize the boxsizer?
    pass
