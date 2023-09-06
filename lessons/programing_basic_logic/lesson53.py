"""
enumeramento - enumera iteráveis
"""
lista = ["Maria", "helena", 'Luiz']
lista.append("joão")

# for item in enumerate(lista):
#   print(item)

# for item in enumerate(lista):
#   indice,nome = item
#   print(indice, nome)

for indice, nome in enumerate(lista):
  print(indice, nome)


# lista_enumerada = enumerate(lista) # Não é legal atribuir á uma variavel
# lista_enumerada = list(enumerate(lista)) # Ele cria uma lista com varias tupla tendo o indice e o valor
# print(lista_enumerada)