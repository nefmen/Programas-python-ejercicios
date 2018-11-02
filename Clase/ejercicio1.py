import sys
importe = int(sys.argv[1])
billetes50 = importe // 50
resto50 = importe % 50
billetes20 = resto50 // 20
resto20 = resto50 % 20
billetes10 = resto20 // 10
resto10 = resto20 % 10
billetes5 = resto10 // 5
resto5 = resto10 % 5
monedas2 = resto5 // 2
resto2 = resto5 % 2
monedas1 = resto2 // 1
resto1 = resto2 % 1
if billetes50 !=0:
        if billetes50 == 1:
            print (billetes50,"billetes de 50€")
        if billetes50 > 1:
            print (billetes50,"billetes de 50€")
if billetes20 !=0:
    if billetes20 == 1:
        print (billetes20,"billetes de 20€")
    if billetes20 > 1:
        print(billetes20,"billetes de 20€")
if billetes10 !=0:
    if billetes10 == 1:
        print(billetes10,"billetes de 10€")
    if billetes10 > 1:
        print(billetes10,"billetes de 10€")
if billetes5 != 0:
    if billetes5 == 1:
        print(billetes5,"billetes de 5€")
    if billetes5 > 1:
        print(billetes5,"billetes de 5€")
if monedas2 !=0:
    if monedas2 == 1:
        print(monedas2,"monedas de 2€")
    if monedas2 > 1:
        print(monedas2,"monedas de 2€")
if monedas1 != 0:
    if monedas1 == 1:
        print(monedas1,"monedas de 1€")
    if monedas1 > 1:
        print(monedas1,"monedas de 1€")
