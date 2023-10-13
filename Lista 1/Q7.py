funcionalidade1 = input()
funcionalidade_ponto1 = int(input())
funcionalidade2 = input()
funcionalidade_ponto2 = int(input())
funcionalidade3 = input()
funcionalidade_ponto3 = int(input())
funcionalidade4 = input()
funcionalidade_ponto4 = int(input())
funcionalidade5 = input()
funcionalidade_ponto5 = int(input())

if funcionalidade1 == 'novo lançador de teias':
    print('Com calma, aranha')
    if funcionalidade2 == 'lentes de visão avançada':
        print('Lembre de desativar as lentes depois, e cuidado ao usar as teias no escuro')
        if funcionalidade3 == 'traje à prova de balas':
          print('UOU, só tente sair dessa vivo, vou otimizar a energia aqui')

if funcionalidade1 == 'ativação de inteligência artificial' or funcionalidade2 == 'ativação de inteligência artificial' or funcionalidade3 == 'ativação de inteligência artificial' or funcionalidade4 == 'ativação de inteligência artificial' or funcionalidade5 == 'ativação de inteligência artificial':
    print('Espero que não esteja ativando isso para usar nas provas')

if funcionalidade_ponto1 + funcionalidade_ponto2 + funcionalidade_ponto3 + funcionalidade_ponto4 + funcionalidade_ponto5 >= 80:
    print('Vou descarregar em questão de minutos, pare AGORA')

if (funcionalidade1 == 'ativação de inteligência artificial' or funcionalidade2 == 'ativação de inteligência artificial' or funcionalidade3 == 'ativação de inteligência artificial' or funcionalidade4 == 'ativação de inteligência artificial' or funcionalidade5 == 'ativação de inteligência artificial') and (funcionalidade1 == 'membranas planadoras' or funcionalidade2 == 'membranas planadoras' or funcionalidade3 == 'membranas planadoras' or funcionalidade4 == 'membranas planadoras' or funcionalidade5 == 'membranas planadoras') and (funcionalidade1 == 'novo lançador de teias' or funcionalidade2 == 'novo lançador de teias' or funcionalidade3 == 'novo lançador de teias' or funcionalidade4 == 'novo lançador de teias' or funcionalidade5 == 'novo lançador de teias'):
    print('Tudo certo, mas cuidado ao ficar conversando com IA enquanto voa')

soma_funcionalidade = funcionalidade_ponto1 + funcionalidade_ponto2 + funcionalidade_ponto3 + funcionalidade_ponto4 + funcionalidade_ponto5
print(f'Aranha, nessa sequência você usou {soma_funcionalidade} de energia!')