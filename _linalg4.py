#_linalg4.py

import numpy as np

def gausseidel(A, b, imax=1000, es100=0.1, lamb=1.):
    n = len(A)
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x = np.zeros(n)
    for i in range(n):
        pivot = A[i,i]
        A[i,:] /= pivot
        b[i] /= pivot
    for i in range(n):
        sum = b[i]
        for j in range(n):
            if i != j: sum -= A[i,j]*x[j]
        x[i] = sum
    iter = 1
    while True:
        sentinel = 1
        for i in range(n):
            old = x[i]
            sum = b[i]
            for j in range(n):
                if i != j: sum -= A[i,j]*x[j]
            x[i] = lamb*sum + (1 - lamb)*old
            if sentinel and x[i]:
                ea = abs(1 - old/x[i])
                if ea*100 > es100: sentinel = 0
        iter += 1
        if sentinel or iter >= imax:
            break
    print("iterations=",iter)
    return x
#end gausseidel()
