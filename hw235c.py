# Problem 2.35, part c
from math import exp
def find_zero((start, stop), shouldbezero, r, precision=100):
    precision = float(precision)
    start = int(start * precision)
    stop =  int(stop * precision)
    checkrange = range(start,stop)
    xs = []
    diffs = []
    for x in checkrange:
        x = x/precision*1.0
        diff = shouldbezero(x,r)
        xs.append(x)
        diffs.append(abs(diff))
    min_diff = min(diffs)
    index = diffs.index(min_diff)
    return (xs[index], min_diff)

def zero235c(x,r):
    #return 2/x-1-exp(3-3*x)
    return 2*r-r*x*(1+exp(r-r*x))

def zero235d3(x,r):
   #return 3*r-r*x*(1+exp(r-r*x)-r*x*exp(2*r-r*x*(1+exp(r-r*x))))
    return 3*r-r*x*(1+exp(r-r*x))-r*x*exp(2*r-r*x*(1+exp(r-r*x)))
    
if __name__ == "__main__":
    print "part c (period-2 points for r>r_1):"
    ranges = [(1.2, 2.0), (0.75, 1.2), (0.01, 0.75)]
    r = 3
    for tryrange in ranges:
        (x, min_diff) = find_zero(tryrange, zero235c, r, precision=1000000)
        print "closest to zero in range", tryrange, "is", x, "(min_diff=", min_diff, ")"

    #print ""
    #r=4
    #print "part d:"
    #ranges = [(0.01, 9),]
    #for tryrange in ranges:
        #(x, min_diff)= find_zero(tryrange, zero235d3, r, precision=1000000)
        #print "closest to zero in range", tryrange, "is", x, "(min_diff=", min_diff, ")"
    
    
    