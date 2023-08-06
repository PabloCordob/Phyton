#1. Escriba una función redondear() que permita redondear un número
#decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
#entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
#anterior (3). 
def redondear(numero):
    numero2=numero*10
    resto=numero2//10
    numero3=numero-resto
    if numero3 >= 0.5:
        print(resto+1)
    elif numero3 <= 0.5:
        print(resto)

redondear(numero=float(input("Ingrese un numero decimal:")))

#2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un
#módulo que esté fuera de ese paquete, cree una función de suma de
#decimales que redondee el resultado haciendo uso de la función
#redondear() del paquete recién creado.
from prueba import redondear
numero1=float(input("Ingrese el primer numero:"))
numero2=float(input("Ingrese el segundo numero:"))
suma=numero1+numero2
redondear(suma)