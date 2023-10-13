equipe1_nome1 = input()
equipe1_nome2 = input()
equipe2_nome1 = input()
equipe2_nome2 = input()

quantidade_partidas = int(input())
quantidade_partidas_originais = quantidade_partidas

#Começo das partidas
print(f"VAMO VER QUEM VAI COMER GRAMA! TEREMOS {quantidade_partidas} PARTIDAS ENTRE:")
print(f"{equipe1_nome1} e {equipe1_nome2} X {equipe2_nome1} e {equipe2_nome2}")

pontos_totais = 0
pontos_totais_equipe1 = 0
pontos_totais_equipe2 = 0
vitorias_equipe1 = 0
vitorias_equipe2 = 0


while quantidade_partidas > 0:
    ponto_equipe1 = int(input())
    ponto_equipe2 = int(input())
    #Partida terminada com 0 pontos
    if ponto_equipe1 == 0:
        quantidade_partidas == 0
        print("JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 1, QUE VERGONHA")
    elif ponto_equipe2 == 0:
        quantidade_partidas = 0
        print("JOGO ENCERRADO POR DESISTÊNCIA DA EQUIPE 2, QUE VERGONHA")
    else:
        pontos_totais += (ponto_equipe1 + ponto_equipe2)
        pontos_totais_equipe1 += ponto_equipe1
        pontos_totais_equipe2 += ponto_equipe2
        if ponto_equipe1 >= ponto_equipe2:
            vitorias_equipe1 += 1
        elif ponto_equipe1 < ponto_equipe2:
            vitorias_equipe2 += 1
    quantidade_partidas -= 1

#Coeficiente para vitoria
coeficiente_equipe1 = pontos_totais_equipe1*(vitorias_equipe1/quantidade_partidas_originais)
coeficiente_equipe2 = pontos_totais_equipe2*(vitorias_equipe2/quantidade_partidas_originais)


#Toddas as partidas terminadas com pontos != 0
if ponto_equipe1 != 0 and ponto_equipe2 != 0:
    print(f"CARAMBA! Tivemos um total de {pontos_totais} bolas ao chão ao longo dessa disputa.")
    if coeficiente_equipe1 >= coeficiente_equipe2:
        print(f"{equipe1_nome1} e {equipe1_nome2} são os grandes vencedores!")
        print(f"Mataram {pontos_totais_equipe1} bolas, ganhando {vitorias_equipe1} partidas")
    elif coeficiente_equipe1 < coeficiente_equipe2:
        print(f"{equipe2_nome1} e {equipe2_nome2} são os grandes vencedores!")
        print(f"Mataram {pontos_totais_equipe2} bolas, ganhando {vitorias_equipe2} partidas")
