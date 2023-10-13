n = int(input())

a = 1
sequencia = str(a)
# Para n escrever os zeros
if n > 1:
    b = 1
    sequencia = sequencia + ', ' + str(b)

for i in range(n - 2):
    c = a + b
    sequencia = sequencia + ', ' + str(c)
    a = b
    b = c

print(f'A sequência de número das camisas do seu time será: {sequencia}')