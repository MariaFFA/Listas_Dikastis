nome_aluno = input()
nome_professor = input()

vitorias_aluno = 0
vitorias_professor = 0

print('E agora, só pela resenha:')
print(f'Melhor de 3 entre: {nome_aluno} e {nome_professor}!')
print('COMEÇOU!')

#partida
while vitorias_aluno < 2 and vitorias_professor < 2:
    pontos_aluno = 0
    pontos_professor = 0
    #rodada    
    while (pontos_aluno < 11 and pontos_professor < 11) or ((pontos_aluno >= 11 or pontos_professor >= 11) and diferença < 2): 
        num = int(input())
        if num % 2 == 0:
            pontos_professor += 1
        else:
            pontos_aluno += 1
        print(f'{pontos_aluno} - {pontos_professor}')
        diferença = abs(pontos_aluno - pontos_professor)
    if pontos_aluno > pontos_professor:
        vitorias_aluno += 1
        print(f'{nome_aluno} ganhou esta partida!')
    else: 
        vitorias_professor += 1
        print(f'{nome_professor} ganhou esta partida!')
    print(f'Placar: {nome_aluno} [{vitorias_aluno}-{vitorias_professor}] {nome_professor}')

#Acabou
print('FIM DA SÉRIE!')
if vitorias_aluno > vitorias_professor:
    vencedor = nome_aluno
    print(f'{nome_aluno} ganhou a série! Puro talento!')
else: 
    vencedor = nome_professor
    print(f'{nome_professor} ganhou a série! A experiência ganhou!')
