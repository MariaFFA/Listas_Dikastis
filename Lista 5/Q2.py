Vidas_Casas = input()

Vidas_Casas = Vidas_Casas.split(' ')
vidas = int(Vidas_Casas[0])
casas_totais = int(Vidas_Casas[1])
casa_atual = 0

#Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

while casa_atual != casas_totais and vidas > 0:
    casas = int(input())
    lista_fibonacci = [0]
    fibonacci_atual = 1
    #Lista Fibonacci
    while lista_fibonacci[-1] < casas:
        lista_fibonacci.append(fibonacci(fibonacci_atual))
        fibonacci_atual += 1
    if casas in lista_fibonacci:
        casa_atual += 1
    else:
        print("Oh nao Link! Voce nao pode parar ainda, voce e a ultima esperanca de Hyrule!")
        vidas -= 1
        casa_atual = 0

if casa_atual == casas_totais:
    print("Voce Adicionou A Master Sword ao seu inventario")
    print("Link Salve Hyrule!!!")
else:
    print("A ultima defesa de hyrule caiu, nao sobrou ninguem capaz de se opor a Ganondorf")