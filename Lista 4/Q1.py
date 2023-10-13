qtd_operações = int(input())

#Soma
def soma(a,b):
    return(a+b)
#Subtrair
def subtração(a,b):
    return(a-b)
#Multiplicar
def produto(a,b):
    return(a*b)
#Dividir
def divisao(a,b):
    return(a/b)
#Elevar
def potencia(a,b):
    return(a**b)
operação_atual = 1
if qtd_operações == 0:
    print('Vou relaxar aqui na minha nave')
else:
    while operação_atual <= qtd_operações:
        operação =input()
        numero1 = float(input())
        numero2 = float(input())
        if operação == 'Quero somar esses dois números:':
            resultado = soma(numero1,numero2)
        elif operação == 'Preciso subtrair um pelo outro':
            resultado = subtração(numero1,numero2)
        elif operação == 'Quanto dá o produto disso?':
            resultado = produto(numero1,numero2)
        elif operação == 'Vou dividir aqui rapidinho':
            resultado = divisao(numero1,numero2)
        elif operação == 'E se eu elevar um pelo outro?':
            resultado = potencia(numero1,numero2)
        print(f'O resultado da {operação_atual}ª operação foi {resultado:,.1f}')
        operação_atual += 1
    print('Ufa, já deu de cálculos por hoje!')
