__author__ = 'sarvps'

'''
Author: Sarv Parteek Singh
Course: CS-600, Scientific Computation 1
HW: #6, Pr.1
Brief: Root finding for a polynomial of degree 3 using Muller's method
'''

import matplotlib.pyplot as plt
import _poly, _plot, _muller

#x**3 - x**2 + 2*x - 2
a = [-2, 2, -1, 1]

def f(x): return _poly.eval(a, x)

xl, xu = -5, 5
_plot.graph(f, xl, xu, title="y = {}".format(_poly.tostr(a)))

prec = 4

xr1 = _muller.muller(f, xr= 1.2, h=.1, es100=.5*10**(2-prec), debug=True)
print("xr1 = {}".format(xr1))

b = _poly.defl(a, xr1)[0]

xr2, xr3 = _muller.quadratic(a = b[2], b = b[1], c = b[0])
print("xr2 = {}".format(xr2))
print("xr3 = {}".format(xr3))

#plot roots
xr = [xr1, xr2, xr3]
_plot.graph(f, xl, xu, title="y = {}".format(_poly.tostr(a)), show=False)
axes = plt.gca()  #get current axes object and obtain dimensions
left, right = axes.get_xlim(); width = right - left
down, up = axes.get_ylim(); height = up - down
for i in range(len(xr)):
    plt.annotate("xr{} = {:.{p}}".format(i+1, xr[i], p=prec),
                 xy=(xr[i].real, 0), xytext=(xr[i].real + width/25, (i+1)*height/25),
                 arrowprops=dict(width=.25, headwidth=4, headlength=9))
plt.show()