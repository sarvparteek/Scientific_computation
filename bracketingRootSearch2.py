__author__ = 'sarvps'

'''
Author: Sarv Parteek Singh
Course: CS-600, Scientific Computation 1
HW: #5, Pr 5.4, 'Numerical methods for Engineers', 7th edition
Brief: Root finding for a polynomial of degree 3 using bracketing methods
'''

import _roots, _plot

def f(x):
    return -12 - 21*x + 18*(x**2) - 2.75*(x**3)

#Part(a): Two plots are generated: the first gives a holistic view and the second one a zoomed-in view
_plot.graph(f, xl = -10.0, xu = 10.0, xlabel = 'x', ylabel = 'f(x)', title = 'Plot over wide range of x')
_plot.graph(f, xl = -1.0, xu = 0.0, xlabel = 'x', ylabel = 'f(x)', title = 'Plot over a small range of interest of x')

#Part (b)
print("bisection:")
_roots.bisect(f, xl = -1.0, xu = 0.0, es100 = 1.0, tv = -0.414689, debug = True) #tv obtained from graphical representation

#Part(c)
print("\nfalse position:")
_roots.falsepos(f, xl = -1.0, xu = 0.0, es100 = 1.0, tv = -0.414689, debug = True) #tv obtained from graphical representation