lista_desejo = input()
lista_desejo = lista_desejo.split(', ')
lista_casa = input()
lista_casa = lista_casa.split(', ')
n = 0
l = 0

#Quantidade de itens faltando
for i in lista_desejo:
    if i not in lista_casa:
         n +=1

#Faltando tudo
if n == len(lista_desejo):
    print(f"Nossa, irei ao shopping agora mesmo! Não tenho nenhum dos {n} itens em casa.")
#Faltando alguma coisa
else:
    print('Esses são os itens que já tenho em casa:')
    for item in lista_desejo:
        if item in lista_casa:
            l += 1
            print(f'{l}º item: {item}')
#faltando nada
    if n == 0:
        print(f"Que ótimo, consegui encontrar cada um dos {len(lista_desejo)} itens!")
    else:
         print(f"Irei precisar comprar {n} itens antes do meu encontro!")      

print("Isso é tudo! Hora de me preparar!")