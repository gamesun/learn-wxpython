# -*- coding:utf-8 -*-

# import regex module
import re

"""

"""

g_match = re.compile('(?P<time>[0-9a-fA-F]{4}) (?P<value>[0-9a-fA-F]{8})')

def Parser(lines):
    """
    parser the data and display results at the canvas.
    Parser(list) -> [ duration,    info
                      [((x1,y1), (x2,y2), ... (xn,yn)),    wave 1
                      (...),    wave 2
                      ...  ]]
    """

    RawData = [g_match.search(l) for l in lines]                                    # get the origin data
    list = [(r.group('time'), r.group('value')) for r in RawData if r is not None]  # filter the null data
    list.sort()
    
    if 0 < len(list):
        matrix = [[(int(l[0], 16), int(v)) for v in bits(int(l[1], 16), 32)] for l in list]
        return (int(list[-1][0], 16) - int(list[0][0], 16), zip(*matrix))
    return

def bits(data):
    while data:
        yield data & 1
        data >>= 1

def bits(data, bits):
    for i in xrange(bits):
        yield data & 1
        data >>= 1
    
def Scale(factor):
    """
    scale the canvas using the factor.
    """
    
    #by resize the boxsizer?
    pass
