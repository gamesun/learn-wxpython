# -*- coding:utf-8 -*-

# import regex module
import re

"""

"""

g_match = re.compile('[0-9a-fA-F]{4} [0-9a-fA-F]{8}')

def Parser(list):
    """
    parser the data and display results at the canvas.
    """
    
#    for l in list:
#        print l,
    
    tmp = [g_match.search(l) for l in list ]
    tmp = [t for t in tmp if t is not None]

    for t in tmp:
        print t.group()



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
