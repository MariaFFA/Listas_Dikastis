jogos = int(input())

pontos_mancherster_cin = 0
pontos_spicin_girls = 0

while jogos > 0:
    nome = input()
    gols = int(input())
    chutes_ao_gol = int(input())
    cartões_amarelos = int(input())
    cartões_vermelhos = int(input())
    #Vez de Manchester CIn
    if nome == 'Manchester CIn':
        pontos_mancherster_cin = pontos_mancherster_cin + (gols * 10)+(chutes_ao_gol * 3)-(cartões_amarelos*2)-(cartões_vermelhos*4)
        #Verificação
        if gols >= (30*(chutes_ao_gol)/100):
            pontos_mancherster_cin += 3
        #Verificação
        if cartões_vermelhos >= cartões_amarelos:
            pontos_mancherster_cin -= 3
    #Vez de SpiCIn Girls
    elif nome == 'SpiCIn Girls':
        pontos_spicin_girls = pontos_spicin_girls + (gols * 10)+(chutes_ao_gol * 3)-(cartões_amarelos*2)-(cartões_vermelhos*4)
        #Verificação
        if gols >= (30*(chutes_ao_gol)/100):
            pontos_spicin_girls += 3
        #Verificação
        if cartões_vermelhos >= cartões_amarelos:
            pontos_spicin_girls -= 3
    #Casos negativos
    if pontos_mancherster_cin < 0:
        print("O time Manchester CIn ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.")
        jogos = 0
    if pontos_spicin_girls < 0:
        print("O time SpiCIn Girls ficou com pontuação negativa. A aposta não é segura, podemos perder nosso dinheiro.")
        jogos = 0
    jogos = jogos - 1

#Casos não negativos
if pontos_mancherster_cin >= 0 and pontos_spicin_girls >= 0:
    if pontos_mancherster_cin > pontos_spicin_girls:
        print(f'Com {(pontos_mancherster_cin/(pontos_mancherster_cin + pontos_spicin_girls)*100):.2f}% dos pontos, o time Manchester CIn pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.')
    elif pontos_mancherster_cin < pontos_spicin_girls:
        print(f'Com {(pontos_spicin_girls/(pontos_mancherster_cin + pontos_spicin_girls)*100):.2f}% dos pontos, o time SpiCIn Girls pode garantir nosso dinheiro na CInBet, é uma das grandes apostas do InterCIn.')