
'''
module: _series.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapter on truncation errors & the taylor series
- implemented from algorithms/pseudocode provided
'''

import math

def taylor(dfdx, n, xi, h, start=0):
    "computes the nth order taylor series of f(xi+h)"
    #n: order
    #xi: reference point
    #h: step-size (h = xi+1 - xi)
    #dfdx(i,xi): ith derivative of f(xi) for i=0,1,..,n"  [dfdx(0,xi) is f(xi)]
    sum = .0
    for i in range(start, n+1):  #loop from i=start to n
        sum += dfdx(i, xi) * h**i / math.factorial(i)
    return sum
#end taylor()

def R(dfdx, n, xi, h):
    "computes the nth order remainder of the taylor series of f(xi+h)"
    #n: order
    #xi: reference point
    #h: step-size (h = xi+1 - xi)
    #dfdx(i,xi): ith derivative of f(xi) for i=0,1,..,n"  [dfdx(0,xi) is f(xi)]
    return taylor(dfdx, 20, xi, h, n+1)
#end R()
