__author__ = 'sarvps'

'''
Author: Sarv Parteek Singh
Course: CS-600, Scientific Computation 1
HW: #3, Pr 3.10, 'Numerical methods for Engineers', 7th edition
Brief: Estimation of cosine using Maclaurin series expansion
'''

import math
import numpy as np
import pylab as pl
import _error

def cosEstimate(x,sigDigits):
    sum = 0.0
    iter = 0
    iterMax = 1000 #max number of iterations
    tv = math.cos(x)
    pv = 0.0
    es100 = _error.es100(sigDigits) # error tolerance
    res = [] #Result
    while True:
        sum += (-1)**iter * x**(2*iter)/math.factorial(2*iter)
        cv = sum #current value
        ea100 = _error.ea100(cv,pv)  #approximate relative error %
        print("iter = {}| av = {:.12f}| tv = {:.12f}| es = {:.12f}%| ea = {:.12f}%".format(iter,cv,tv,es100,ea100))
        res += [cv]
        if math.fabs(ea100) < es100 or iter > iterMax:
            break
        iter += 1
        pv = cv
    return res,iter

num = 0.3 * math.pi
avList,iter = cosEstimate(num,8)

#Plot results
tvList = [math.cos(num)] * (iter+1) #For comparison with estimation using Maclaurin series'
testRange = list(range(iter+1))
pl.figure(1)
pl.plot(testRange,tvList,'r',label = 'Math library-computed value')
pl.plot(testRange,avList,'b',label = 'Maclaurin estimated value')
pl.legend(loc = 'best')
pl.xlabel('Iterations')
pl.ylabel('Computed value')
pl.title('Comparison of cos(x) computed by math lib vs Maclaurin estimation')
pl.grid(True)
pl.show()