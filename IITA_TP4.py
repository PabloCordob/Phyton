#1)Escriba una función que muestre todos los números primos entre 1 y un número n que es
#ingresado por parámetro.
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return 
    return print(numero)
limite=int(input("ingrese un limite para buscar numeros primos:"))
for rango in range(1,limite+1):
    es_primo(rango)

#2) Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta
#que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje
#avisando que ya se agregó el condimento al sándwich. Escriba versiones diferentes del
#programa de acuerdo a estos criterios:
#• Use un test condicional en el ciclo while para detener la ejecución.
#• Use un test condicional dentro del ciclo para decidir si continuar la ejecución.
#1
def hacer_sandwich():
    condimentos = []
    while True:
        condimento = input("Ingrese un condimento para el sándwich (o 'salir' para terminar): ")
        if condimento == 'salir':
            break
        else:
            condimentos.append(condimento)
            print(f"Se agregó '{condimento}' al sándwich.")

    return condimentos

print("¡Bienvenido a la creación de sándwiches!")
ingredientes_sandwich = hacer_sandwich()
print("\nSu sándwich ha sido creado con los siguientes condimentos:")
for condimento in ingredientes_sandwich:
    print(f"- {condimento}")

#2
lista=[]
while True:
    condimento = input("Ingrese un condimento para el sándwich (o 'salir' para terminar): ")
    if condimento == "salir":
         break
    else:
         lista.append(condimento)
    print("se agrego un condimento al sandwich")
    agregar=input("desea seguir agregando condimentos al sandwich o salir del programa?")
    if agregar == "salir": 
            break
    elif agregar == "seguir":
            pass
    elif agregar != "seguir" or agregar != "salir":
         print("la opcion no es valida")
         break
sandwich=lista
print("\nBienvenido a la colocacion de condimentos")
print(f"se agrego {sandwich} de condimentos al sandwich")


#3) A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un
#tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje
#describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez
#usando argumentos por posición. Llámela una segunda vez usando argumentos por clave.

#B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por
#defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los
#valores por defecto, y la segunda con valores diferentes.

def hacer_remera(tamano, mensaje):
    print(f"Tamaño de la remera: {tamano}")
    print(f"Mensaje impreso en la remera: {mensaje}")

hacer_remera("L", "Me gusta python")

hacer_remera(tamano="L",mensaje="Me gusta python")

def hacer_remera(tamaño,mensaje):
    print(f"Tamaño de la remera: {tamaño}")
    print(f"Mensaje impreso en la remera: {mensaje}")


hacer_remera("L","me gusta python")
while True:
    opcion=input("Desea crear otra remera?.(si o no):")
    if opcion == "si":
        hacer_remera(tamaño=input("ingrese una talle:"),mensaje=input("Ingrese un mensaje para la remera:"))
    elif opcion == "no":
         break 
    else:
         print("la opcion no es valida")
         break
    
#4) Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros
#de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo
#número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …). 

def fibonacci(n):
    series = []
    valor1, valor2 = 0, 1

    for _ in range(n):
        series.append(valor1)
        valor1, valor2 = valor2, valor1 + valor2

    return series
n = 10
serie_de_fibonacci = fibonacci(n)
print(serie_de_fibonacci)







