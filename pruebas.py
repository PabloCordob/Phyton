def redondear(numero):
    numero2=numero*10
    resto=numero2//10
    numero3=numero-resto
    if numero3 >= 0.5:
        print(resto+1)
    elif numero3 <= 0.5:
        print(resto)

redondear(numero=float(input("Ingrese un numero decimal:")))