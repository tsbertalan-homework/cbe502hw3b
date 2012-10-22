import numpy as np
def findzero(func,(minx,maxx),precision=10000,verbose=False):
    #print "finding zeros between", minx, "and", maxx
    old = func(minx)
    oldsign = getsign(old)
    dx = (maxx-minx)/float(precision)
    roots = []
    xs = np.arange(minx+dx, maxx, dx)
    if verbose:
        print "            finding zeros among", len(xs), "candidates."
    for x in xs:
        value = func(x)
        #if verbose:
            #print "current function value is", value
        cursign = getsign(value)
        if not cursign==oldsign:
            #roots.append(np.around(x,3))
            roots.append(x)
            if verbose:
                print "changed sign at x=",x
        oldsign = cursign
    roots = list(set(roots))
    roots.sort()
    newroots=[]
    #for root in roots:
        #newroots.append(np.round(root,decimals=2))
    #print list(set(newroots))
    if verbose:
        print "returning roots=", roots
    return(roots)
        

def getsign(value):
    '''encode a sign as -1, 1, or 0 for negative, positive, or zero'''
    if value > 0:
        cursign = 1
    elif value < 0:
        cursign = -1
    else:
        cursign = 0
    return cursign

def saysign(sign):
    if sign==-1:
        return "negative"
    elif sign==1:
        return "positive"
    else:
        return "unsigned"
    
if __name__=="__main__":
    testfunc = lambda x: x**2 - 1
    found_roots = findzero(testfunc, (-3,3), precision=1000000)
    print "found these roots:", found_roots
    