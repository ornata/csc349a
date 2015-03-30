import math

# Function for question
def f(x):
    return (1.0-x-4.0*math.pow(x,3.0)+2.0*math.pow(x,5.0))

# return the width times the average height.
# simpson's rule just works with a second-order interpolating
# polynomial so we can just do this all in here without having
# another function. it's very simple!
def simpson(width, a, b):
	c = a + (b-a)/2.0
	li = [f(a), 4*f(c), f(b)]
	return width * sum(li)/6

# Print percent relative error wrt analytic value
def relative_err(real, approx):
    return math.fabs(((approx/real) - 1.0) * 100.0)

b = 4.0
a = -2.0
s = simpson((b-a), a, b)
print s
print relative_err(1104, s)
