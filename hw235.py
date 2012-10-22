from sys import exit # this allows you to die intentionally in any function
from math import exp
def f235(x, r):
    '''map to return points x_{n+1} = f(x_{n}) for problem 2.35'''
    return x*exp(r*(1-x))

def map_n(x, r, n, func=f235):
    '''wrapper function to call a given function func with input x and parameter r,
     recursively n times.'''
    if n==0:
        return x
    elif n==1:
        to_return = func(x,r)
    else:
        fx = map_n(x, r, n=n-1, func=func)
        to_return = func(fx, r)
    return to_return

    
def nth_derivative(x,r,n):
    '''specifically returns the nth derivitive of the map given in 2.35'''
    to_return = 1.0
    for i in range(1,n+1): # [1, 2, 3, ... n]
        fnprev = map_n(x, r, n=i-1)
        to_return = to_return * exp(r-r*fnprev)*(1-r*fnprev)
    return to_return

    
from finder import findzero


def get_fixed_points(func,precision=100000, verbose=False):
    xfp_func = lambda x: func(x) - x
    to_return = findzero(xfp_func, (0,20.0), precision=precision, verbose=verbose)
    new_roots = []
    for root in to_return:
        new_roots.append(np.round(root,decimals=2))
    to_return = list(set(new_roots))
    to_return.sort()
    return to_return[1:] # [1:] leaves out the period-0 fixed point

    
def get_doubling_point(x, n, precision=100000, verbose=False):
    should_be_zero = lambda r: abs(nth_derivative(x,r,n)) - 1
    doubling_point = findzero(should_be_zero, (0.01,20.0), precision=precision,verbose=verbose)[0]
    return doubling_point

    
if __name__ == "__main__":
    from scipy.optimize import fsolve
    import numpy as np
    import matplotlib.pyplot as plt

    
    print ""
    print ">>>> (a) find period-1 fixed point:"
    map1 = lambda x: map_n(x,100, n=1)  # use a big value of 10 to insure we get equilibrated fp's
    fp1s = get_fixed_points(map1, precision=10000)
    fp1 = fp1s[0]
    print "  Period-1 fixed point is x=", fp1
    
    
    print ""
    print ">>>> (b) find first period-doubling point r=r_1"
    r1 = get_doubling_point(fp1, 1,precision=100000)
    print "  first period-doubling is at r1=", r1
    
    
    print ""
    print ">>>> (c) after r1=", r1, ", we have multiple solutions to the period-2 fixed-point equation:"
    #zero_for_p2 = lambda x: x*exp(2*r-r*x-r*x*exp(r-r*x))-x
    #def map_n(x, r, n=1, func=f235):
    #zero_for_p2 = lambda x: map_n(x,r,n=2,func=f235)
    r = r1-.01
    print "  period-2 solutions at r=", r, "are:"
    map2 = lambda x: map_n(x,r,n=2)
    period_2_solutions = get_fixed_points(map2, precision=10000)
    print "    x=", period_2_solutions
    
    r = r1+.01
    print "  period-2 solutions at r=", r, "are:"
    map2 = lambda x: map_n(x, r, n=2)
    period_2_solutions = get_fixed_points(map2,precision=10000)
    format_solns = '[%.2f, %.2f, %.2f]'
    print "    x=", format_solns%tuple(period_2_solutions)
    print "    (of which, one is actually just a period-1 solution)"
    
    r = 5
    print "  eventually, period-2 solutions at r=", r, "are:"
    map2 = lambda x: map_n(x, r, n=2)
    period_2_solutions = get_fixed_points(map2, precision=100000)
    print "    x=", period_2_solutions
    
    
    print ""
    print ">>>> (d) find the next two period-doublings, r2 and r3"
    fp2 = period_2_solutions[-1]
    r2 = get_doubling_point(fp2,2)
    print "    r2=", r2
    
    r=5
    map3 = lambda x: map_n(x, r, n=3)    
    period_3_solutions = get_fixed_points(map3,precision=100000)
    
    fp3 = period_3_solutions[-1]
    r3 = get_doubling_point(fp3,3)
    print "    r3=", r3
