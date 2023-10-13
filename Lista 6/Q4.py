#Dicionario do alfabeto(a-z)
alfabeto = {0 : 'a', 1 : 'b', 2 : 'c', 3 : 'd', 4 : 'e', 5 : 'f', 6 : 'g', 7 : 'h', 8 : 'i', 9 : 'j', 10 : 'k', 11 : 'l', 12 : 'm', 13 : 'n', 14 : 'o', 15 : 'p', 16 : 'q', 17 : 'r', 18 : 's', 19 : 't', 20 : 'u', 21 : 'v',  22 : 'w', 23 : 'x', 24 : 'y', 25 : 'z'}

linhas = int(input())
possibilidades = []
ocorrencias = 0

#Todas as possibilidades
for _ in range(linhas):
    string = input()
    string = list(string)
    index = string.index('_')
    for i in alfabeto:
        string[index] = alfabeto[i]
        string_possivel = ''.join(string)
        possibilidades.append(string_possivel)

#Colocar em ordem alfabetica
possibilidades = sorted(possibilidades)

#Descobrir maior ocorrencia
for s in possibilidades:
    string_ocorrencia = possibilidades.count(s)
    if string_ocorrencia > ocorrencias:
        ocorrencias = string_ocorrencia
        string_fake = s

print(f'{string_fake} {ocorrencias}')