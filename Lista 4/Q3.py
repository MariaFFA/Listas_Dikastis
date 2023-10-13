def palindromo(f_n):
    f_n_palindromo = f_n[slice(-1,-(len(f_n) + 1),-1)]
    if f_n == f_n_palindromo:
        return True
    else: 
        return False

def contar_distintos(f_n):
    distintos = 0
    while f_n != []:
        distintos += 1
        primeiro_caractere = f_n[0]
        while primeiro_caractere in f_n:
            f_n.remove(primeiro_caractere)
    return distintos


n = int(input())
for _ in range(n):
    frase_numero = input()
    frase_numero_limpa = frase_numero.lower()
    frase_numero_limpa = list(frase_numero_limpa)
    while ' ' in frase_numero_limpa:
        frase_numero_limpa.remove(' ')
    if palindromo(frase_numero_limpa):
        if frase_numero.isdigit():
            print(f'O número "{frase_numero}" é um palíndromo!')
            print(f'Há {contar_distintos(frase_numero_limpa)} número(s) distinto(s) na sequência de números.')
        else:
            print(f'A frase "{frase_numero}" é um palíndromo!')
            print(f'Há {contar_distintos(frase_numero_limpa)} letra(s) distinta(s) na frase.')
    else:
        print('A frase ou o número não é um palíndromo.')

