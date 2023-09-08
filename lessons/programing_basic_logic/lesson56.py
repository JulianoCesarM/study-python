"""
split e join com list e str
split - divide uma string em uma lista
join - une uma string
"""
frase = '    Olha só que, coisa interessante     '

# lista_palavras_1 = frase.split()
# lista_palavras_2 = frase.split(', ') # Separa quando encontra uma virgula o espaço conta
# print(lista_palavras_1)
# print(lista_palavras_2)

lista_palavras_cruas= frase.split(',')

# Funcional porem jeito errado de fazer
# for i, frase in enumerate(lista_palavras_3):
#     print(lista_palavras_3[i].strip()) # corta os espaços iniciais e finais


# Melhores práticas de programação 
lista_frases = []
for i, frase in enumerate(lista_palavras_cruas):
    lista_frases.append(lista_palavras_cruas[i].strip()) # corta os espaços iniciais e finais

print(lista_palavras_cruas)
print(lista_frases)


frases_unidas = ", ".join(lista_frases) # É str e join - junta uma lista tupla...
print(frases_unidas)