vida_maxima_venom = int(input())
ataque_venom = int(input())
pocao_venom = int(input())

vida_creeper = int(input())

#turno 1
print('SENHORAS E SENHORES! AGORA O VENOM ENFRENTARÁ O CREEPER!')

vida_venom = vida_maxima_venom - ataque_venom
vida_creeper = vida_creeper - ataque_venom

vencedor = ''
if vida_venom <= 0:
    print('O venom não tankou e foi de base...')
    vencedor = 'creeper'
    if vida_creeper <= 0:
        print('O creeper não tankou e foi de base...')
    print('AH NÃO! O VENOM PEGOU EM BOMBA!')
    print('Pelo visto as aventuras do Miles terminaram por aqui...')
elif vida_creeper <= 0:
    print('O creeper não tankou e foi de base...')
    vencedor = 'venom'
    print('Isso aí! Ele é todo esquentadinho, mas no final deu tudo certo!')
else:
    print(f'Vida atual do Venom: {vida_venom}')
    print(f'Dano sofrido pelo Venom: {ataque_venom}')
    print(f'Vida atual do creeper: {vida_creeper}')
    print(f'Dano sofrido pelo creeper: {ataque_venom}')
    if vida_creeper < vida_venom:
        vencedor = 'venom'
        print('Isso aí! Ele é todo esquentadinho, mas no final deu tudo certo!')
    else:
        vencedor = 'creeper'
        print('AH NÃO! O VENOM PEGOU EM BOMBA!')
        print('Pelo visto as aventuras do Miles terminaram por aqui...')

if vida_maxima_venom - vida_venom >= pocao_venom and vencedor == 'venom':
    vida_venom = vida_venom + pocao_venom
    print('Ah! Essa poção é da boa!')

#turno 2
if vencedor == 'venom':
    print('SENHORAS E SENHORES! AGORA O VENOM ENFRENTARÁ O DRUIDA!')
    vida_druida = int(input())
    ataque_druida = int(input())
    vida_venom = vida_venom + pocao_venom
    if vida_venom > vida_maxima_venom:
        taxa_envenenamento = vida_venom - vida_maxima_venom
        vida_venom = vida_venom - taxa_envenenamento
        ataque_druida = ataque_druida + taxa_envenenamento
    vida_venom -= ataque_druida
    vida_druida -= ataque_venom
    if vida_venom <= 0:
        print('O venom não tankou e foi de base...')
        if vida_creeper <= 0:
          print('O druida não tankou e foi de base...')
        print('Pelo visto a poção tava fora do prazo de validade :(')
        print('Pelo visto as aventuras do Miles terminaram por aqui...')
    elif vida_druida <=0:
        print('O druida não tankou e foi de base...')
        print('Quase me dei mal, nunca mais aceito nada de estranho...')
        print('Essa aventura foi epicamente épica, meu amigo! Boa viagem aí! * Começa a tocar saxofone *')
    else:
        print(f'Vida atual do Venom: {vida_venom}')
        print(f'Dano sofrido pelo Venom: {ataque_druida}')
        print(f'Vida atual do druida: {vida_druida}')
        print(f'Dano sofrido pelo druida: {ataque_venom}')
        if ataque_venom > ataque_druida:
            print('Quase me dei mal, nunca mais aceito nada de estranho...')
            print('Essa aventura foi epicamente épica, meu amigo! Boa viagem aí! * Começa a tocar saxofone *')
        elif ataque_venom < ataque_druida:
            print('Pelo visto a poção tava fora do prazo de validade :(')
            print('Pelo visto as aventuras do Miles terminaram por aqui...')
        else:
            if vida_venom > vida_druida:
                print('Quase me dei mal, nunca mais aceito nada de estranho...')      
                print('Essa aventura foi epicamente épica, meu amigo! Boa viagem aí! * Começa a tocar saxofone *')
            else:
                print('Pelo visto a poção tava fora do prazo de validade :(')
                print('Pelo visto as aventuras do Miles terminaram por aqui...')