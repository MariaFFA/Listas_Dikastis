max = input()
max_lista = max.split(' ; ')
max_objetos = int(max_lista[0])
max_custo = int(max_lista[1])

lista_objetos = []
lista_itens_objetos = []
lista_preço = []

ação = input()

while ação != "Fim! Muito obrigada pela ajuda!!":
    #Adicionar item
    if ação == "Quero adicionar um item":
        objeto = input()
        objeto_lista = objeto.split(' , ')
        item_filme = objeto_lista[0].split(' - ')
        item = item_filme[0]
        filme = item_filme[1]
        item_filme = item + ' - ' + filme
        preço = int(objeto_lista[1])
        if len(lista_objetos) < max_objetos and preço <= max_custo:
            max_custo -= preço
            print(f'Vá em frente, Ken! Você ainda tem {max_custo} barbieCoins disponíveis')
            lista_objetos.append(item_filme)
            lista_itens_objetos.append(item)
            lista_preço.append(preço)
        else:
            print('Avise a Barbie que isso não será possível.')
    #Remover item
    elif ação == "Quero remover um item":
        item = input()
        if item in lista_itens_objetos:
            for i in lista_itens_objetos:
                if item == i:
                    index_item = lista_itens_objetos.index(i)
            lista_objetos.pop(index_item)
            lista_itens_objetos.remove(item)
            max_custo += lista_preço[index_item]
            lista_preço.pop(index_item)
            print('Ok, Barbie!')
            print(f'Ken, você ainda tem {max_custo} barbieCoins disponíveis')
        else:
            print("Barbie, infelizmente não consegui fazer isso.")
    #Listar itens
    else: 
        if lista_objetos == []:
            print("Por enquanto seu museu está vazio, Barbie. Vamos trabalhar nisso!")
        else:
            print('Claro!')
            for itens in lista_objetos:  
                print(itens)
    ação = input()

print('Por nada! Estou sempre à disposição!')