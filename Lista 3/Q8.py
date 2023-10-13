#Opções
opções_penteados = input()
opções_tops = input()
opções_bottoms = input()
opções_sapatos = input()

penteados = opções_penteados.split(' - ')
tops = opções_tops.split(' - ')
bottoms = opções_bottoms.split(' - ')
sapatos = opções_sapatos.split(' - ')

print('Triagem das peças realizada com sucesso, pronta para iniciar mesclagem!')

#Foco
if len(penteados) % 2 == 0:
    foco_penteados = int(len(penteados)/2)
else:
    foco_penteados = len(penteados) // 2
if len(tops) % 2 == 0:
    foco_tops = int(len(tops)/2)
else:
    foco_tops = len(tops) // 2
if len(bottoms) % 2 == 0:
    foco_bottoms = int(len(bottoms)/2)
else:
    foco_bottoms = len(bottoms) // 2
if len(sapatos) % 2 == 0:
    foco_sapatos = int(len(sapatos)/2)
else:
    foco_sapatos = len(sapatos) // 2

decisao = 'Acho que não combinou muito :/'

while decisao == 'Acho que não combinou muito :/':
    #Direção
    direção = input()
    direção = direção.split(' ')
    vezes = []
    sentido = []
    for i in direção:
        vezes_sentido = list(i)
        numero = ''.join(vezes_sentido[:(len(vezes_sentido)-1)])
        vezes.append(int(numero))
        sentido.append(vezes_sentido[(len(vezes_sentido)-1)])

    print('Iniciando mesclagem...')

    #Rodando penteados
    if sentido[0] == '<':
            for _ in range(int(vezes[0])):
                foco_penteados -=1
                if foco_penteados < 0:
                    foco_penteados = len(penteados) - 1
    elif sentido[0] == '>':
            for _ in range(int(vezes[0])):
                foco_penteados +=1
                if foco_penteados >= len(penteados):
                    foco_penteados = 0

    #Rodando tops
    if sentido[1] == '<':
            for _ in range(int(vezes[1])):
                foco_tops -=1
                if foco_tops < 0:
                    foco_tops = len(tops) - 1
    elif sentido[1] == '>':
            for _ in range(int(vezes[1])):
                foco_tops +=1
                if foco_tops >= len(tops):
                    foco_tops = 0

    #Rodando bottoms
    if sentido[2] == '<':
            for _ in range(int(vezes[2])):
                foco_bottoms -=1
                if foco_bottoms < 0:
                    foco_bottoms = len(bottoms) - 1
    elif sentido[2] == '>':
            for _ in range(int(vezes[2])):
                foco_bottoms +=1
                if foco_bottoms >= len(bottoms):
                    foco_bottoms = 0

    #Rodando sapatos
    if sentido[3] == '<':
            for _ in range(int(vezes[3])):
                foco_sapatos -=1
                if foco_sapatos < 0:
                    foco_sapatos = len(sapatos) - 1
    elif sentido[3] == '>':
            for _ in range(int(vezes[3])):
                foco_sapatos +=1
                if foco_sapatos >= len(sapatos):
                    foco_sapatos = 0

    print('O look gerado foi:')
    print(f'cabelo {penteados[foco_penteados]}, {tops[foco_tops]} com {bottoms[foco_bottoms]} e {sapatos[foco_sapatos]} nos pés.')
    decisao = input()


if decisao == 'Amei!!':
    if tops[foco_tops] == 'camisa da seleção':
        print('Essa Barbie vai torcer pela seleção feminina na copa do mundo 2023!')
    else:
        print('Essa Barbie vai arrasar com o look perfeito!')
else:
    print('Acho que estou precisando de ajustes, Ken :(')