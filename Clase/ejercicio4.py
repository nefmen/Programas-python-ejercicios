import sys
from math import sqrt
x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])
x3 = float(sys.argv[5])
y3 = float(sys.argv[6])
d1 = sqrt((x1-x2)**2 + (y1-y2)**2) < sqrt((x1-x3)**2 + (y1-y3)**2)
d2 = sqrt((x1-x3)**2 + (y1-y3)**2) < sqrt((x1-x2)**2 + (y1-y2)**2)
dt1 = sqrt((x1-x2)**2 + (y1-y2)**2)
dt2 = sqrt((x1-x3)**2 + (y1-y3)**2)
if d1:
    print("el punto","(",x2,",",y2,")" "es mas cercano","a","(",x1,",",y1,")" , "con distancia",dt2)
elif d2:
    print("el punto","(",x3,",",y3,")" "es mas cercano","a","(",x1,",",y1,")" , "con distancia",dt2)
