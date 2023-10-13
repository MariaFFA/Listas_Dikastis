def caindo(matriz_caida):
    mudanças = 0
    for l in range(dimensão - 1):
        for c in range(dimensão):
            if matriz_caida[l][c] != 'O':
                if matriz_caida[l + 1][c] == 'O':
                    li = l + 1
                    matriz_caida[li][c] = matriz_caida[l][c]
                    matriz_caida[l][c] = 'O'
                    mudanças +=1
                    
    if mudanças == 0:
        return matriz_caida
    else:
        return caindo(matriz_caida)
    
def eliminando_linhas(matriz, linhaX, linhaH, linhaO, pontuação, linhas):
    for l in range(len(matriz)):
        if matriz[-1-l] == linhaX:
            matriz[-1-l] = linhaO[:]
            if linhas > len(matriz):
                pontuação += (len(matriz))**2 * linhas
            else:
                pontuação += (len(matriz))**2 * len(matriz)
            linhas += 1 
            return matriz, pontuação, linhas
    return matriz, pontuação, linhas

def jogar(matriz, pontuação ,linhas):
    matriz_atual = caindo(matriz)
    matriz_atual, pontuação_atual, linhas = eliminando_linhas(matriz_atual, linha_eliminatoriaX, linha_eliminatoriaH, linha_eliminatoriaO, pontuação, linhas)
    if pontuação == pontuação_atual: 
        return matriz, pontuação, linhas
    else:
        return jogar(matriz_atual, pontuação_atual, linhas)

def limpando_matriz(matriz,dimensão):
    for l in range(dimensão):
        for c in range(dimensão):
            if matriz[l][c] != 'O' and matriz[l][c] != 'H' and matriz[l][c] != 'X':
                    matriz[l][c] = 'O'
    return matriz

dimensão = int(input())

matriz = []
linha_eliminatoriaX = []
linha_eliminatoriaH = []
linha_eliminatoriaO = []
pontuação = 0
linhas = 0

#Matriz
for _ in range(dimensão):
    linha = input()
    linha = list(linha)
    matriz.append(linha)

    #Possivel linha eliminada
    linha_eliminatoriaX.append('X')
    linha_eliminatoriaH.append('H')
    linha_eliminatoriaO.append('O')


ação = input()
matriz = limpando_matriz(matriz, dimensão)
matriz, pontuação, linhas = jogar(matriz, pontuação, linhas)

while ação != 'sair':
    ação = ação.split(',')
    ação[0] = int(ação[0])
    ação[1] = int(ação[1])
    if 0 <= ação[0] < len(matriz) and 0 <= ação[1] < len(matriz) and matriz[ação[0]][ação[1]] == 'O':
        if ação[2] == 'H' or ação[2] == 'X':
            matriz[ação[0]][ação[1]] = ação[2]
            linha_eliminatoriaO = []
            for _ in range(len(matriz)):
                linha_eliminatoriaO.append('O')
        else:
           matriz[ação[0]][ação[1]] = 'O'
    matriz, pontuação, linhas = jogar(matriz,pontuação, linhas)
    ação = input()

print('Resultado:')
for l in matriz:
    l = ''.join(l)
    print(l)
print(f'Pontuação: {pontuação}')