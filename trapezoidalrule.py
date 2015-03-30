import math

# Interval: [a,b]
# Get n+1 points spaced h = (b-a)/n apart over [a,b]
# Return them in a list
def getxs(a,b,n):
    h = (b-a)/n
    xcurr = a + h
    xlist = [a]

    for i in range(1,int(n+1)):
        xlist.append(xcurr)
        xcurr += h
    return xlist

# Get average height
# that is,
# [f(x0) + 2*(sum of all of the f(xis) that aren't x0 or xn) + xn]/2n
def avgheight(xlist, x0, xn, n, fn):
    return (fn(x0) + 2.0 * sum(map(fn,xlist[1:int(n-1)])) + fn(xn))/(2*n)

# Trapezoidal rule for integration: width * average height over the interval
def traprule(xlist, width, x0, xn, n, fn):
    return width * avgheight(xlist, x0, xn, n, fn)

# Compute relative error from the real answer
def relative_err(real, approx):
    return math.fabs(((approx/real) - 1.0) * 100.0)

