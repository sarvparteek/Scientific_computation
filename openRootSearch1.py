__author__ = 'sarvps'

'''
Author: Sarv Parteek Singh
Course: CS-600, Scientific Computation 1
HW: #5, Pr 6.9, 'Numerical methods for Engineers', 7th edition
Brief: Root finding for a polynomial of degree 3 using open methods
'''

import math
import _plot, _roots2

def f(x):
    return x**3 - 6*(x**2) + 11*x - 6.1

def df(x):
    return 3*(x**2) - 12*x + 11

#part(a): Two plots are generated: the first gives a holistic view and the second one a zoomed-in view
_plot.graph(f, xl = -10.0, xu = 10.0, xlabel = 'x', ylabel = 'f(x)', title = 'Plot over wide range of x')
_plot.graph(f, xl = 0.0, xu = 4.0, xlabel = 'x', ylabel = 'f(x)', title = 'Plot over a small range of interest of x')

#Note: In the following segment, the tv that is used is obtained using graphical representation in part(a)
#part(b)
print("\nNewton-Raphson method:")
_roots2.newton(f, df, x0 = 3.5, imax = 5, tv = 3.046676, debug = True)

#part(c)
print("\nSecant method:")
_roots2.secant(f, x0 = 3.5, x1 = 2.5, imax = 5, tv = 3.046676, debug = True)

#part(d)
print("\nModified secant method:")
_roots2.modified_secant2(f, x0 = 3.5, delta = 0.1, imax =5, tv = 3.046676, debug = True)