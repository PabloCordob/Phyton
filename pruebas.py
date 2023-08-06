def redondear(numero):
    numero2=numero*10
    resto=numero2//10
    numero3=numero-resto
    if numero3 >= 0.5:
        print(resto+1)
    elif numero3 <= 0.5:
        print(resto)

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return 
    return print(numero)

import random
lista=[1,2,3,4,5,6]
print(int(random.uniform(2,11)))