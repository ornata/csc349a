import trapezoidalrule as trp
import math

# 21.3
print "----- 21.3"
b = 4.0
a = -2.0
fn = lambda x: 1.0-x-4.0*math.pow(x,3.0)+2.0*math.pow(x,5.0)

h1 = (b-a)/2.0
h2 = (b-a)/4.0

li = map(fn, trp.getxs(a, b, 2.0))
t1 = trp.trapm(h1, 2, li)

li = map(fn, trp.getxs(a, b, 4.0))
t2 = trp.trapm(h2, 4, li)

t0 = trp.single_trap(b-a, fn(a), fn(b))
print t0
print trp.relative_err(1104.0, t0)
print ""

print t1
print trp.relative_err(1104.0, t1)
print ""
print t2
print trp.relative_err(1104.0, t2)

print ""
#21.4
print "----- 21.4"
b = 2.0
a = 1.0
fn = lambda x: math.pow(((x + 1.0)/x), 2.0)
for i in range(1,5):
	h = (b-a)/float(i)
	li = map(fn, trp.getxs(a, b, i))
	t = trp.trapm(h, len(li)-1, li)
	print t
	print trp.relative_err(2.8863, t)
	print ""




