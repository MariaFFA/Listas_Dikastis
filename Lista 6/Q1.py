qtd_famosos = int(input())
famosos = {}
famosos_fake = []

for _ in range(qtd_famosos):
    famoso = input()
    famoso = famoso.split(' - ')
    nome_famoso = famoso[0]
    famoso_caracteristica = famoso[1].split(' ')
    profissao = famoso_caracteristica[0]
    avaliação_famoso = famoso_caracteristica[1]
    mês_planejado = famoso_caracteristica[2]
    famosos[nome_famoso] = (profissao, avaliação_famoso, mês_planejado)

mês_escolhido = input()

for f in famosos:
    avaliação = famosos[f][1]
    mês = famosos[f][2]
    if famosos[f][1] == 'fake' and famosos[f][2] == mês_escolhido:
        famosos_fake.append(f)
famosos_fake = sorted(famosos_fake)

if famosos_fake != []:
    print('Os fake nattys do mês são:')
    for fake in famosos_fake:
        print(f'{fake} - {famosos[fake][0]}')
else:
    print('Até agora não temos ninguém pra expor na internet neste mês :(')
