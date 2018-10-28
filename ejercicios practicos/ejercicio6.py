import sys
from math import pi
r = float(sys.argv[1])
a = 2 * r
b = 2 * pi * r
c = pi * (r**2)
cadena = input("eliga una opción 1-4 ")
cadena = float(cadena)
if cadena == 1:
    print("El diámetro de la circunferencia es",a)
if cadena == 2:
    print("El perímetro de la cicunferencia es",b)
if cadena == 3:
    print("El área del circulo es",c)
if cadena == 4:
    print("saliendo")
if cadena != 1 and cadena != 2 and cadena != 3 and cadena != 4:
    print("Opción no válida")
