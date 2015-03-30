import math
import trapezoidalrule as trp

g = 9.8
m = 68.1
cd = 0.25
t = 10
n = 50

fn = lambda t: math.sqrt(g*m/cd) * math.tanh(math.sqrt(g*cd/m) * t)

f = trp.getxs(0,10,n)
print f
f = map(fn, f)
h = 10.0/float(n)
print h

print trp.trapm(h, n, f)
# actual val: 333.92622