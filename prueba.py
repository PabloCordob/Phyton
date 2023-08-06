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