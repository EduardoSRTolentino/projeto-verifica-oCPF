verificador_unidade = 0
verificador_dezena = 0
cpf = input("Imforme o CPF: ")
digito1 = cpf[0:1]
digito2 = cpf[1:2]
digito3 = cpf[2:3]
digito4 = cpf[3:4]
digito5 = cpf[4:5]
digito6 = cpf[5:6]
digito7 = cpf[6:7]
digito8 = cpf[7:8]
digito9 = cpf[8:9]
digito10 = cpf[9:10]
digito11 = cpf[10:11]

numero01 = int(digito1)
numero02 = int(digito2)
numero03 = int(digito3)
numero04 = int(digito4)
numero05 = int(digito5)
numero06 = int(digito6)
numero07 = int(digito7)
numero08 = int(digito8)
numero09 = int(digito9)
numero10 = int(digito10)
numero11 = int(digito11)
resto_div_digito1 = ((numero01 * 10) + (numero02 * 9) + (numero03 * 8) + (numero04 * 7) + (numero05 * 6) + (numero06 * 5) + (numero07 * 4) + (numero08 * 3) + (numero09 * 2)) % 11
if resto_div_digito1 == 0 or resto_div_digito1 == 1:
    verificador_dezena = 0 
else:
    verificador_dezena = 11 - resto_div_digito1
resto_div_digito2 = ((numero01 * 11) + (numero02 * 10) + (numero03 * 9) + (numero04 * 8) + (numero05 * 7) + (numero06 * 6) + (numero07 * 5) + (numero08 * 4) +(numero09 * 3) + (verificador_dezena * 2)) % 11
if resto_div_digito2 == 0 or resto_div_digito2 == 1:
    verificador_unidade = 0 
else:
    verificador_unidade = 11 - resto_div_digito2
