participantes = int(input())

if participantes > 0:
    nome =  input()
    pontos = int(input())
    penalidades = int(input())
    total = pontos - penalidades
    participantes -= 1
    
while participantes > 0:
    nome2 = input()
    pontos2 = int(input())
    penalidades2 = int(input())
    total2 = pontos2 - penalidades2
    if total < total2:
        nome = nome2
        total = total2
    participantes -= 1

print(f'O grande vencedor do torneio foi {nome} com um total de {total} pontos!')