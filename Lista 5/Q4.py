#Derivar
def derivada(ordem, numero,coeficiente):
    if ordem > 0 and coeficiente > 0:
        ordem -= 1
        return derivada(ordem, (numero * coeficiente), (coeficiente - 1))
    if numero != 0:
        if coeficiente == 0:
            return str(numero)
        elif coeficiente == 1:
            return f'{numero}x'
        elif ordem  == 0:
            return f'{numero}x^{coeficiente}'
        else:
            return f'{numero * coeficiente}x^{coeficiente - 1}'

    else:
        return ''

grau = int(input())
ordem = int(input())
coeficientes_n_nulos = int(input())
derivadas = []
polinomios = []

for _ in range(grau + 1):
    polinomios.append('')
for _ in range(grau + 1):
    derivadas.append('')

#Polinomio
for _ in range(coeficientes_n_nulos):
    coeficiente_numero = input()
    coeficiente_numero = coeficiente_numero.split(' ')
    coeficiente = int(coeficiente_numero[2])
    numero = int(coeficiente_numero[4])
    if numero != 0:
        polinomios[coeficiente] = numero
        if ordem == 0:
            if coeficiente == 0:
                derivadas[coeficiente] = str(numero)
            elif coeficiente == 1:
                derivadas[coeficiente] = f'{numero}x'
            else:
                derivadas[coeficiente] = f'{numero}x^{coeficiente}'
        elif coeficiente - ordem >= 0:
            derivadas[coeficiente - ordem] = derivada(ordem, numero,coeficiente)

#Formatar polinomio
for i in polinomios:
    if polinomios.index(i) == 0:
        polinomios[polinomios.index(i)] = f'{i}'
    elif polinomios.index(i) == 1 and i != '':
        polinomios[polinomios.index(i)] = f'{i}x'
    elif i == 1:
        polinomios[polinomios.index(i)] = f'x^{polinomios.index(i)}'
    elif i == -1:
        polinomios[polinomios.index(i)] = f'-x^{polinomios.index(i)}'
    elif i != '' and polinomios.index(i) != 0:
        polinomios[polinomios.index(i)] = f'{i}x^{polinomios.index(i)}'
while '' in polinomios:
    polinomios.remove('')
polinomio = '+'.join(polinomios)
index = -1
for j in polinomio:
    if j == '-':
        polinomio = list(polinomio)
        index = polinomio.index(j, index + 1)
        if index != 0:
            polinomio.pop(index-1)
        polinomio = ''.join(polinomio)
if polinomio == '':
    print(f'A derivada {ordem} do polinômio 0 é')
else:
    print(f'A derivada {ordem} do polinômio {polinomio} é')

#Formatar derivada
while '' in derivadas:
    derivadas.remove('')
derivada = '+'.join(derivadas)
index = -1
for k in derivada:
    if k == '-':
        derivada = list(derivada)
        index = derivada.index(k, index + 1)
        if index != 0:
            derivada.pop(index-1)
        derivada = ''.join(derivada)

if derivada == '':
    print('0')
else:
    print(derivada)