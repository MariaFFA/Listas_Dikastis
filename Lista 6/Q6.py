def tri_grama(frase):
    lista = []
    frase = list(frase)
    while len(frase) >=3:
        tri = frase[0:3]
        tri = ''.join(tri)
        lista.append(tri)
        frase.pop(0)
    if len(frase) > 0:
        frase = ''.join(frase)
        lista.append(frase)
    return lista

frase = input()
frases = []
dicionario = {}
linha = 0

while frase != "END_OF_FILE":
    frase = frase.lower()
    dicionario[linha] = tri_grama(frase)
    linha += 1
    
    frases.append(frase)
    frase = input()

pesquisas = int(input())

for i in range(pesquisas):
    resultado = -1
    busca_completa = input()
    busca_completa = busca_completa.lower()
    busca = busca_completa[0:3]
    for t in dicionario:
        if busca in dicionario[t] and resultado == -1:
            if busca_completa in frases[t]:
                resultado = t
    print(resultado)
    