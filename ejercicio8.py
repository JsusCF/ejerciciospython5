nombres = []
edades = []
while True:
    nombre = input("Introduce el nombre de un alumno: ")
    if nombre != "*":
        nombres.append(nombre)
        edades.append(int(input("Ingrese su edad: ")))
    if nombre == "*":
        break

edad_max = max(edades)
print("")
print("Alumnos mayores de edad")
for nombre, edad in zip(nombres, edades):
    if edad >= 18:
        print(nombre)
print("")
print("Alumnos mayores")
for nombre, edad in zip(nombres, edades):
    if 30 <= edad <= edad_max:
        print(nombre)
