#1) Meter los números del 1 al 20 en una lista y mostrarla en pantalla. Hacer lo mismo
# para un rango de números indicado por un usuario. 
lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
mostrar=len(lista)
for rango in range(mostrar):
    print(lista[rango])

numero=int(input("ingresa cuantos numeros quieres que se impriman en pantala:"))
lista=[]
for rango in range(numero+1):
    lista.append(rango)
    print(lista[rango])

#2) Pide un número y guarda en una lista su tabla de multiplicar hasta el 10. Por
#ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50 
numero=int(input("Ingrese el numero que desea saber su tabla de multiplicar:"))
lista=[]
lista.append(numero)
guardado=0
for rango in range(1,10+1):
    guardado+=numero
    lista.append(guardado)
    print(lista[rango])
#3) Pide una cadena (string) por teclado, mete los caracteres en una lista sin repetir
#caracteres.
palabra=input("Que palabra desea ingresar en la lista?:")
contador=len(palabra)
lista=[]
for rango in range(contador):
    lista.append(palabra[rango])
print(lista)
#4) Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios. 
palabra=input("Que palabra desea ingresar en la lista?:")
contador=len(palabra)
contador2=-1
lista=[]
for rango in range(contador):
    lista.append(palabra[rango])
    contador2+=1
    if lista[contador2]==" ":
        lista.remove(" ")
        contador2-=1
print(lista)
#5) Crea una tupla con números, pide un numero por teclado e indica cuantas veces se
#repite.
numero=int(input("Que numero deseas saber cuantas veces se repite en la tupla?:"))
tupla=(1,2,4,32,31,4,2,12,43,2,6)
contador=len(tupla)
veces=0
for rango in range(contador):
    if numero==tupla[rango]:
        veces+=1
print(f"El numero {numero} en la tupla aparece {veces}")
#6) Crea una tupla con los meses del año, pedir números al usuario. Si el numero esta
#entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino
#muestra un mensaje de error. El programa termina cuando el usuario introduce un
#cero
tupla=("El programa termino","enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
contador=len(tupla)
while True:
    numero=int(input("Ingrese un numero:"))
    if numero > 0 and numero < contador:
        print(tupla[numero])
    elif numero == 0:
        print(tupla[numero])
        break
    elif numero < 0 or numero >= 13:
        print("El numero ingresado no es valido")
#7) Crea una tupla con números e indica el número con mayor valor y el que menor
#tenga.
tupla=(1,2,5,2,8,66,7,0)
contador=len(tupla)
mayor=tupla[0]
menor=tupla[0]
for rango in range(contador):
    if mayor < tupla[rango]:
        mayor=tupla[rango]
    if menor > tupla[rango]:
        menor=tupla[rango]
print(f"el mayor numero es {mayor}")
print(f"el menor numero es {menor}")

#9) Opcional: Pide números y mételos en una lista, cuando el usuario meta un 0 ya
#dejaremos de insertar. Por último, muestra los números ordenados de menor a
#mayor.
lista=[]
while True:
    numeros=int(input("Ingrese un numero:"))
    lista.append(numeros)
    if numeros == 0:
        break
contador=len(lista)
for rango in range(contador):
    menor=lista[0]
    for rango2 in range(contador):
        if menor < lista[rango2]:
           menor=menor
        elif menor > lista[rango2]:
            menor=lista[rango2]
    rango2=0
    contador=contador-1
    print(menor)
    lista.remove(menor)