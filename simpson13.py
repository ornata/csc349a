import math

# Function for question
def f(x):
    return (1.0-x-4.0*math.pow(x,3.0)+2.0*math.pow(x,5.0))

def simpson(h, f0, f1, f2):
	return 2*h * (f0 + 4*f1 + f2 )/6

# Print percent relative error wrt analytic value
def relative_err(real, approx):
    return math.fabs(((approx/real) - 1.0) * 100.0)

def main():
	b = 4.0
	a = -2.0
	c = a + (b-a)/2.0
	s = simpson((b-a), f(a), f(c), f(b))
	print s
	print relative_err(1104, s)

if __name__ == "__main__":
	main()
