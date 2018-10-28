import sys
nombre = str(sys.argv[1])
longitud = len(nombre)

if longitud < 6:
    print("el nombre es demasiad corto")
if longitud >= 6 and  longitud < 12:
    print(nombre , "is","True")
if longitud > 12:
    print("el nombre es demasiado largo")
