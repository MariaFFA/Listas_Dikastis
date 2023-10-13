import math

coordeandaX = input()
coordeandaY = input()

coordeandaX = coordeandaX.lower()
coordeandaY = coordeandaY.lower()
coordeandaX = list(coordeandaX)
coordeandaY = list(coordeandaY)

len_original = 0

while len_original != len(coordeandaX):
    len_original = len(coordeandaX)
    for i in range(len(coordeandaX) - 1):
        if i < (len(coordeandaX) - 1) and coordeandaX[i].isnumeric() and coordeandaX[i+1].isnumeric():
            coordeandaX[i] = coordeandaX[i] + coordeandaX[i + 1]       
            coordeandaX.pop(i + 1)

len_original = 0

while len_original != len(coordeandaY):
    len_original = len(coordeandaY)
    for i in range(len(coordeandaY) - 1):
        if i < (len(coordeandaY) - 1) and coordeandaY[i].isnumeric() and coordeandaY[i+1].isnumeric():
            coordeandaY[i] = coordeandaY[i] + coordeandaY[i + 1]       
            coordeandaY.pop(i + 1)

def decodificar_codigo(coordenada):
    #Passo 1 - Separar tipos
    numeros = []
    vogais = []
    consoantes = []
    for c in coordenada:
        if c.isnumeric():
            numeros.append(c)
        elif c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            vogais.append(c)
        else:
            consoantes.append(c)
    
    #Passo 2
    if len(consoantes) == 0:
        divisao = 0
    else:
        divisao = len(vogais) / len(consoantes)

    #Passo 3
    divisao = math.floor(divisao)

    #Verficar se os numeros decidem
    if len(numeros) != 0:
        multiplo = 0
        for m in numeros:
            multiplicar = 1
            while int(numeros[0]) * multiplicar <= int(m):
                if int(numeros[0]) * multiplicar == int(m):
                    multiplo += 1
                multiplicar += 1
        if multiplo == len(numeros):
            return 3
        else:
            #Passo 4
            return divisao % 7
    else:
        #Passo 4
        return divisao % 7
        
coordeandaX = decodificar_codigo(coordeandaX)
coordeandaY = decodificar_codigo(coordeandaY)

#Matriz
matriz = [['.', '.', '.', '.', '.', '.', '.'], 
          ['.', '.', '.', '.', '.', '.', '.'], 
          ['.', '.', '.', '.', '.', '.', '.'], 
          ['.', '.', '.', '.', '.', '.', '.'], 
          ['.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.', '.']]

matriz[coordeandaX][coordeandaY] = '☆'

print(' '.join(matriz[0]))
print(' '.join(matriz[1]))
print(' '.join(matriz[2]))
print(' '.join(matriz[3]))
print(' '.join(matriz[4]))
print(' '.join(matriz[5]))
print(' '.join(matriz[6]))

#Frases
if matriz[3][3] == '☆':
    print('Ótimo, a estrela vai ficar exatamente no meio da fotografia! Posição melhor não existe!')
    print('Obrigado pela ajuda! A foto ficou ótima!')
elif '☆' in matriz[0] or '☆' in matriz[6] or '☆' == matriz[1][0] or '☆' == matriz[2][0] or  '☆' == matriz[3][0] or '☆' == matriz[4][0] or '☆' == matriz[5][0] or '☆' == matriz[1][6] or '☆' == matriz[2][6] or '☆' == matriz[3][6] or '☆' == matriz[4][6] or '☆' == matriz[5][6]:
    print('Ihhh, vou ter que relocalizar a câmera, uma fotografia com a estrela na borda não dá! Infelizmente demora um pouco para criar outro código...')
    print('Mesmo que eu não tenha conseguido uma matriz boa para tirar a foto, obrigado pelo seu tempo.')
else:
    print('Ok, agora é só enviar a matriz!')
    print('Obrigado pela ajuda! A foto ficou ótima!')