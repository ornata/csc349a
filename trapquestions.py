import trapezoidalrule as trp
import math

# 21.3
print "----- 21.3"
b = 4.0
a = -2.0
f = lambda x: 1.0-x-4.0*math.pow(x,3.0)+2.0*math.pow(x,5.0)

t1 = trp.traprule(trp.getxs(a,b,2.0), b-a, a, b, 2.0, f)
t2 = trp.traprule(trp.getxs(a,b,4.0), b-a, a, b, 4.0, f)

print t1
print trp.relative_err(1104, t1)
print ""
print t2
print trp.relative_err(1104, t2)

print ""
#21.4
print "----- 21.4"
b = 2.0
a = 1.0
g = lambda x: math.pow(((x + 1.0)/x), 2.0)

for i in range(1,5):
    t = trp.traprule(trp.getxs(a,b,float(i)), b-a, a, b, float(i), g)
    print t
    print trp.relative_err(2.8863, t)
    print ""

print "----- 21.10"

# function for the given table
def table1(x):
    if x == 0.0:
        return 1.0
    elif x == 0.1:
        return 8.0
    elif x == 0.2:
        return 4.0
    elif x == 0.3:
        return 3.5
    elif x == 0.4:
        return 5.0
    elif x == 0.5:
        return 1.0
    return 0

# lambda to be passed in
h = lambda x: table1(x)
b = 0.5
a = 0
# we know the list already
xl = [0.0,0.1,0.2,0.3,0.4,0.5]
t1 = trp.traprule(xl, b-a, a, b, 5.0, h)
print t1




