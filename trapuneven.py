import math
from simpson13 import simpson as s13
from simpson38 import simpson as s38
from trapezoidalrule import single_trap
from trapezoidalrule import relative_err

# Function for question
def table(x):
	if x == 0:
		return 2.0
	elif x == 0.05:
		return 1.8555
	elif x == 0.15:
		return 1.5970
	elif x == 0.25:
		return 1.3476
	elif x == 0.35:
		return 1.1831
	elif x == 0.475:
		return 0.9808
	elif x == 0.6:
		return 0.8131
	return 0.0

# trapezoidal rule on uneven step size
def trapuneven(x, y, n):
	trap = 0.0
	for i in range(1, n):
		trap += (x[i] - x[i-1]) * (y[i] + y[i-1]) / 2
	return trap

# combination trapezoidal rule using simpson's rules wherever possible
# when 2 adjacent strips are of equal length, use simpson's 1/3
# when 3 are equal, use simpson's 3/8
# otherwise, use the trapezoidal rule
def combtrap(x, y, n, fn):
	h = x[1] - x[0]
	k = 1
	trap = 0.0
	for j in range(1,n):
		hf = x[j+1] - x[j]
		if math.fabs(h - hf) < 0.000001:
			if k == 3:
				trap += s13(h, y[j-3], y[j-2], y[j-1])
				k -= 1
			else:
				k += 1
		else:
			if k == 1:
				trap += single_trap(h, y[j-1], y[j])
			else:
				if k == 2:
					trap += s13(h, y[j-2], y[j-1], y[j])
				else:
					trap += s38(h, y[j-3], y[j-2], y[j-1], y[j])
				k = 1
		h = hf
	return trap

fn = lambda x: table(x)
x = [0, 0.05, 0.15, 0.25, 0.35, 0.475, 0.6]
y = map(fn, x)
n = 6

t = trapuneven(x, y, n)
print t
print relative_err(0.79124, t)

c = combtrap(x, y, n, fn)
print c
print relative_err(0.79124, c)

