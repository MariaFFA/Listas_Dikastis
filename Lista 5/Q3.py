nome_suspeito = input()
nome_suspeito_igual = nome_suspeito.lower()
string_concat = input()
string_concat = string_concat.lower()
string_concat = list(string_concat)

i, f = 0, 0

def parte_string(i,f):
    if ''.join(string_concat[i:f]) == nome_suspeito_igual:
        return 'encontrado'
    elif f < len(string_concat):
        f += 1
        return parte_string(i, f)
    elif i < len(string_concat):
        i += 1
        f = i
        return parte_string(i, f)

suspeito = parte_string(0,0)

if suspeito == 'encontrado':
    print(f'Encontrei, o culpado é o {nome_suspeito}!')
else:
    print(f'Não era o {nome_suspeito}, tenho que continuar procurando.')