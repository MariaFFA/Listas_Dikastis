local_ferias = input()
local_procurar = input()

if local_ferias.lower() != local_procurar.lower():
    print ('Carambolas, ele não está aqui. Ele continua se divertindo!')
    local_procurar = input()
    if local_ferias.lower() != local_procurar.lower():
        print('Carambolas, ele não está aqui. Ele continua se divertindo!')
        local_procurar = input()
        if local_ferias.lower() != local_procurar.lower():
            print('Carambolas, ele não está aqui. Ele continua se divertindo!')
            print('AAAAAAAH, ele escapou de vez!')
        else:
            print('Ahá, te encontrei e é o fim das suas férias!')
    else:
        print('Ahá, te encontrei e é o fim das suas férias!')
else:
    print('Ahá, te encontrei e é o fim das suas férias!')