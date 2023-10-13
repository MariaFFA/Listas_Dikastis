duplas = int(input())

#primeira dupla
nome_dupla = input()
periodo_dupla = int(input())
pontos_dupla = int(input())
pontos_dupla = pontos_dupla / periodo_dupla

#automaticamente 1ª dupla vencedora e perdedora simutaneamente
nome_dupla_vencedor = nome_dupla
nome_dupla_perdedor = nome_dupla
pontos_dupla_vencedor = pontos_dupla
pontos_dupla_perdedor = pontos_dupla

#outras duplas
for i in range(duplas - 1):
    nome_dupla2 = input()
    periodo_dupla2 = int(input())
    pontos_dupla2 = int(input())
    pontos_dupla2 = pontos_dupla2 / periodo_dupla2
    #dupla anterior venceu
    if pontos_dupla > pontos_dupla2:
        if pontos_dupla > pontos_dupla_vencedor:
            nome_dupla_vencedor = nome_dupla
            pontos_dupla_vencedor = pontos_dupla
        if pontos_dupla2 < pontos_dupla_perdedor:
            nome_dupla_perdedor = nome_dupla2
            pontos_dupla_perdedor = pontos_dupla2
    #dupla nova venceu
    elif pontos_dupla < pontos_dupla2:
        if pontos_dupla2 > pontos_dupla_vencedor:
            nome_dupla_vencedor = nome_dupla2
            pontos_dupla_vencedor = pontos_dupla2
        if pontos_dupla < pontos_dupla_perdedor:
            nome_dupla_perdedor = nome_dupla
            pontos_dupla_perdedor = pontos_dupla

print(f'A dupla vencedora foi {nome_dupla_vencedor} com a pontuação final de {pontos_dupla_vencedor:,.2f} pontos.')
print(f'A dupla perdedora foi {nome_dupla_perdedor} com a pontuação final de {pontos_dupla_perdedor:,.2f} pontos.')
