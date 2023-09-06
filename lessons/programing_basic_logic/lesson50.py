"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ["Maria", "helena", 'Luiz']
lista.append("joão")

indices = range(len(lista))
for indice in indices:
  print(indice, lista[indice], type(lista[indice]))

# Usando método
# for nome in lista:
#   print(lista.index(nome)," ",nome)