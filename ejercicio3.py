notas = []
for i in range(1, 6):
    while True:
        nota = int(input("Introduce la nota %d: " % i))
        if 0 <= nota <= 10:
            break
    notas.append(nota)
print("Notas:", notas)
print("Nota media: ", sum(notas) / len(notas))
print("Nota max: ", max(notas))
print("Nota min: ", min(notas))