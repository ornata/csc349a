import math

# Function for question
def f(x):
    return (1.0-x-4.0*math.pow(x,3.0)+2.0*math.pow(x,5.0))

# get the two inner points, return all four in a list
def getxs(a, b, fn):
    h = (b-a)/3.0
    xlist = [fn(a), 3.0*fn(a+h), 3.0*fn(a+2.0*h), fn(b)]
    return xlist

# return the width times the average height defined
def simpson(xlist, width, a, b, fn):
	return width * sum(xlist)/8

# Print percent relative error wrt analytic value
def relative_err(real, approx):
    return math.fabs(((approx/real) - 1.0) * 100.0)

def main():
	b = 4.0
	a = -2.0
	fn = lambda x: f(x)
	s = simpson(getxs(a,b,fn), (b-a), a, b, fn)
	print s
	print relative_err(1104, s)

if __name__ == "__main__":
	main()
