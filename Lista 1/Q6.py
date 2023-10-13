nome = input()
pessoas_circulo = int(input())
coeficiente = float(input())

resto = pessoas_circulo % 2
pessoas_fumantes = coeficiente * (pessoas_circulo - 1) / 2

if resto == 0:
    pessoas_fumantes = coeficiente * (pessoas_circulo - 1) + 1
else:
    pessoas_fumantes = coeficiente * (pessoas_circulo - 1) / 2

if 0.5 >= pessoas_fumantes%1 >= 0.1:
    pessoas_fumantes = pessoas_fumantes // 1 
elif 1 >= pessoas_fumantes%1 > 0.5:
    pessoas_fumantes = pessoas_fumantes//1 + 1


print(f'Vamos verificar se {nome} vai fumar singaro!')
print(f'{int(pessoas_fumantes/pessoas_circulo*100)}% dos seus amigos fumam singaro')
if pessoas_fumantes/pessoas_circulo < 25/100:
    print('Você tem poucas chances de fumar singaro, fuma não pow, cuide da sua saúde')
elif 50/100 > pessoas_fumantes/pessoas_circulo > 25/100: 
    print('Cuidado pra não fumar ein, fuma não pow, cuide da sua saúde')
else:
    print('TIRA ESSE SINGARO DA BOCA. FUMA NÃO POW, CUIDE DA SUA SAÚDE!')