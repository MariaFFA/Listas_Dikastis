numero_nomes = int(input())
natty ={}
fake_natty = {}

for _ in range(numero_nomes):
    pessoa_nota_cat = input()
    pessoa_nota_cat = pessoa_nota_cat.split(' - ')
    pessoa = pessoa_nota_cat[0]
    nota = int(pessoa_nota_cat[1])
    categoria = pessoa_nota_cat[2]
    nome = (nota,categoria)
    if nome[1] == 'natty':
        natty[pessoa] = nota
    else:
        fake_natty[pessoa] = nota

natty_ordenado = sorted(natty, key = natty.get, reverse=True)

fake_natty_ordenado = sorted(fake_natty, key = fake_natty.get, reverse=True)

for p in natty_ordenado:
    print(f'{p} - {natty[p]} - natty')

for pf in fake_natty_ordenado:
    print(f'{pf} - {fake_natty[pf]} - FAKE NATTY')

