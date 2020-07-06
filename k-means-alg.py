import math

DELTA = 0.25
A = (2,2, 'A')
B = (2,0, 'B')
C = (-2,2, 'C')
D = (-1,-2, 'D')
E = (0,-3, 'E')

points = [A,B,C,D,E]

Z1 = (0,0, 'F')
Z2 = (-2,-3, 'G')

def delta(a, b):
    dx = a[0]-b[0]
    dy = a[1]-b[1]
    return math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))

def print_del(a,b, d):
    print ("d(", b[2], ",", a[2], ") =", round(d, 5))

def calc():
    C1 = Z1
    C2 = Z2

    delt = DELTA + 1
    while delt > DELTA:
        diffC1 = []
        diffC2 = []
        assertC1 = []
        assertC2 = []
        for p in points: 
            d1 = delta(p, C1)
            print_del(p, C1, d1)
            d2 = delta(p, C2)
            print_del(p, C2, d2)
            diffC1.append(d1)
            diffC2.append(d2)
            if d1 > d2:
                assertC2.append(p)
                print ("assign (", C2[2], ",", p[2], ")\n")
            else:
                assertC1.append(p)
                print ("assign (", C1[2], ",", p[2], ")\n")
        sum_x = 0
        sum_y = 0
        for p in assertC1:
            sum_x += p[0]
            sum_y += p[1]
        newC1 = ((sum_x) / len(assertC1), (sum_y) / len(assertC1), (C1[2] + '\''))
        delt1 = delta(C1, newC1)
        print (newC1[2], "= (",  round(newC1[0],5), ",",  round(newC1[1],5), ")")
        print ("d(", C1[2], ",", newC1[2], ") =", round(delt1,5), "\n")
        C1 = newC1
        
        sum_x = 0
        sum_y = 0
        for p in assertC2:
            sum_x += p[0]
            sum_y += p[1]
        newC2 = ((sum_x) / len(assertC2), (sum_y) / len(assertC2), (C2[2] + '\''))
        delt2 = delta(C2, newC2)
        print (newC2[2], "= (", round(newC2[0],5), ",", round(newC2[1],5), ")") 
        print ("d(", C2[2], ",", newC2[2], ") =", round(delt2,5), "\n")
        C2 = newC2
        
        if (delt1 > delt2):
            delt = delt1
        else:
            delt = delt2

calc()
    

