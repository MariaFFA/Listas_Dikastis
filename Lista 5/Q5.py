quantidade_salas = int(input())
salas = []
moedas = 0
espada = False
salas_visitadas = []

def procurar(salas, sala_atual, moedas, espada, salas_visitadas):
    while '◇' in salas[sala_atual]:
        moedas += 1
        salas[sala_atual].remove('◇')
    if 'Zelda' in salas[sala_atual]:
        if espada == False and 'Agahnim' in salas[sala_atual]:
            return f"Infelizmente a princesa ainda corre perigo, mas temos {moedas} rupees para nos ajudar nas buscas"
        else:
            return f'A princesa Zelda está a salvo e ainda conseguimos coletar {moedas} rupees'
    elif sala_atual in salas_visitadas:
        return f"Infelizmente a princesa ainda corre perigo, mas temos {moedas} rupees para nos ajudar nas buscas"
    else:
        if 'Agahnim' in salas[sala_atual]:
            salas[sala_atual].remove('Agahnim')
        if 'espada' in salas[sala_atual]:
            espada = True
            salas[sala_atual].remove('espada')
        salas_visitadas.append(sala_atual)
        sala_atual = int(salas[sala_atual][0])
        return procurar(salas, sala_atual, moedas, espada, salas_visitadas)

for _ in range(quantidade_salas):
    sala = input()
    sala = sala.split(' - ')
    salas.append(sala)

sala_atual = int(input())

print(procurar(salas, sala_atual, moedas, espada, salas_visitadas))