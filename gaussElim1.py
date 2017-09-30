__author__ = 'sarvps'

'''
Author: Sarv Parteek Singh
Course: CS-600, Scientific Computation 1
HW: #7, Pr. 9.11, 'Numerical methods for Engineers', 7th edition
Brief: Solution for a system of 3 linear equations
'''

import numpy as np
import _linalg

A = np.array( [[2, -6, -1],
               [-3, -1, 7],
               [-8, 1, -2]] )
b = np.array( [-38, -34, -20] )

print("A =\n{}".format(A))
print("b = {}".format(b))

print("solving...")
x = _linalg.gauss(A, b)  #solve using Gauss elimination method w/ scaling & partial pivoting
x_check = np.linalg.solve(A, b)  #solve using numpy (to test correctness)
print("x = {}\n".format(x))
print("x_check = {}\n".format(x_check))

#Check by re-substitution
sum = [0] * len(A)
for i in range(len(A)):
    for j in range(len(x)):
        sum[i] += A[i][j] * x[j]
    sum[i] -= b[i]

print("The sum of three equations are {}".format(sum))
