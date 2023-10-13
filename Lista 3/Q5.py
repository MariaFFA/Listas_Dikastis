n = int(input())
matriz = []
matriz_completa = []
for andar in range(n):
    matriz.append([])
    for comodo in range(n):
        tamanho_comodo = input()
        matriz[andar].append(tamanho_comodo)
    matriz_andar = ' '.join(matriz[andar])
    matriz_completa.append(matriz_andar)

matriz_limpa = '\n'.join(matriz_completa)

print(matriz_limpa)
