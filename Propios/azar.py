import sys
from random import randint
n=int(sys.argv[1])
ganador=randint(0,36)
if n==ganador:
    print("El numero ganado es",ganador)
    print("Premio")
else:
    print("El numero ganado es",ganador)
