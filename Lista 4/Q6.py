import math

def somar(numeros):
    soma = numeros[-2] + numeros[-1]
    return soma

def subtrair(numeros):
    subtração = numeros[-2] - numeros[-1]
    return subtração

def multiplicar(numeros):
    multiplicação = numeros[-2] * numeros[-1]
    return multiplicação

def dividir(numeros):
    divisão = numeros[-2] / numeros[-1]
    return divisão

def decodificar(linha):
    #Operações
    numeros = []
    for c in linha:
        if c == '+':
            numeros.append(somar(numeros))
            numeros.pop(-2)
            numeros.pop(-2)
        elif c == '-':
            numeros.append(subtrair(numeros))
            numeros.pop(-2)
            numeros.pop(-2)
        elif c == '*':
            numeros.append(multiplicar(numeros))
            numeros.pop(-2)
            numeros.pop(-2)
        elif c == '/':
            numeros.append(dividir(numeros))
            numeros.pop(-2)
            numeros.pop(-2)
        elif c != '':
            numeros.append(int(c))
    #Numero perfeito
    numero = numeros[0]
    numero = int(numero)
    multiplos = []
    for i in range(numero - 1):
        if numero % (i + 1) == 0:
            multiplos.append(i + 1)
    somatorio = 0
    for m in multiplos:
        somatorio += m
    if somatorio == numero and numero != 0:
        return '1'
    else:
        return '0'


linha = input()
n = 1
characteres = []
while linha != "Todas as expressoes foram enviadas!":
    #Decodificar letra
    expressão = []
    while linha != '':
        linha = linha.split(' ')
        expressão.append(decodificar(linha))
        linha = input()
    #Binario -> ASCII
    expressão_int = ''.join(expressão)
    character = int(expressão_int, 2)
    character = chr(character)
    print(f"O {n}º conjunto de expressoes resultou no binario {''.join(expressão)} que em ASCII eh: {character}")
    print()
    characteres.append(character)
    n += 1
    linha = input()

print('A decodificacao final resultou em:')
print(''.join(characteres))