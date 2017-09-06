
'''
module: _roots.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapters on bracketing methods for root finding
- implemented from algorithms/pseudocode provided
'''

#bracketing methods...

def bisect(f, xl, xu, es100=.5, imax=1000, tv=None, debug=False, precision=6, tab=12):
    xl = float(xl)  #force xl,xu as float, even if integer passed - avoids potential integer division
    xu = float(xu)
    iter = 0
    x0 = xl
    ea = 1.  #100%
    if debug and tab:
        print("{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}"
              .format("iter","xl","xu","xr","ea","et",t=tab))
    while ea*100 >= es100 and iter <= imax:
        xr = (xl + xu) / 2.
        if xr: ea = abs(1 - x0 / xr)
        et = abs(1 - xr / tv) if tv else float('inf') if tv is not None else float('nan')
        iter += 1
        if debug:
            print(("{:<{t}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}%}{:<{t}.{p}%}" if tab
                   else "iter={}, xl={:.{p}}, xu={:.{p}}, xr={:.{p}}, ea={:.{p}%}, et={:.{p}%}")
                  .format(iter, xl, xu, xr, ea, et, t=tab, p=precision))
        test = f(xl) * f(xr)
        if test < 0: xu = xr
        elif test > 0: xl = xr
        else: ea = 0.0
        x0 = xr
    #end while()
    return xr
#end bisect()

def falsepos(f, xl, xu, es100=.5, imax=1000, tv=None, debug=False, precision=6, tab=12):
    xl = float(xl)  #force xl,xu as float, even if integer passed - avoids potential integer division
    xu = float(xu)
    iter = 0
    x0 = xl
    ea = 1.  #100%
    if debug and tab:
        print("{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}"
              .format("iter","xl","xu","xr","ea","et",t=tab))
    while ea*100 >= es100 and iter <= imax:
        xr = xu - f(xu)*(xl - xu) / (f(xl) - f(xu))
        if xr: ea = abs(1 - x0 / xr)
        et = abs(1 - xr / tv) if tv else float('inf') if tv is not None else float('nan')
        iter += 1
        if debug:
            print(("{:<{t}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}%}{:<{t}.{p}%}" if tab
                   else "iter={}, xl={:.{p}}, xu={:.{p}}, xr={:.{p}}, ea={:.{p}%}, et={:.{p}%}")
                  .format(iter, xl, xu, xr, ea, et, t=tab, p=precision))
        test = f(xl) * f(xr)
        if test < 0: xu = xr
        elif test > 0: xl = xr
        else: ea = 0.
        x0 = xr
    #end while()
    return xr
#end falsepos()
