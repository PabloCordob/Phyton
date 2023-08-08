from datetime import datetime
dt = datetime.now()
horas=dt.hour
minutos=dt.minute
segundos=dt.second
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
from pruebas import redondear
numero1=float(input("Ingrese el primer numero:"))
numero2=float(input("Ingrese el segundo numero:"))
suma=numero1+numero2
redondear(suma)

#3. Usando el módulo datetime, escribe un programa que muestre la fecha
#y hora actuales del sistema
dt = datetime.now()
print(dt)

#4. Escriba un programa que devuelva un número par al azar entre 2 y 10
#(pista: para comprobar si se pueden generar todos los números, pruebe
#ejecutar el programa dentro de un ciclo infinito).
from pruebas import es_primo
import random
while True:
    numero=int(random.randrange(2,11))
    es_primo(numero)
    if True:
        break

#5. Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
#para la adivinación o para buscar consejo. Su mecanismo es muy simple:
#ante una pregunta del usuario, la bola responde con una de 8 posibles
#respuestas:
#- Es seguro que sí
#- Las chances son buenas
#- Puedes contar con ello
#- Pregúntame de nuevo más tarde
#- Concéntrate y pregunta de nuevo
#- No veo con claridad, intenta de nuevo
#- Mi respuesta es no
#- Mis fuentes me dicen que no
#Escriba una función en Python para simular la bola mágica.

def bola8(numero):
    if numero == 1:
        print("Es seguro que si")
    elif numero == 2:
        print("Las chances son buenas")
    elif numero == 3:
        print("Puedes contar con ello")
    elif numero == 4:
        print("Preguntame de nuevo mas tarde")
    elif numero == 5:
        print("Concentrate y pregunta de nuevo")
    elif numero == 6:
        print("No veo con claridad , intenta de nuevo")
    elif numero == 7:
        print("Mi respues es no")
    elif numero == 8:
        print("Mis fuentes dicen que no")
print("Bienvenido al juego de la Bola ocho")
mensaje=input("Realize su pregunta:")
bola8(numero=random.randrange(1,9))

#6. Encuentre el tiempo de ejecución de los programas de los ejercicios
#anteriores (pista: use el módulo time)
horas2=dt.hour
minutos2=dt.minute
segundos2=dt.second
tiempo=int(segundos2)-int(segundos)
tiempo2=int(minutos2)-int(minutos)
if tiempo2 == 0:
    print(f"El tiempo de ejecucion de los programas fue de {tiempo} segundos.")
elif segundos2 < segundos:
    tiempo2=tiempo2-1
    tiempo=tiempo+60
    print(f"El tiempo de ejecucion de los programas fue de {tiempo2} minutos y {tiempo} segundos.")










