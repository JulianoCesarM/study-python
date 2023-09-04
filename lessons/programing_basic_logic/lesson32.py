"""
Faça um programa que peça para o usuário digitar um número inteiro, e informe se esse número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""
# numero = input("Dígite um número inteiro: ")

# try:
#   numero_inteiro = int(numero)
#   par_ou_impar = int(numero_inteiro) % 2 == 0

#   if par_ou_impar:
#     print("É par")
#   else:  
#     print("É impar")
# except:
#   print("Não é um número inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23
"""
# horario = input("Que horas são agora? ")

# try:
#   horario_inteiro = int(horario)

#   bom_dia =  horario_inteiro >= 0 and horario_inteiro <= 11
#   boa_tarde = horario_inteiro <= 17
#   boa_noite = horario_inteiro <= 23
  
#   if bom_dia:
#     print(f"Bom dia, são {horario_inteiro} horas.")
#   elif boa_tarde:
#     print(f"Boa tarde, são {horario_inteiro} horas.")
#   elif boa_noite:
#     print(f"Boa noite, são {horario_inteiro} horas.")
#   else:
#     print("Não é um horário válido")
# except:
#   print("Não é um número")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
primeiro_nome = input("Dígite seu primeiro nome? ")

qtd_letras = len(primeiro_nome)

if primeiro_nome > 1:
  if  qtd_letras <= 4:
    print("Seu nome é curto.")
  elif qtd_letras >= 5 and qtd_letras <= 6:
    print("Seu nome é normal")
  else:
    print("Seu nome é muito grande")
else:
  print("Números não são permitidos.")