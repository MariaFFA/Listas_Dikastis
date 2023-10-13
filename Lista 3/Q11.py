voceY = int(input())
voceX = int(input())
cambistaY = int(input())
cambistaX = int(input())
pipocaY = int(input())
pipocaX = int(input())
barbieY = int(input())
barbieX = int(input())
oppenheimerY = int(input())
oppenheimerX = int(input())

chegou = 'nada'
pode_movimentar = 'sim'
pipoca = 'nao'
linha1 = ['-', '-', '-', '-','-', '-', '-', '-']
linha2 = ['-', '-', '-', '-','-', '-', '-', '-']
linha3 = ['-', '-', '-', '-','-', '-', '-', '-']
linha4 = ['-', '-', '-', '-','-', '-', '-', '-']
linha5 = ['-', '-', '-', '-','-', '-', '-', '-']
linha6 = ['-', '-', '-', '-','-', '-', '-', '-']
linha7 = ['-', '-', '-', '-','-', '-', '-', '-']
linha8 = ['-', '-', '-', '-','-', '-', '-', '-']
matrix = [
    linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8
]

#Matriz inicial
matrix[voceY][voceX] = 'V'
matrix[cambistaY][cambistaX] = 'C'
matrix[pipocaY][pipocaX] = 'P'
matrix[barbieY][barbieX] = 'B'
matrix[oppenheimerY][oppenheimerX] = 'O'

while chegou != 'barbie' and chegou != 'oppenheimer' and chegou != 'cambista':
    #Movimento do cambista
    if voceX == cambistaX and voceY == cambistaY:
        chegou = 'cambista'
        #Impriminto a matrix
        matrix_linhas = []
        for l in range(8):
            linha = ''.join(matrix[l])
            matrix_linhas.append(linha)
        for c in range(8):
            coluna = ' '.join(matrix_linhas[c])
            print(coluna) 
        print('Droga! Agora volto pra casa sem filme e sem dinheiro.')
    elif voceX == cambistaX and voceY != cambistaY:
        if voceY > cambistaY:
            matrix[cambistaY][cambistaX] = '-'
            cambistaY +=1
            matrix[cambistaY][cambistaX] = 'C'
        elif voceY < cambistaY:
            matrix[cambistaY][cambistaX] = '-'
            cambistaY -=1
            matrix[cambistaY][cambistaX] = 'C'
    else:
        if voceX > cambistaX:
            matrix[cambistaY][cambistaX] = '-'
            cambistaX +=1
            matrix[cambistaY][cambistaX] = 'C'
        elif voceX < cambistaX:
            matrix[cambistaY][cambistaX] = '-'
            cambistaX -=1
            matrix[cambistaY][cambistaX] = 'C'
    
    if matrix[voceY][voceX] != matrix[cambistaY][cambistaX]:
        movimento = input()
        #Movimendo de Você
        if pode_movimentar == 'sim':
            if movimento == 'esquerda':
                matrix[voceY][voceX] = '-'
                voceX -=1
                matrix[voceY][voceX] = 'V'
            elif movimento == 'direita':
                matrix[voceY][voceX] = '-'
                voceX +=1
                matrix[voceY][voceX] = 'V'
            elif movimento == 'cima':
                matrix[voceY][voceX] = '-'
                voceY -=1
                matrix[voceY][voceX] = 'V'
            elif movimento == 'baixo':
                matrix[voceY][voceX] = '-'
                voceY +=1
                matrix[voceY][voceX] = 'V'
        else:
            pode_movimentar = 'sim'

    if matrix[voceY][voceX] != matrix[cambistaY][cambistaX]:
        #Impriminto a matrix
        matrix_linhas = []
        for l in range(8):
            linha = ''.join(matrix[l])
            matrix_linhas.append(linha)
        for c in range(8):
            coluna = ' '.join(matrix_linhas[c])
            print(coluna)    
        
        if matrix[voceY][voceX] == matrix[barbieY][barbieX]:
            chegou = 'barbie'
            if pipoca == 'nao':
                print('Ah não, vou passar fome! Não tem nem graça assistir filme sem uma pipoquinha.')
            else:
                print('A Margot Robbie está incrível, mas que barulho é esse vindo da sala do lado?')
        elif matrix[voceY][voceX] == matrix[oppenheimerY][oppenheimerX]:
            chegou = 'oppenheimer'
            if pipoca == 'nao':
                print('Ah não, vou passar fome! Não tem nem graça assistir filme sem uma pipoquinha.')
            else:
                print('Aí sim, que filmaço! Christopher Nolan nunca erra!')
        else:
            #Pipoca de você
            if pipoca == 'sim':
                print('Já peguei a pipoca')
            elif matrix[pipocaY][pipocaX] == 'V':
                pipoca = 'sim'
                pode_movimentar = 'não'
                print('Finalmente! Peguei a pipoca')
            else:
                print('Ainda não achei a pipoca')

            #Distancia entre você e cambista
            aproximação = (voceX - cambistaX)**2 + (voceY - cambistaY)**2
            if aproximação <= 3**2:
                print('Preciso acelerar, o cambista tá na minha cola!')
            elif 3**2 < aproximação <= 4**2:
                print('Consigo ver lá longe o cambista, mas é melhor acelerar!')
            else:
                print('O cambista está longe, mas não posso ficar parado')
            print('')
    else:
        matrix[voceY][voceX] = 'C'