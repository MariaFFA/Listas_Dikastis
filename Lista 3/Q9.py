tempo_ideal = int(input())
entradas = int(input())
posições = []
tempos = []
tempo_total = 0
selecionadas = []

#Separar posições e tempos em listas
for _ in range(entradas):
    treino = input()
    treino_tempo = treino.split(' ')
    posições.append(treino_tempo[0])
    tempos.append(treino_tempo[1])

ultimo = 0
#Testando todas as posibilidades se sublistas
while ultimo < len(tempos):
    começo = 0
    while começo <= ultimo:
        tempo_temporario = []
        p = ultimo - começo
        for _ in range(p+1):
            tempo_temporario.append(int(tempos[_+começo]))
            tempo_total_temporario = sum(tempo_temporario)
            if tempo_total_temporario == tempo_ideal:
                tempo_total = tempo_ideal
                selecionadas = posições[começo:ultimo+1]
                começo = len(tempos)
                ultimo = len(tempos)


        começo +=1          
    ultimo +=1
#Conclusão
if tempo_total == tempo_ideal:
    posições_selecionadas = ' '.join(selecionadas)
    print(f'Conquistamos nossa primeira estrela! Barbie e Chelsea arrasaram nos treinos das {posições_selecionadas}!')
else:
    print('Não treinamos na dose certa e infelizmente a estrela vai ter que ficar para a próxima')