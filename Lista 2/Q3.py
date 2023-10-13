garrafas = 20
frase = ''

while garrafas >= 0 and frase != 'O InterCIn acabou!!! Vamos verificar nosso estoque de bebidas':    
    frase = input()
    #Partida acabou
    if frase == 'Acabou uma partida e precisamos da seguinte quantidade de garrafas para matar a sede dos jogadores':
        jogadores = int(input())
        #Garrafas insuficientes
        if garrafas - jogadores < 0 :
            print(f'Não teremos água para todos os jogadores... Temos que garantir {(garrafas - jogadores) * (-1)} garrafas!!')
            garrafas = 2 * garrafas
            #Garrafas continuam insuficientes
            if garrafas - jogadores < 0 :
                print('Por questões logísticas, teremos que acabar com os jogos...')
            garrafas -= jogadores
        else: 
            garrafas -= jogadores
    #Encher Cooler
    elif frase == 'Encham o cooler! O jogo vai começar!!!!':
        garrafas += 15
        print('Geladeira cheia!')
    #Timeout
    elif frase == 'Timeout da partida! Verifiquem quantas garrafas pediram aos voluntários':
        quantidade_1 = int(input())
        quantidade_2 = int(input())
        quantidade_3 = int(input())
        quantidade_4 = int(input())
        quantidade_5 = int(input())
        garrafas -= (quantidade_1 + quantidade_2 + quantidade_3 + quantidade_4 + quantidade_5)
        #Acabaram as garrafas
        if garrafas < 0:
            print(f'Faltaram {(garrafas) * (-1)} garrafas para atender o pedido feito aos voluntários')
            print('Por questões logísticas, teremos que acabar com os jogos...')

#InterCin acabou
if garrafas > 0:
    print(f'Sobraram {garrafas} garrafas, vamos guardar na geladeira :D')
elif frase == 'O InterCIn acabou!!! Vamos verificar nosso estoque de bebidas':
    print('Vendemos todas as garrafas! Nosso planejamento foi perfeito!')