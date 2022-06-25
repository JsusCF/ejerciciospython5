lista = []
numero = int(input("Introduce un numero: "))
while numero >= 0:
    lista.append(numero)
    numero = int(input("Introduce un numero: "))

for numero in lista:
    print(numero, " ", end="")
