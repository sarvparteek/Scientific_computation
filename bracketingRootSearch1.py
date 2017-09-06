__author__ = 'sarvps'

'''
Author: Sarv Parteek Singh
Course: CS-600, Scientific Computation 1
HW: #5, Pr 5.3, 'Numerical methods for Engineers', 7th edition
Brief: Root finding for a polynomial of degree 5 using bracketing methods
'''

import _roots, _plot

def f(x):
    return -25 + 82*x - 90*(x**2) + 44*(x**3) - 8*(x**4) + 0.7*(x**5)

#Part(a): Two plots are generated: the first gives a holistic view and the second one a zoomed-in view
_plot.graph(f, xl = -50.0, xu = 50.0, xlabel = 'x', ylabel = 'f(x)', title = 'Plot over wide range of x')
_plot.graph(f, xl = 0.5, xu = 1.0, xlabel = 'x', ylabel = 'f(x)', title = 'Plot over a small range of interest of x')

#Part (b)
print("bisection:")
_roots.bisect(f, xl = 0.5, xu = 1.0, es100 = 10, tv = 0.579409, debug = True)

#Part(c)
print("\nfalse position:")
_roots.falsepos(f, xl = 0.5, xu = 1.0, es100 = 0.2, tv = 0.579409, debug = True)