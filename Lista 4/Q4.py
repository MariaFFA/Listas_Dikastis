capsulas = eval(input())
posicao_explosao = eval(input())
raio_impacto = int(input())

#Checar se explodirá
def checar_sobreviventes(x,y):
    distancia = ((posicao_explosao[0] - x)**2 + (posicao_explosao[1] - y)**2 )**(1/2)
    if distancia > raio_impacto:
        return True
    else:
        return False

#Media dos astronautas por capsula
def pontos_centrais(capsula):
    media = [0, 0]
    for a in capsula:
        media[0] += a[0]
        media[1] += a[1]
    media[0] = media[0] / len(capsula)
    media[1] = media[1] / len(capsula)
    return media

#Verificar cada capsula e astronauta
def resgatar_astronautas():
    sobreviventes = 0
    resultado = [[]]
    for capsula in capsulas:
        astronautas_sobreviventes = []
        for astronauta in capsula:
            if checar_sobreviventes(astronauta[0],astronauta[1]):
                sobreviventes += 1
                astronautas_sobreviventes.append(astronauta)
        if astronautas_sobreviventes != []:
            resultado[0].append(pontos_centrais(astronautas_sobreviventes))
    resultado.insert(0, sobreviventes)
    return resultado

print(resgatar_astronautas())