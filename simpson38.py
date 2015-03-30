import math

# Function for question
def f(x):
    return (1.0-x-4.0*math.pow(x,3.0)+2.0*math.pow(x,5.0))

def simpson(h, f0, f1, f2, f3):
	return 3*h * (f0 + 3*(f1 + f2) + f3)/8

# Print percent relative error wrt analytic value
def relative_err(real, approx):
    return math.fabs(((approx/real) - 1.0) * 100.0)

def main():
	b = 4.0
	a = -2.0
	h = (b-a)/3.0
	s = simpson(h, f(a), f(a + h), f(a + 2.0*h), f(b))
	print s
	print relative_err(1104, s)

if __name__ == "__main__":
	main()
