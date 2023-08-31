
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

comparacao = primeiro_valor > segundo_valor

if comparacao:
  print(f'{primeiro_valor=} é maior ou igual do que {segundo_valor=}')
else:
  print(f'{segundo_valor=} é maior ou igual do que {primeiro_valor=}')