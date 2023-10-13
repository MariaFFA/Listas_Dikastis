#Converter número
def converter(frase):
  numero = []
  frase = frase.split('+')
  while '+' in frase:
    frase.remove('+')
  for n in frase:
    if n == "Oooh look at him":
      numero.append('0')
    elif n == "Baseball bat":
      numero.append('1')
    elif n == "Aesthetic":
      numero.append('2')
    elif n == "Fake Natty":
      numero.append('3')
    elif n == "Chris Bumbstead, o CBUM":
      numero.append('4')
    elif n == "Pope Francis":
      numero.append('5')
    elif n == "O suco vicia":
      numero.append('6')
    elif n == "I don't know you tell me":
      numero.append('7')
    elif n == "Não é mesmo?":
      numero.append('8')
    elif n == "Rodrigo Goes out":
      numero.append('9')
  numero = ''.join(numero)
  return int(numero)

#Verificar se tem lugar vazio ou faltando
def lugar_vazio(fila):
    for i in range(len(fila)):
        if i not in fila:
            return 'NO'
        elif fila[i] == 0:
            fila.pop(i)
    return fila
  
n_pessoas = int(input())
fila = {}

#Adicionar cada pessoa ao seu lugar
for _ in range(n_pessoas):
    frase = input()
    lugar = converter(frase)
    if lugar not in fila:
        fila[lugar] = 1
    else:
        fila[lugar] += 1

fila = lugar_vazio(fila)

#Tirar uma pessoa de cada lugar
while fila != 'NO' and fila.get(0) is not None:
    for f in range(len(fila)):
        fila[f] -= 1
    fila = lugar_vazio(fila)   

#Conclusão
if len(fila) == 0:
    print('YES')
else:
    print('NO')