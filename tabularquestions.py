import trapezoidalrule as trp
import simpson13 as s13
import simpson38 as s38
import math

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

def main():

    print "----- 21.10 (a)"
    f = lambda x: table1(x)
    b = 0.5
    a = 0
    li = [0.0,0.1,0.2,0.3,0.4,0.5]

    print trp.traprule(li, b-a, a, b, 5.0, f)
    print s13.simpson(b-a, a, b, f)
    print s38.simpson(li, b-a, a, b, f)


if __name__ == "__main__":
    main()