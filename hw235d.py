from sys import exit # this allows you to die intentionally in any function
from math import exp
def f235(x, r):
    '''map to return points x_{n+1} = f(x_{n}) for problem 2.35'''
    return x*exp(r*(1-x))

def map_n(x, r, n, func=f235):
    '''wrapper function to call a given function func with input x and parameter r,
     recursively n times.'''
    #print "        calling map_n with n=", n
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
    #print "taking the nth derivative, n=", n
    for i in range(1,n+1): # [1, 2, 3, ... n]
        fnprev = map_n(x, r, n=i-1)
        #print "fnprev is", fnprev
        to_return = to_return * exp(r-r*fnprev)*(1-r*fnprev)
    return to_return

from finder import findzero


def get_fixed_points(func,precision=100000, verbose=False):
    xfp_func = lambda x: func(x) - x
    to_return = findzero(xfp_func, (0,20.0), precision=precision, verbose=verbose) # [1:] leaves out the period-0 fixed point
    #print "about to return these fixed points, minus the first one:", to_return
    return to_return[1:]

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
    print fp1s
    fp1 = fp1s[0]
    
    print "Period-1 fixed point is x=", fp1
    
    print ""
    print ">>>> (b) find first period-doubling point r=r_1"
    
    #should_be_zero = lambda r: abs(nth_derivative(fp1,r,1))
    #fig=plt.figure()
    #ax = fig.add_subplot(1,1,1)
    #xtoplot = np.arange(0.01,4.0,.001)
    #y1toplot = []
    #y2toplot = []
    #y3 = []
    #for x in xtoplot:
        #y1toplot.append(should_be_zero(x))
        #y2toplot.append(0)
        #y3.append(nth_derivative(x,1.0,1))
    ##ax.plot(xtoplot,y1toplot)
    #ax.plot(xtoplot,y2toplot)
    #ax.plot(xtoplot,y3)
    ##ax.set_yscale('log')
    #plt.show()
    
    r1 = get_doubling_point(fp1, 1,precision=100000)
    print "first period-doubling is at r1=", r1
    
    print ""
    print ">>>> (c) after r1=", r1, ", we have multiple solutions to the period-2 fixed-point equation:"
    #zero_for_p2 = lambda x: x*exp(2*r-r*x-r*x*exp(r-r*x))-x
    #def map_n(x, r, n=1, func=f235):
    #zero_for_p2 = lambda x: map_n(x,r,n=2,func=f235)
    r = r1-.01
    print "period-2 solutions at r=", r, "are:"
    map2 = lambda x: map_n(x,r,n=2)
    period_2_solutions = get_fixed_points(map2, precision=10000)
    print "    x=", period_2_solutions
    
    r = r1+.01
    print "period-2 solutions at r=", r, "are:"
    map2 = lambda x: map_n(x, r, n=2)
    period_2_solutions = get_fixed_points(map2,precision=10000)
    print "    x=", period_2_solutions
    print "(of which, one is actually just a period-1 solution)"
    
    r = 5
    print "eventually, period-2 solutions at r=", r, "are:"
    map2 = lambda x: map_n(x, r, n=2)
    period_2_solutions = get_fixed_points(map2, precision=100000)
    print "    x=", period_2_solutions
    
    #r = r1+1
    #zero_for_p2 = lambda x: (f235(f235(x,r),r)-x)
    #period_2_solutions = findzero(zero_for_p2, (.1, 10))
    #print "period-2 solutions at r=", r, "are:"
    #print "    x=", period_2_solutions
    
    print ""
    print ">>>> (d) find the next two period-doublings, r2 and r3"
    #zero_for_r2 = lambda r: abs(nth_derivative(period_2_solutions[2],r,2)) - 1
    ##zero_for_r2 = lambda r: abs((exp(r-r*x)*(1-r*x))*(exp(r-r*f235(x,r))*(1-r*f235(x,r))))-x
    #print findzero(zero_for_r2, (1.0,3.69), verbose=True, precision=10000)
    #r2 = findzero(zero_for_r2, (1.0,3.69), precision=10000)[0]
    fp2 = period_2_solutions[-1]
    r2 = get_doubling_point(fp2,2)
    #r2=2.4
    print "    r2=", r2
    
    r=5
    map3 = lambda x: map_n(x, r, n=3)
    
    #xtoplot = np.arange(1,3.69,.0001)
    #print "graphing with", len(xtoplot), "points"
    #y1toplot = []
    ##y2toplot = []
    #y3toplot = []
    #for x in xtoplot:
        #y1toplot.append(map3(x))
        ##y2toplot.append(zero_for_r2(x))
        #y3toplot.append(0)
    #plt.plot(xtoplot,y1toplot)
    ##plt.plot(xtoplot,y2toplot)
    #plt.plot(xtoplot,y3toplot)
    #plt.show()
    
    period_3_solutions = get_fixed_points(map3,precision=100000)
    #period_3_solutions = findzero(zero_for_p3, (.1, 10), precision=1000)
    #print "period-3 solutions at r=", r, "are:"
    #print "    x=", period_3_solutions
    #print "(%d of them)"%len(period_3_solutions)
    
    fp3 = period_3_solutions[-1]
    r3 = get_doubling_point(fp3,3)
    print "    r3=", r3
    map4 = lambda x: map_n(x, r, n=4)
    #period_4_solutions = get_fixed_points(map4,precision=100000)
    #print "period-4 solutions at r=", r, "are:"
    #print "    x=", period_4_solutions
    #print "(%d of them)"%len(period_4_solutions)
    #exit(0)
    
    
    
    fig=plt.figure()
    ax = fig.add_subplot(1,1,1)
    
    precision=1000
    ymax=1
    xs_ = range(0,int(precision*ymax))
    xs = []
    for x in xs_:
        xs.append(x/float(precision))
    ax.plot(xs,xs)
    rvalues = [r1, r2, r3]
    num_periods = 3
    rlegend_entries = [r'$45 \degree $ line']
    for r in rvalues:
        fxs = []
        for x in xs:
            fxs.append(map_n(x, r, n=num_periods, func=f235))
        ax.plot(xs, fxs)
        rlegend_entries.append(r'$r = %.3f$'%r)
    #ax.set_yscale('log')
    #ax.set_xscale('log')
    fontsize = 20
    ax.set_xlabel(r'$x$', fontsize=fontsize)
    ax.set_ylabel(r'$f^{(%i)}(x)$'%num_periods, fontsize=fontsize)
    ax.legend(rlegend_entries)
    ax.set_title('Attempts to Achieve Period-%d Fixed Points'%num_periods, fontsize=fontsize)
    plt.savefig('hw3_regions.png')
    #plt.show()