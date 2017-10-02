__author__ = 'sarvps'

'''
Author: Sarv Parteek Singh
Course: CS-600, Scientific Computation 1
HW: #8, Pr. 10.6, 'Numerical methods for Engineers', 7th edition
Brief: Inverse of a 3 by 3 matrix derived from a system of 3 linear equations
'''

import numpy as np
import _linalg3

A = np.array([
    [10, 2, -1],
    [-3, -6, 2],
    [1, 1, 5],
])
print("A = \n{}".format(np.array(A)))

#decompose A into L,U matrices (also get row order)
L, U, o = _linalg3.decompLU(A)
print("L = \n{}".format(L))
print("U = \n{}".format(U))
print("o = {} (row order)\n".format(o))

#----------------Solve for column1 of A inv. using L,U decomposition----------------
b1 = np.array([ 1, 0, 0])
print("\nb1 = {}\n".format(np.array(b1)))
d1 = _linalg3.subst(L, b1, dir="fwd")  #compute vector d using forward substitution: [L]{d} = {b}
print("(using L,U decomp)\nd1 = {}".format(d1))
x1 = _linalg3.subst(U, d1, dir="bwd")  #compute vector x using backward substitution: [U]{x} = {d}
print("col 1 of A inv = {}".format(x1))
x1_gauss = _linalg3.gauss(A, b1)
print("(Using gauss elimination)\ncol 2 of A inv = {}".format(x1_gauss))

#----------------Solve for column2 of A inv using L,U decomposition-----------------
b2 = np.array([ 0, 1, 0])
print("\nb2 = {}\n".format(np.array(b2)))
d2 = _linalg3.subst(L, b2, dir="fwd")  #compute vector d using forward substitution: [L]{d} = {b}
print("(using L,U decomp)\nd1 = {}".format(d1))
x2 = _linalg3.subst(U, d2, dir="bwd")  #compute vector x using backward substitution: [U]{x} = {d}
print("col 2 of A inv = {}".format(x2))
x2_gauss = _linalg3.gauss(A, b2)
print("(Using gauss elimination)\ncol 2 of A inv = {}".format(x2_gauss))

#----------------Solve for column3 of A inv using L,U decomposition-------------------
b3 = np.array([ 0, 0, 1])
print("\nb3 = {}\n".format(np.array(b3)))
d3 = _linalg3.subst(L, b3, dir="fwd")  #compute vector d using forward substitution: [L]{d} = {b}
print("(using L,U decomp)\nd3 = {}".format(d3))
x3 = _linalg3.subst(U, d3, dir="bwd")  #compute vector x using backward substitution: [U]{x} = {d}
print("col 3 of A inv = {}".format(x3))
x3_gauss = _linalg3.gauss(A, b3)
print("(Using gauss elimination)\ncol 2 of A inv = {}".format(x3_gauss))

#-------------------Merge all vectors to form the inverse matrix-----------------------
A_inv = np.array([x1,x2,x3])
A_inv = A_inv.transpose() # x1, x2 and x3 are column vectors but were registered in A_inv as row vectors.
print("A inv = \n{}".format(np.array(A_inv)))

#Check the results by doing a matrix multiplication of A and A inverse. The result should be an identity matrix.
prod = np.matmul(A,A_inv)
print("Product = \n{}".format(np.array(prod)))

