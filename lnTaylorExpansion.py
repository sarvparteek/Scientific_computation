__author__ = 'sarvps'

'''
Author: Sarv Parteek Singh
Course: CS-600, Scientific Computation 1
HW: #4, Pr 4.6, 'Numerical methods for Engineers', 7th edition
Brief: Estimation of ln(2.5) using Taylor's expansion about 1
'''

import _series
import math
import pylab as pl

print("Taylor expansion of ln(x) for x = 2.5 about x = 1")

def f(x): return math.log(x)

def dfdx(i, x):
    return {
        0: f(x),
        1: 1/x,
        2: -1/x**2,
        3: 2/x**3,
        4: -6/x**4
    }.get(i,0)

xi = 1.0
xiplus1 = 2.5
tv = f(xiplus1)
h = xiplus1 - xi

avList = []
orders = 4
for i in range(orders+1):
    av = _series.taylor( dfdx, i, xi, h)
    avList += [av]
    et = abs(1-av/tv)
    print("i = {}| av = {}| tv = {}| et = {:%}".format(i,av,tv,et))

#Plot results
tvList = [f(xiplus1)] * (orders+1) #For comparison with estimation using Maclaurin series'
testRange = list(range(orders+1))
pl.figure(1)
pl.plot(testRange,tvList,'r',label = 'Math library-computed value')
pl.plot(testRange,avList,'b',label = 'Taylor estimated value')
pl.legend(loc = 'best')
pl.xlabel('Iterations')
pl.ylabel('Computed value')
pl.title('Comparison of ln(x) computed by math lib vs Taylor estimation')
pl.grid(True)
pl.show()