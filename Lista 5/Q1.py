#Fatoração
def fatorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fatorial(n-1)

lower = 0
upper = 0

str_random = input()

#Quantidade de maiúsculas e minúsculas
for l in str_random:
    if l.islower():
        lower += 1
    elif l.isupper():
        upper += 1

#Condições
if lower > upper:
    preço = fatorial(lower) * len(str_random)
elif lower < upper:
    preço = fatorial(upper) * len(str_random)
else:
    preço = (len(str_random))**2

#Conclução
if preço >= 100:
    print(f'Hum... {preço}? Acho que na volta eu compro')
else:
    print(f'{preço}! Vou comprar todos!')