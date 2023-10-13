time_1 = input()
time_2 = input()
pontuacao_time1 = int(input())
pontuacao_time2 = int(input())

vitorias_time1 = 0
vitorias_time2 = 0

while vitorias_time1 !=3 and vitorias_time2 != 3:
    if pontuacao_time1 > pontuacao_time2:
        vitorias_time1 += 1
        print(f'O vencedor da {vitorias_time1 + vitorias_time2}ª rodada foi: {time_1}')
    elif pontuacao_time2 > pontuacao_time1:
        vitorias_time2 += 1
        print(f'O vencedor da {vitorias_time2 + vitorias_time1}ª rodada foi: {time_2}')
    if vitorias_time1 !=3 and vitorias_time2 != 3:
      pontuacao_time1 = int(input())
      pontuacao_time2 = int(input())
else:
    if vitorias_time1 == 3:
        vencedor_partida = time_1
    else:
        vencedor_partida = time_2
    print(f'O time {vencedor_partida} ganhou a partida final!')