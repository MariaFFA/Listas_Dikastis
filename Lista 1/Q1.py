nome_aranha = input()
frequencia_maquina = float(input())

if nome_aranha == "Miles Morales" and 2400 > frequencia_maquina >= 800 :
    print('Miles será enviado para a praça do Harlem! O Rino e o Prowler estão causando problemas demais essa hora do dia!')
elif nome_aranha == "Miles Morales" and frequencia_maquina < 800 :
    print('Miles está mais livre e pode passar pra visitar sua mãe Rio em seu apartamento!')
elif nome_aranha == "Miles Morales" and 2400 <= frequencia_maquina:
    print('Essa frequência é desconhecida para o Miles! Com certeza vai achar encrenca!')
elif nome_aranha == "Spider-Gwen" and 3000 > frequencia_maquina >= 600 :
    print('A Gwen deve ir dar um basta nas operações da Tinkerer, ajustaremos a Máquina para a Times Square!')
elif nome_aranha == "Spider-Gwen" and frequencia_maquina < 600 :
    print('A Gwen está liberada pra tomar Sorvete no Central Park, esse será seu Destino')
elif nome_aranha == "Spider-Gwen" and 3000 <= frequencia_maquina:
    print('Sabemos que a Gwen está mais habituada pra viajar entre Universos mas essa frequência é perigosa até para ela!!')
elif nome_aranha == "Miranha-Furacão" and frequencia_maquina > 0 :
    print('A Carreta Furacão sai desgovernada pra animar mais uma rua em Cabrobó!')
elif nome_aranha == "Miranha-Furacão" and frequencia_maquina <= 0 :
    print('Mas o que é isso?! Esse bregueço deve ta quebrado, Miranha-Furacão, Pica-Pau, Pikachu, Mickey e Cascão vão continuar treinando seu número em casa!')
elif nome_aranha == "Homem-Aranha do PS4" or nome_aranha == "Homem-Funko-Pop" :
    print('Maceió! Há rumores de um Vilão misterioso nas praias, alguns Aranhas devem ir pra lá!')
elif nome_aranha == "Porco-Aranha":
    print('O destino será a Fazendinha do Plaza!')
else :
    print('Quê?! Ou esse Aranha não existe ou não deve ser enviado em nenhuma missão pelo Dikastisverso!')
