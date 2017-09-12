__author__ = 'sarvps'

'''
Author: Sarv Parteek Singh
Course: CS-600, Scientific Computation 1
HW: #6, Pr.4
Brief: Root finding for a polynomial of degree 4 using Bairstow's method
'''

import matplotlib.pyplot as plt
import _poly, _plot, _bairstow, _muller

#x**4 -2x**3+ 6x**2 -2x + 5
a = [5, -2, 6, -2, 1]

def f(x): return _poly.eval(a, x)

xl, xu = -5, 5
_plot.graph(f, xl, xu, title="y = {}".format(_poly.tostr(a)))

prec = 4

xr1, xr2 = _bairstow.bairstow(a, r=-1, s=1, es100=.5*10**(2-prec), debug=True, tab=11, precision=prec)
print("xr1 = {:.{p}}\nxr2 = {:.{p}}".format(xr1, xr2, p=prec))

#we can find the remaining roots by depleting polynomial a with resulting
#quadratic polynomial (x - xr1)(x - xr2), then continue applying bairstow()
#until we get a quadratic or linear equation, which then can be solved with
#the quadratic formula or simple solving.
a1, _ = _poly.defl(a,xr1)
a2, _ = _poly.defl(a1,xr2)
xr3,xr4 = _muller.quadratic(a = a2[2], b = a2[1], c = a2[0])
print("xr3 = {}".format(xr3))
print("xr4 = {}".format(xr4))

#plot roots
xr = [xr1, xr2, xr3, xr4]
_plot.graph(f, xl, xu, title="y = {}".format(_poly.tostr(a)), show=False)
axes = plt.gca()  #get current axes object and obtain dimensions
left, right = axes.get_xlim(); width = right - left
down, up = axes.get_ylim(); height = up - down
for i in range(len(xr)):
    plt.annotate("xr{} = {:.{p}}".format(i+1, xr[i], p=prec),
                 xy=(xr[i].real, 0), xytext=(xr[i].real + width/25, (i+1)*height/25),
                 arrowprops=dict(width=.25, headwidth=4, headlength=9))
plt.show()
