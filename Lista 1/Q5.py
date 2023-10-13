caracteristica1 = input()
caracteristica2 = input()
nome = input()
habilidade = input()
nota1 = int(input())
nota2 = int(input())
nota3 = int(input())

if caracteristica1 == 'Humildade' and caracteristica2 == 'Bondade' and (nome == 'Mary' or nome == 'Ninguem') and (habilidade == 'Dancar' or habilidade == 'Lancar') and (nota1 + nota2 + nota3)/3 >= 7:
    print('Siga em frente, olhe para o lado. Bem-vindo ao aranhaverso, Miranha Furacao!')
else:
    print('Ops, parece que não foi dessa vez, Miranha. Você terá que continuar na Carreta Furacao mesmo!')

if caracteristica1 != 'Humildade' or caracteristica2 != 'Bondade':
    print('Infelizmente você não possui as característica necessárias!')
elif nome != 'Mary' and nome != 'Ninguem':
    print('Infelizmente você não está apaixonado pela pessoa certa!')
elif habilidade != 'Dancar' and habilidade != 'Lancar':
    print('Infelizmente você não possui as habilidades necessárias!')
elif (nota1 + nota2 + nota3)/3 < 7:
    print('Infelizmente você não obteve um bom desempenho escolar!')