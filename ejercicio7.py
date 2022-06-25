lista1 = []
lista2 = []
lista3 = []
for i in range(1, 6):
    lista1.append(int(input("Ingresa el elemento %d para la lista 1: " % i)))
for i in range(1, 6):
    lista2.append(int(input("Ingresa el elemento %d para la lista 2: " % i)))

for i in range(0, 5):
    lista3.append(lista1[i] + lista2[i])

print("La suma de lista 1 y lista 2 es:")
for numero in lista3:
    print(numero, " ", end="")
