n = int(input())

for l in range(n):
    coleções = input()
    coleções = coleções.split(', ')
    notas = input()
    notas = notas.split(', ')
    #Peças descartadas
    if 'colete preto' in coleções:
        print("colete preto é uma peça muito gótica, não faz o estilo da Glimmer.")
        l = len(notas) 
    elif 'coturno' in coleções:
        print("coturno é uma peça muito gótica, não faz o estilo da Glimmer.")
        l = len(notas)
    elif 'vestido com babados' in coleções:
        print("vestido com babados é uma peça muito antiquada, infelizmente essa coleção não vai servir...")
        l = len(notas)
    elif 'blusa bufante' in coleções:
        print("blusa bufante é uma peça muito antiquada, infelizmente essa coleção não vai servir...")
        l = len(notas)
    else: 
        #Por notas
        soma_nota = 0
        for nota in notas:
            soma_nota += int(nota)
        media_notas = soma_nota/len(notas)
        if media_notas < 6:
            print("Até que as peças são bonitinhas, mas não o bastante. Essa coleção não vai servir.")
        else:
            print("Que coleção linda! Com certeza vai ajudar Glimmer a se inspirar.")

