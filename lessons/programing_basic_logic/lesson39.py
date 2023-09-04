"""

"""
#       123456789...
nome = 'Juliano Cesar Magoga'
tamanho_nome= len(nome)
print(nome)
print(tamanho_nome)

contador = 0
nova_string = ''

while contador < tamanho_nome:
  if nome[contador] == " ":
    nova_string += f' '
  else:
    nova_string += f'*{nome[contador]}'
  contador+=1

nova_string += f'*'
print(nova_string)