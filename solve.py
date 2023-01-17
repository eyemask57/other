from sympy import *

a = int(input())
b = int(input())
c = int(input())
x = symbols('x')
y = a * x ** 2 + b * x + c
n_m = solve(y, x)
D = b ** 2 - 4 * a * c
if a == 0:
    if b != 0:
        print(str(n_m[0]))
    else:
        print("error!")
elif D == 0: 
    print(str(n_m[0]) + "," + str(n_m[0]))
elif D < 0:
    print("complex number!!")
else:
    print(str(n_m[0]) + "," + str(n_m[1]))