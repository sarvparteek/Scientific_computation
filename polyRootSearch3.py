__author__ = 'sarvps'

'''
Author: Sarv Parteek Singh
Course: CS-600, Scientific Computation 1
HW: #6, Pr.3
Brief: Root finding for a polynomial of degree 3 using Bairstow's method
'''

import matplotlib.pyplot as plt
import _poly, _plot, _bairstow, _muller

#-2 + 6.2*x - 4*x**2 + 0.7*x**3
a = [-2, 6.2, -4, 0.7]

def f(x): return _poly.eval(a, x)

xl, xu = -5, 5
_plot.graph(f, xl, xu, title="y = {}".format(_poly.tostr(a)))

prec = 4

xr1, xr2 = _bairstow.bairstow(a, r=2, s=-1, es100=.5*10**(2-prec), debug=True, tab=11, precision=prec)
print("xr1 = {:.{p}}\nxr2 = {:.{p}}".format(xr1, xr2, p=prec))

a1, q = _poly.defl(a,xr1)
a2, _ = _poly.defl(a1,xr2)
xr3 = -a2[0]/a2[1]
print("xr3 = {}".format(xr3))

#plot roots
xr = [xr1, xr2,xr3]
_plot.graph(f, xl, xu, title="y = {}".format(_poly.tostr(a)), show=False)
axes = plt.gca()  #get current axes object and obtain dimensions
left, right = axes.get_xlim(); width = right - left
down, up = axes.get_ylim(); height = up - down
for i in range(len(xr)):
    plt.annotate("xr{} = {:.{p}}".format(i+1, xr[i], p=prec),
                 xy=(xr[i].real, 0), xytext=(xr[i].real + width/25, (i+1)*height/25),
                 arrowprops=dict(width=.25, headwidth=4, headlength=9))
plt.show()
