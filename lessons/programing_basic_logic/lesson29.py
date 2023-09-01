"""
Fail fast

try/except
try -> tente executar o codigo
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobrar o número que vc digitar: ')

try:
  numero_float = float(numero_str)
  print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
  print('Não é um número')


# if numero_str.isdigit():
#   numero_float = float(numero_str)
#   print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#   print('Não é um número')

