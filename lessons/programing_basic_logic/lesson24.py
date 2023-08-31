nome = 'Juliano'

print(nome[2])
print(nome[-5])

print('uli' in nome)
print('á' in nome)

print('uli' not in nome)
print('á' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
  print(f'{encontrar} está em {nome}')
else:
  print(f'{encontrar} não está em {nome}')