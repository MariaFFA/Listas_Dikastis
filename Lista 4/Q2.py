qtd_desclassificados = 0
qtd_classificados = 0
situações = ''

#Alterando quantidade de propulsores
def qtd_propulsores(situações):
    if situações == 'Pit-Stop Espacial':
        return 1
    elif situações == 'Um Droide apareceu do nada na pista, do nadaaa! Perdi o controle e bati em uma pedra.':
        return -1
    
#Relatorio
def relatorio(nome,qtd_propulsores_final,velocidade_propulsor,qtd_propulsores_inicial):
    print(f'--- Participante: {nome} ---')
    print(f'Qtd de propulsores Final: {qtd_propulsores_final}')
    print(f'Velocidade Inicial: {velocidade_propulsor * qtd_propulsores_inicial} km/h')
    print(f'Velocidade Final: {velocidade_propulsor * qtd_propulsores_final} km/h')

#Informações
informações = input()
informações = informações.split(' ')
nome = informações[0]
qtd_propulsores_inicial = int(informações[1])
velocidade_propulsor = int(informações[2])
qtd_propulsores_final = qtd_propulsores_inicial
situações = input()

while situações != 'FIM':    
        #Alterando quantidade de propulsores
        while (situações == 'Pit-Stop Espacial' or situações == 'Um Droide apareceu do nada na pista, do nadaaa! Perdi o controle e bati em uma pedra.') and qtd_propulsores_final != 0:
            qtd_propulsores_final += qtd_propulsores(situações)
            if qtd_propulsores_final == 0:
                print(f'BUUMM!! Infelizmente, {nome} está fora da corrida.')
                qtd_desclassificados +=1
                qtd_classificados -= 1
            else:
                situações = input()
                if situações == 'FIM':
                    relatorio(nome,qtd_propulsores_final,velocidade_propulsor,qtd_propulsores_inicial)
        #Participande não inscrito
        if situações == 'Opa esse participante tem ID de Droide, desclassificando em 3, 2, 1...':
            print(f'O {nome} achou que não descobriríamos, tirem {nome} imediatamente da pista.')
            qtd_desclassificados += 1
            qtd_classificados -= 1
        elif situações == 'Próximo':
            relatorio(nome,qtd_propulsores_final,velocidade_propulsor,qtd_propulsores_inicial)
        qtd_classificados += 1
        if situações != 'FIM':
            #Informações
            informações = input()
            if informações == 'FIM':
                situações = 'FIM'
            else:
                informações = informações.split(' ')
                nome = informações[0]
                qtd_propulsores_inicial = int(informações[1])
                velocidade_propulsor = int(informações[2])
                qtd_propulsores_final = qtd_propulsores_inicial
                situações = input()


#Conclusão
if qtd_classificados == 0:
    print('NÃO! Esses Droides me pagam, sabotaram minha corrida!')
else:
    print(f'Relatório da CIn Pod Race: {qtd_classificados} participantes terminaram a corrida e {qtd_desclassificados} foram desclassificados.')
