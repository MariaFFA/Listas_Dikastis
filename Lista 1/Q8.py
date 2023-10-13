dica = int(input())

if dica % 2 == 0:
    numero_caracteres = int((dica/2)**(1/2) + 2)
else:
    numero_caracteres = int(dica/3 + 3)

filme1 = input()
filme2 = input()
filme3 = input()

if filme1 == 'Coringa' or filme1 == 'Batman vs Superman' or filme1 == 'O Cavaleiro das Trevas':
    print('Algo de errado não está certo!')

else:
    nivel_cansaço = 0
    if numero_caracteres == len(filme1):
        nivel_cansaço += 1
    elif numero_caracteres == len(filme2):
        nivel_cansaço += 2
    elif numero_caracteres == len(filme3):
        nivel_cansaço += 3

    if filme1 == 'Vingadores: Ultimato':
        nivel_cansaço += 1
    elif filme2 == 'Vingadores: Ultimato':
        nivel_cansaço += 2
    elif filme3 == 'Vingadores: Ultimato':
        nivel_cansaço += 3
    
    duracao = 120
    if numero_caracteres == len(filme1) or numero_caracteres == len(filme2) or numero_caracteres == len(filme3):
        nome_filme = input()
        duracao = int(input())
    
    achou = ''
    if len(filme1) != numero_caracteres:
        print("Miles: Tou frio, melhor ir procurar nas fases mais antigas")
        if len(filme2) != numero_caracteres:
            print('Gwen: Cadê o velho??? Queria um autógrafo')
            if len(filme3) != numero_caracteres:
                print('Peter: Parece que o próximo filme do aranha-verso vai demorar mais do que esperado pra sair...')
            else:
                achou = 'Miles: Achei o easter egg!!!'
                print(achou)
        else:
            achou = 'Miles: Achei o easter egg!!!'
            print(achou)
    else:
        achou = 'Miles: Achei o easter egg!!!'
        print(achou)

    if achou == 'Miles: Achei o easter egg!!!' and nivel_cansaço >= 2 and duracao >= 135:
        print('Miles: A mimir')
    elif achou == 'Miles: Achei o easter egg!!!' and nivel_cansaço >= 2 and 120 <= duracao < 135:
        print('Gwen: Nada que uma xícara de café não resolva!')
    elif achou == 'Miles: Achei o easter egg!!!' and nivel_cansaço < 2 or duracao < 120:
        print(f'Peter: {nome_filme} é o melhor filme do homem aranha, 10/10')