__author__ = 'sarvps'

'''
Author: Sarv Parteek Singh
Course: CS-600, Scientific Computation 1
HW: #5, Pr 6.10, 'Numerical methods for Engineers', 7th edition
Brief: Root finding for a nonlinear function using open methods
'''

import math
import _plot, _roots2

def f(x):
    return 7*math.sin(x)*math.exp(-x) - 1

def df(x):
    return 7*math.exp(-x) * (math.cos(x) - math.sin(x))

#part(a): Two plots are generated: the first gives a holistic view and the second one a zoomed-in view
_plot.graph(f, xl = -10.0, xu = 10.0, xlabel = 'x', ylabel = 'f(x)', title = 'Plot over wide range of x', show = False)
_plot.graph(f, xl = 0.0, xu = 0.5, xlabel = 'x', ylabel = 'f(x)', title = 'Plot over a small range of interest of x', show = False)

#Note: In the following segment, the tv that is used is obtained using graphical representation in part(a)
#part(b)
print("\nNewton-Raphson method:")
_roots2.newton(f, df, x0 = 0.3, imax = 2, tv = 0.170180, debug = True)

#part(c)
print("\nSecant method:")
_roots2.secant(f, x0 = 0.5, x1 = 0.4, imax = 4, tv = 0.170180, debug = True)

#part(d)
print("\nModified secant method:")
_roots2.modified_secant2(f, x0 = 0.3, delta = 0.01, imax = 2, tv = 0.170180, debug = True)