fazer = input()
arara = 0
#Quantidade de profissoes e uniformes iguais
iguais = 0

while fazer != "Meninas, acho que já falei demais. Vamos para o shopping?":
    profissões_fora = []
    uniformes = input()
    uniformes = uniformes.split(', ')
    profissões = input()
    profissões = profissões.split(', ')
    print(f'Arara {arara}:')
    #numero de uniformes e profissões diferentes
    if len(uniformes) != len(profissões):
        print("Hmm, estranho! Acho que a Barbie se confundiu na organização e nas lembranças!")
    else:
    #profissões e uniformes iguais independente da ordem
        for u in uniformes:
            if u in profissões:
                iguais += 1
            else:
                profissões_fora.append(u)
        if iguais == len(uniformes):
            print("Boa, Barbie! Não bagunçou nada, pode contar todas as suas histórias!")
        else:
            #quantidades iguais, mas profissões diferentes
            total_nao_encontrados = len(profissões) - iguais
            print(f"Poxa, Barbie! Você acabou desorganizando essa arara, e {total_nao_encontrados} profissões vão ficar de fora da conversa. São elas: {', '.join(profissões_fora)}.")
    iguais = 0
    u = 0
    arara += 1
    fazer = input()
