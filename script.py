verificador_unidade = 0
verificador_dezena = 0
cpf = input("Imforme o CPF: ")
cpf = cpf.replace('.', '').replace('-', '')
if len(cpf) != 11:
    print('erro (A quantidade de caracteres não é valida.)')
else:
    numero = []
    numero.append(int(cpf[0:1]))
    numero.append(int(cpf[1:2]))
    numero.append(int(cpf[2:3]))
    numero.append(int(cpf[3:4]))
    numero.append(int(cpf[4:5]))
    numero.append(int(cpf[5:6]))
    numero.append(int(cpf[6:7]))
    numero.append(int(cpf[7:8]))
    numero.append(int(cpf[8:9]))
    numero.append(int(cpf[9:10]))
    numero.append(int(cpf[10:11]))
    resto_div_digito1 = ((numero[0] * 10) + (numero[1] * 9) + (numero[2] * 8) + (numero[3] * 7) + (numero[4] * 6) + (numero[5] * 5) + (numero[6] * 4) + (numero[7] * 3) + (numero[8] * 2)) % 11
    if resto_div_digito1 == 0 or resto_div_digito1 == 1:
        verificador_dezena = 0 
    else:
        verificador_dezena = 11 - resto_div_digito1
    resto_div_digito2 = ((numero[0] * 11) + (numero[1] * 10) + (numero[2] * 9) + (numero[3] * 8) + (numero[4] * 7) + (numero[5] * 6) + (numero[6] * 5) + (numero[7] * 4) +(numero[8] * 3) + (verificador_dezena * 2)) % 11
    if resto_div_digito2 == 0 or resto_div_digito2 == 1:
        verificador_unidade = 0 
    else:
        verificador_unidade = 11 - resto_div_digito2
    if verificador_dezena == numero[9] and verificador_unidade == numero[-1]:
        print(f'O CPF do usuário ({cpf}) é valido.')
    else:
        print(f'O CPF do usuário ({cpf}) é invalido')
  