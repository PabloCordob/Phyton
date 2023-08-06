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

