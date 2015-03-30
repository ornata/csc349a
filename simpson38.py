import math

# Function for question
def f(x):
    return (1.0-x-4.0*math.pow(x,3.0)+2.0*math.pow(x,5.0))

# get the two inner points, return all four in a list
def getxs(a,b):
    h = (b-a)/3.0
    xlist = [f(a), 3.0*f(a+h), 3.0*f(a+2.0*h), f(b)]
    return xlist

# return the width times the average height defined
def simpson(width, a, b):
	return width * sum(getxs(a,b))/8

# Print percent relative error wrt analytic value
def relative_err(real, approx):
    return math.fabs(((approx/real) - 1.0) * 100.0)

b = 4.0
a = -2.0
s = simpson((b-a), a, b)
print s
print relative_err(1104, s)
