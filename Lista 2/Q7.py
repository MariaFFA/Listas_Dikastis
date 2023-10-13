qtd_partidas = int(input())

pontos_jogador = 0
pontos_adversario = 0
i = 1

#Cada partida - a ultima
while qtd_partidas > 1:
    qtd_rodadas = int(input())
    print(f'Vai começar a {i}º partida. Esse jogo terá {qtd_rodadas} rodada(s).')
    pontos_jogador = 0
    pontos_adversario = 0
    while qtd_rodadas > 0:
        habilidade_jogador = int(input())
        habilidade_adversario = int(input())
        if habilidade_adversario > habilidade_jogador:
            pontos_adversario += 1
        else:
            pontos_jogador += 1
        qtd_rodadas = qtd_rodadas - 1
        if pontos_jogador >= (pontos_adversario + 5):
            qtd_partidas = 0
            qtd_rodadas = 0
    print(f'Fim de jogo! O placar foi {pontos_jogador}x{pontos_adversario}')
    if pontos_jogador >= (pontos_adversario + 5):
            print(f'QUE GOLEADAAAA!!! Essa vitória fez os outros times desistirem e a equipe de IP/P1 é a campeã!')
    elif pontos_jogador == pontos_adversario:
        qtd_partidas = 0
        print('Não foi dessa vez! Treinar pro ano que vem!')
        qtd_rodadas = 0
    else: 
        print("Vamos para próxima fase!")
        qtd_rodadas = qtd_rodadas - 1
    qtd_partidas = qtd_partidas - 1
    i = i + 1

#Ultima partida
if qtd_partidas == 1:
    qtd_rodadas = int(input())
    print(f'Tá na hora da grande final! Esse jogo terá {qtd_rodadas} rodada(s).')
    pontos_jogador = 0
    pontos_adversario = 0
    while qtd_rodadas > 0:
        habilidade_jogador = int(input())
        habilidade_adversario = int(input())
        if habilidade_adversario > habilidade_jogador:
            pontos_adversario += 1
        else:
            pontos_jogador += 1
        qtd_rodadas = qtd_rodadas - 1
    print(f'Fim de jogo! O placar foi {pontos_jogador}x{pontos_adversario}')
    if pontos_jogador <= pontos_adversario:
        print(f'Ah não!! Chegaram tão longe mas não foi dessa vez. :(')
        qtd_partidas = 0
    else:
        print('É CAMPEÃO! O TIME DE IP/P1 GARANTIU A TAÇA!')
