__author__ = 'sarvps'

'''
    Author: Sarv Parteek Singh
    Course: CS 600
    HW: #3, Pr 3.6, 'Numerical methods for engineers, 7th edition'
    Brief: Computation of an exponential term using different numerical methods
'''

import math
import numpy as np
import pylab as pl
import _error

def inverseExpSum(x,tv,iter):
    print("\n######### Inverse summation for e^{} ##############".format(-1*x))
    etList = []
    eaList = []
    avList = []
    termList = []
    sum = 0.0
    pv = 0.0
    for i in range(iter):
        sum += x**i/math.factorial(i)
        av = 1/sum
        et = _error.et(tv,av)
        ea = _error.ea(av,pv)
        print("iter ={}| tv={:.8f}| av={:.8f}| et={:.8%}| ea={:.8%}".format(i,tv,av,et,ea))
        etList += [et]
        eaList += [ea]
        avList += [av]
        termList += [av-pv]
        pv = av # for next iteration
    return etList,eaList,avList,termList

def directExpSum(x,tv,iter):
    print("\n######### Direct summation for e^{} ##############".format(-1*x))
    etList = []
    eaList = []
    avList = []
    termList = []
    sum = 0.0
    pv = 0.0
    for i in range(iter):
        sum += (-1)**i * x**i/math.factorial(i)
        av = sum
        et = _error.et(tv,av)
        ea = _error.ea(av,pv)
        print("iter ={}| tv={:.8f}| av={:.8f}| et={:.8%}| ea={:.8%}".format(i,tv,av,et,ea))
        etList += [et]
        eaList += [ea]
        avList += [av]
        termList += [av-pv]
        pv = av # for next iteration
    return etList,eaList,avList,termList

tv = 6.737947* 10**-3
iter = 20
etInv, eaInv, avInv, termInv = inverseExpSum(5,tv,iter)
etDir, eaDir, avDir, termDir = directExpSum(5,tv,iter)

# Plot true errors for each
iterations = list(range(iter))
pl.figure(1)
pl.plot(iterations, etInv, 'r', label = 'InverseExpSum')
pl.plot(iterations, etDir, 'b', label = 'DirectExpSum')
pl.legend(loc = 'upper right')
pl.xlabel('Iterations')
pl.ylabel('True relative error(%)')
pl.title('True relative error for direct & inverse exp sum computation')
pl.grid(True)

#Plot relative errors for each
pl.figure(2)
pl.plot(iterations, eaInv, 'r', label = 'InverseExpSum')
pl.plot(iterations, eaDir, 'b', label = 'DirectExpSum')
pl.legend(loc = 'upper right')
pl.xlabel('Iterations')
pl.ylabel('Approx relative error(%)')
pl.title('Approx relative error for direct & inverse exp sum computation')
pl.grid(True)

#Plot iterative results for each
tvList = [tv] * len(iterations)
pl.figure(3)
pl.plot(iterations,tvList,'m',label = 'True value')
pl.plot(iterations,avInv, 'r', label = 'InverseExpSum')
pl.plot(iterations,avDir, 'b', label = 'DirectExpSum')
pl.legend(loc = 'upper right')
pl.xlabel('Iterations')
pl.ylabel('Computed value of exp')
pl.title('Progression of computed values by Direct & Inverse exp sum')
pl.grid(True)

#Plot value of term per iteration for each
pl.figure(4)
pl.plot(iterations,termInv,'r',label='InverseExpSum')
pl.plot(iterations,termDir,'b',label='DirectExpSum')
pl.legend(loc = 'upper right')
pl.xlabel('Iterations')
pl.ylabel('Computed value on current iteration')
pl.title('Comparison of value computed per term')
pl.grid(True)
pl.show()