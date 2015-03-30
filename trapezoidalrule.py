import math

# Interval: [a,b]
# Get n+1 points spaced h = (b-a)/n apart over [a,b]
# Return them in a list
def getxs(a, b, n):
    h = (b-a)/float(n)
    xcurr = a + h
    xlist = [a]

    for i in range(1,int(n+1)):
        xlist.append(xcurr)
        xcurr += h
    return xlist

# Compute relative error from the real answer
def relative_err(real, approx):
    return math.fabs(((approx/real) - 1.0) * 100.0)

def single_trap(h, f0, f1):
    return h * (f0 + f1)/2.0

def trapm(h, n, f):
    trp = f[0]
    for i in range(1, n-1):
        trp += 2.0 * f[i]
    trp += f[n]
    return h * trp/2.0
