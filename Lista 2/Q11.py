jogadores = 5  
#Verificar dependencia
artur = 0
frej = 0

while jogadores > 0:
    nome = input()
    if nome == 'Bruna':
        print("LOL NÃO!!! TUDO MENOS LOL!!!")
        jogadores = 0
    else:
        lane = input()
        elo = input()
        #Pontuação por elo
        if elo == 'Bronze':
            pontos = 1
        elif elo == 'Prata':
            pontos = 2
        elif elo == 'Ouro':
            pontos = 4
        elif elo == 'Platina':
            pontos = 6
        elif elo == 'Diamante':
            pontos = 8
        elif elo == 'Desafiante':
            pontos = 10
        else:
            pontos = 0
            print("Não conheço esse elo, então vou considerar que é um elo ruim.")
        #Jogadores com lanes diferentes, logo entraram na equipe
        if jogadores == 5:
            nome5 = nome
            lane5= lane
            elo5 = elo
            pontos5 = pontos
            print(f'{nome} entrou pro time.')
            if nome == 'Artur':
                print("Ele tá meio enferrujado...")
                artur += 1
            if nome == 'Frej':
                print("Joga muito!")
                frej += 1
            jogadores -= 1
        elif jogadores == 4 and lane != lane5:
            nome4 = nome
            lane4= lane
            elo4 = elo
            pontos4 = pontos
            print(f'{nome} entrou pro time.')
            if nome == 'Artur':
                print("Ele tá meio enferrujado...")
                artur += 1
            if nome == 'Frej':
                print("Joga muito!")
                frej += 1
            jogadores -= 1
        elif jogadores == 3 and lane != lane5 and lane != lane4:
            nome3 = nome
            lane3= lane
            elo3 = elo
            pontos3 = pontos
            print(f'{nome} entrou pro time.')
            if nome == 'Artur':
                print("Ele tá meio enferrujado...")
                artur += 1
            if nome == 'Frej':
                print("Joga muito!")
                frej += 1
            jogadores -= 1
        elif jogadores == 2 and lane != lane5 and lane != lane4 and lane != lane3:
            nome2 = nome
            lane2= lane
            elo2 = elo
            pontos2 = pontos
            print(f'{nome} entrou pro time.')
            if nome == 'Artur':
                print("Ele tá meio enferrujado...")
                artur += 1
            if nome == 'Frej':
                print("Joga muito!")
                frej += 1
            jogadores -= 1
        elif jogadores == 1 and lane != lane5 and lane != lane4 and lane != lane3 and lane != lane2:
            nome1 = nome
            lane1= lane
            elo1 = elo
            pontos1 = pontos
            print(f'{nome} entrou pro time.')
            if nome == 'Artur':
                print("Ele tá meio enferrujado...")
                artur += 1
            if nome == 'Frej':
                print("Joga muito!")
                frej += 1
            jogadores -= 1
        else:
            print(f"{nome} não foi aceito, que pena.")


if nome != 'Bruna':
    #Pontuação da equipe
    pontos_equipe = pontos1 + pontos2 + pontos3 + pontos4 + pontos5

    #Time
    print("O time está completo.")
    print(f'{nome5} - {lane5} ({elo5})')
    print(f'{nome4} - {lane4} ({elo4})')
    print(f'{nome3} - {lane3} ({elo3})')
    print(f'{nome2} - {lane2} ({elo2})')
    print(f'{nome1} - {lane1} ({elo1})')

    #Resultado
    if (nome1 != 'Frej' or nome2 != 'Frej' or nome3 != 'Frej' or nome4 != 'Frej' or nome5 != 'Frej') and (nome1 == 'Artur' or nome2 == 'Artur' or nome3 == 'Artur' or nome4 == 'Artur' or nome5 == 'Artur') and artur < 2 and frej < 2:
       pontos_equipe = 0
    #Com Frej e sem Artur
    elif (nome1 == 'Frej' or nome2 == 'Frej' or nome3 == 'Frej' or nome4 == 'Frej' or nome5 == 'Frej') and (nome1 != 'Artur' or nome2 != 'Artur' or nome3 != 'Artur' or nome4 != 'Artur' or nome5 != 'Artur') and artur < 2 and frej < 2:
       pontos_equipe = 20
    
      #Resultado
    if pontos_equipe >= 18:
        print("A GENTE VAI GANHAR!!!")
    else:
        print("Vai dar ruim...")
