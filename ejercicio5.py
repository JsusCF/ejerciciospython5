import random
lista = []
for i in range(1, 11):
    lista.append(random.randint(1, 10))
lista.sort()
print(lista)