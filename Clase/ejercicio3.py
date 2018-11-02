import sys
from math import sqrt
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2*a)
x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2*a)
if a == 0:
    print(-c/b)
elif b ** 2 - 4 * a * c < 0:
    print("no tiene solución real")
if  b ** 2 - 4 * a * c > 0:
    print("x1 es", x1)
    print("x2 es", x2)
    
