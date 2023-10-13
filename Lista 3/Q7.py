profissao_prevista = input()
profissao_dia = input()
ação = input()

lista_prevista = []
lista_dia = []

Medica = ['Estetoscopio', 'Esfigmomanometro', 'Jaleco', 'Caneta', 'Celular']
Assistente_Informatica = ['Calculadora', 'Oculos', 'Notebook', 'Camisa Social', 'Caderno']
Padeira = ['Rolo', 'Caneta', 'Avental', 'Colher de Pau', 'Caderno']
Economista = ['Calculadora', 'Caneta', 'Camisa Social', 'Agenda', 'Celular']
Personal_Trainer = ['Halter', 'Agenda', 'Celular', 'Legging', 'Corda']

#Associar lista a profissão
if profissao_prevista == 'Medica':
    lista_prevista = Medica
elif profissao_prevista == 'Assistente de Informatica':
    lista_prevista = Assistente_Informatica
elif profissao_prevista == 'Padeira':
    lista_prevista = Padeira
elif profissao_prevista == 'Economista':
    lista_prevista = Economista
elif profissao_prevista == 'Personal Trainer':
    lista_prevista = Personal_Trainer

if profissao_dia == 'Medica':
    lista_dia = Medica
elif profissao_dia == 'Assistente Informatica':
    lista_dia = Assistente_Informatica
elif profissao_dia == 'Padeira':
    lista_dia = Padeira
elif profissao_dia == 'Economista':
    lista_dia = Economista
elif profissao_dia == 'Personal Trainer':
    lista_dia = Personal_Trainer


while ação != 'Sair':
    #Adicionar
    if ação == 'Adicionar':
        item = input()
        if item not in lista_dia:
            print(f'Barbie, {item} não esta na lista de itens de {profissao_dia}')
        elif item in lista_prevista:
            print(f'Barbie, você já colocou {item} na bolsa')
        else:
            lista_prevista.append(item)
            print(f'{item} adicionado à bolsa')
    if ação == 'Retirar':
        item = input()
        if item not in lista_prevista:
            print(f'Barbie, como você vai retirar algo que já não esta ai?')
        elif item in lista_dia:
            print(f'Não faca isso Barbie, você precisa de {item} para trabalhar de {profissao_dia}')
        else:
            lista_prevista.remove(item)
            print(f'{item} retirado da bolsa')
    ação = input()
    
lista_prevista.sort()
lista_dia.sort()

#Listar itens
itens_bolsa = ', '.join(lista_prevista)
print(f'Itens na bolsa: {itens_bolsa}')

if lista_prevista == lista_dia:
    print('Boa Barbie, foi na correria mas tudo deu certo!')
for i in lista_prevista:
    if i not in lista_dia:
        print(f'Barbie, você esqueceu de tirar {i}, você não usa ele trabalhando de {profissao_dia}')
for i in lista_dia:
    if i not in lista_prevista:
        print(f'Oh não!! Barbie, você esqueceu de pegar {i}!!')
