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
    return (f(x0) + 2.0 * sum(map(fn,xlist[1:int(n-1)])) + fn(xn))/(2*n)

# Trapezoidal rule for integration: width * average height over the interval
def traprule(xlist, width, x0, xn, n, fn):
    return width * avgheight(xlist, x0, xn, n, fn)

# Compute relative error from the real answer
def relative_err(real, approx):
    return math.fabs(((approx/real) - 1.0) * 100.0)

# 21.3
print "----- 21.3"
b = 4.0
a = -2.0
f = lambda x: 1.0-x-4.0*math.pow(x,3.0)+2.0*math.pow(x,5.0)

t1 = traprule(getxs(a,b,2.0), b-a, a, b, 2.0, f)
t2 = traprule(getxs(a,b,4.0), b-a, a, b, 4.0, f)

print t1
print relative_err(1104, t1)
print ""
print t2
print relative_err(1104, t2)

print ""
#21.4
print "----- 21.4"
b = 2.0
a = 1.0
g = lambda x: math.pow(((x + 1.0)/x), 2.0)

for i in range(1,5):
    t = traprule(getxs(a,b,float(i)), b-a, a, b, float(i), g)
    print t
    print relative_err(2.8863, t)
    print ""

