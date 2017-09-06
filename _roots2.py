
'''
module: _roots2.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapters on open methods for root finding
- implemented from algorithms/pseudocode provided
'''

#open methods...

def fixpt(f, x0, es100=.5, imax=1000, tv=None, debug=False, precision=6, tab=12):
    x0 = float(x0)  #force x0 as float, even if integer passed - avoids potential integer division
    iter = 0
    ea = 1.  #100%
    if debug and tab:
        print("{:<{t}}{:<{t}}{:<{t}}{:<{t}}"
              .format("iter","xr","ea","et",t=tab))
    while ea*100 >= es100 and iter <= imax:
        xr = f(x0) + x0 # We can pass in f(x) + x as the input function too. In that case, this would be just f(x0)
        if xr: ea = abs(1 - x0 / xr)
        et = abs(1 - xr / tv) if tv else float('inf') if tv is not None else float('nan')
        iter += 1
        if debug: print(("{:<{t}}{:<{t}.{p}}{:<{t}.{p}%}{:<{t}.{p}%}" if tab
                         else "iter={}, xr={:.{p}}, ea={:.{p}}, et={:.{p}%}")
                        .format(iter, xr, ea, et, t=tab, p=precision))
        x0 = xr
    return xr
#end fixpt()

def newton(f, df, x0, es100=.5, imax=1000, tv=None, debug=False, precision=6, tab=12):
    x0 = float(x0)  #force x0 as float, even if integer passed - avoids potential integer division
    iter = 0
    ea = 1.  #100%
    if debug and tab:
        print("{:<{t}}{:<{t}}{:<{t}}{:<{t}}"
              .format("iter","xr","ea","et",t=tab))
    while ea*100 >= es100 and iter <= imax:
        xr = x0 - f(x0) / df(x0)
        if xr: ea = abs(1 - x0 / xr)
        et = abs(1 - xr / tv) if tv else float('inf') if tv is not None else float('nan')
        iter += 1
        if debug: print(("{:<{t}}{:<{t}.{p}}{:<{t}.{p}%}{:<{t}.{p}%}" if tab
                         else "iter={}, xr={:.{p}}, ea={:.{p}}, et={:.{p}%}")
                        .format(iter, xr, ea, et, t=tab, p=precision))
        x0 = xr
    return xr
#end newton()

def secant(f, x0, x1, es100=.5, imax=1000, tv=None, debug=False, precision=6, tab=12):
    x0 = float(x0)  #force x0 as float, even if integer passed - avoids potential integer division
    iter = 0
    ea = 1.  #100%
    if debug and tab:
        print("{:<{t}}{:<{t}}{:<{t}}{:<{t}}"
              .format("iter","xr","ea","et",t=tab))
    while ea*100 >= es100 and iter <= imax:
        xr = x0 - f(x0) * (x1 - x0) / (f(x1) - f(x0))
        if xr: ea = abs(1 - x1 / xr)
        et = abs(1 - xr / tv) if tv else float('inf') if tv is not None else float('nan')
        iter += 1
        if debug: print(("{:<{t}}{:<{t}.{p}}{:<{t}.{p}%}{:<{t}.{p}%}" if tab
                         else "iter={}, xr={:.{p}}, ea={:.{p}}, et={:.{p}%}")
                        .format(iter, xr, ea, et, t=tab, p=precision))
        x0 = x1
        x1 = xr
    return xr
#end secant()

def modified_secant2(f, x0, delta=.01, es100=.5, imax=1000, tv=None,
                     debug=False, prec=6, tab=12):
    def df(xi): h = delta * xi; return (f(xi + h) - f(xi)) / h
    return newton(f, df, x0, es100, imax, tv, debug, prec, tab)
#end modified_secant2()