nome_aranha = input()
ataque_aranha = int(input())
defesa_aranha = int(input())
nome_aliado = input()
ataque_aliado = int(input())
defesa_aliado = int(input())

nome_vilao = input()
ataque_vilao = int(input())
defesa_vilao = int(input())
nome_capanga = input()
ataque_capanga = int(input())
defesa_capanga = int(input())

fator_sorte = int(input())

pontos = 0
print('1° confronto:')
if fator_sorte == 0:
    if ataque_aranha >= defesa_vilao:
        vencedor = 'aranha'
    else:
        vencedor = 'vilao'
elif fator_sorte == 1:
    if ataque_aranha + ataque_aliado >= defesa_vilao:
        vencedor = 'aranha'
    else:
        vencedor = 'vilao'
elif fator_sorte == 2:
    if defesa_vilao + defesa_capanga >= ataque_aranha:
        vencedor = 'vilao'
    else:
        vencedor = 'aranha'
elif fator_sorte == 3:
    if defesa_vilao + defesa_capanga <= ataque_aranha + ataque_aliado:
        vencedor = 'aranha'
    else:
        vencedor = 'vilao'


if vencedor == 'aranha':
    print(f'O {nome_aranha} acertou vários golpes no {nome_vilao}')
    pontos += 1
else: 
    print(f'O {nome_vilao} está dificultando a vida do {nome_aranha}')

fator_sorte = int(input())
print('2° confronto:')
if fator_sorte == 0:
    if ataque_vilao > defesa_aranha:
        vencedor = 'vilao'
    else:
        vencedor = 'aranha'
elif fator_sorte == 1:
    if ataque_vilao + ataque_capanga >= defesa_aranha:
        vencedor = 'vilao'
    else:
        vencedor = 'aranha'
elif fator_sorte == 2:
    if defesa_aranha + defesa_aliado >= ataque_vilao:
        vencedor = 'aranha'
    else:
        vencedor = 'vilao'
elif fator_sorte == 3:
    if defesa_aranha + defesa_aliado < ataque_vilao + ataque_capanga:
        vencedor = 'vilao'
    else:
        vencedor = 'aranha'


if vencedor == 'aranha':
    print(f'O {nome_aranha} contra-atacou o {nome_vilao}')
    pontos += 1
else: 
    print(f'O {nome_aranha} não consegue se defender contra o {nome_vilao}')

fator_sorte = int(input())
print('3° confronto:')
if fator_sorte == 0:
    if ataque_aranha >= defesa_vilao:
        vencedor = 'aranha'
    else:
        vencedor = 'vilao'
elif fator_sorte == 1:
    if ataque_aranha + ataque_aliado >= defesa_vilao:
        vencedor = 'aranha'
    else:
        vencedor = 'vilao'
elif fator_sorte == 2:
    if defesa_vilao + defesa_capanga >= ataque_aranha:
        vencedor = 'vilao'
    else:
        vencedor = 'aranha'
elif fator_sorte == 3:
    if defesa_vilao + defesa_capanga <= ataque_aranha + ataque_aliado:
        vencedor = 'aranha'
    else:
        vencedor = 'vilao'


if vencedor == 'aranha':
    print(f'O {nome_aranha} acertou vários golpes no {nome_vilao}')
    pontos += 1
else: 
    print(f'O {nome_vilao} está dificultando a vida do {nome_aranha}')

if pontos >= 2:
    print(f'O {nome_aranha} e {nome_aliado} conseguiram derrotar o {nome_vilao} e recuperar o multiverso!')
else: 
    print(f'O {nome_vilao} e {nome_capanga} invadiram Nova York, onde estão os outros aranhas??')