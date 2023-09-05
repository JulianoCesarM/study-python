"""
Iterável -> str, range, etc
iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
texto = iter('luiz') # __iter__()
# print(next(texto)) # __next__()

# iterador = iter(texto)
# # while True:
# #   try:
# #     letra = next(iterador)
# #     print(letra)
# #   except StopIteration:
# #     break

for letra in texto:
  print(letra)