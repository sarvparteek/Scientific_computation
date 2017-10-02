__author__ = 'sarvps'

'''
Author: Sarv Parteek Singh
Course: CS-600, Scientific Computation 1
HW: #8, Pr. 11.13, 'Numerical methods for Engineers', 7th edition
Brief: Solution of a system of 3 linear equations using Gauss-Seidel method
'''

import numpy as np
import _linalg, _linalg4
import pylab as pl

A = np.array([
    [-6, -1, 2],
    [-1, 7, -3],
    [1, -2, -8],
])
b = np.array([
    -38,
    -34,
    -20,
])

print("A = \n{}".format(np.array(A)))
print("b = {}\n".format(np.array(b)))

x= _linalg4.gausseidel(A, b, imax=1000, es100=0.01, lamb=1.0)
print("(using gauss-seidel with lambda = 1.0)\nx = {}".format(x))

x = _linalg4.gausseidel(A, b, imax=1000, es100=0.01, lamb=1.5)
print("(using gauss-seidel with lambda = 1.2)\nx = {}".format(x))

x = _linalg.gauss(A, b)
print("(using gauss-elim)\nx = {}".format(x))

