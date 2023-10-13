#Se é fake ou não
def natty_ou_fake(nome,pessoas):
    quesitos = 0
    seco = 0
    for c in pessoas[nome]:
        if 'Suor:' not in c:
            seco += 1
    if seco == len(pessoas[nome]):
        quesitos += 1
    for c in pessoas[nome]:
        if c[0] == 'Biceps:' and c[1] > 45:
            quesitos += 1
        elif c[0] == 'Treino:' and c[1] < 30:
            quesitos += 1
        elif c[0] == 'Frequencia:' and c[1] < 4:
            quesitos += 1
        elif c[0] == 'BF:' and c[1] < 10:
            quesitos += 1
        elif c[0] == 'Suor:' and (c[1] != 'Suado' and c[1] != 'Muito Suado' and c[1] != 'Encharcado'):
            quesitos += 1
    if quesitos >= 3:
        return 'FAKE NATTY'
    else:
        return 'natural'

ação = input()
pessoas = {}

while ação != 'FIM':
    #Adicionar
    if ação == 'Adicionar suspeito':
        nome = input()
        print(f'Novo suspeito: {nome}')
        pessoas[nome] = []
    #Atualizar
    elif ação == 'Atualizar suspeito':
        nome_caracteristicas = input()
        nome_caracteristicas = nome_caracteristicas.split('-> ')
        nome = nome_caracteristicas[0]
        if nome in pessoas:
            caracteristicas = nome_caracteristicas[1]
            caracteristicas = caracteristicas.split(', ')
            for cv in caracteristicas:
                index = caracteristicas.index(cv)
                caracteristica_valor = caracteristicas[index].split(' ')
                if caracteristica_valor[0] == 'BF:':
                    caract = list(caracteristica_valor[1])
                    caract.pop(-1)
                    caracteristica_valor[1] = ''.join(caract)
                    valor = int(caracteristica_valor[1])
                elif caracteristica_valor[0] == 'Biceps:':
                    caract = list(caracteristica_valor[1])
                    caract.pop(-1)
                    caract.pop(-1)
                    caracteristica_valor[1] = ''.join(caract)
                    valor = int(caracteristica_valor[1])
                elif caracteristica_valor[0] == 'Treino:':
                    valor = int(caracteristica_valor[1])
                    if caracteristica_valor[2] == 'segundos'or caracteristica_valor[2] == 'segundo':
                        valor = valor/60
                    elif caracteristica_valor[2] == 'horas' or caracteristica_valor[2] == 'hora':
                        valor = valor*60
                elif caracteristica_valor[0] == 'Frequencia:':
                    valor = int(caracteristica_valor[1])
                else:
                    valor = ' '.join(caracteristica_valor[1:])
                caracteristica = caracteristica_valor[0]
                todas_caracteristicas = []
                #Verificar se vai substituir ou acrescentar
                for c in pessoas[nome]:
                    if c[0] == caracteristica:
                        index = pessoas[nome].index(c)
                        pessoas[nome][index] = (caracteristica, valor)
                    todas_caracteristicas.append(c[0])
                if caracteristica not in todas_caracteristicas:
                    pessoas[nome].append((caracteristica, valor))
        else:
            print('Quem é esse crazy man? Não tá aqui na database')
    #Remover
    elif ação == 'Remover suspeito':
        nome = input()
        if nome in pessoas:
            print(f'{nome} removido da lista de suspeitos, está limpo')
            pessoas.pop(nome)
        else:
            print('Quem é esse crazy man? Não tá aqui na database')
    #Julgamento
    elif ação == 'Julgamento':
        nome = input()
        if nome in pessoas:
            print(f'Eu já tenho o meu veredito, e o meu veredito, {nome}:')
            resultado = natty_ou_fake(nome,pessoas)
            if resultado == 'natural':
                print('Natural')
            else:
                print('FAKE NATTY! USOU O SUCO!')
        else:
            print('Quem é esse crazy man? Não tá aqui na database')
    #NattyMeter
    else:
        natural = 0
        fake = 0
        for p in pessoas:
            if natty_ou_fake(p,pessoas) == 'natural':
                natural += 1
            else:
                fake +=1
        print('NattyMeter, ON!')
        if fake == 0:
            print('Oh yeah, vivemos em uma sociedade sem suco, um great day')
        else:
            print(f'NOOO! {int((fake/(fake+natural))*100)}% USARAM O SUCO')
    ação = input()
