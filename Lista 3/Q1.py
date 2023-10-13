n = int(input())
lista = []

for i in range(n):
    animal = input()
    if animal not in lista:
        lista.append(animal)
    else:
        print('Criatura repetida')

print('Registradas:')
for registrados in lista:
    print(registrados)