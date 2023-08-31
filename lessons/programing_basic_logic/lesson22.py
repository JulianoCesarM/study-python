entrada = input('[E]ntrar [S]air: ').upper()
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == "E" or entrada == "e" and senha_digitada == senha_permitida:
  print('Entrou')
else:
  print('Saiu')