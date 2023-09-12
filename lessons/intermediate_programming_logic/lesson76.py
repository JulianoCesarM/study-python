# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')


# pessoa = {
#     'nome': 'Juliano Cesar',
#     'sobrenome': 'Magoga',
#     'idade': 23,
#     'altura': 1.75,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }

# # print(pessoa, type(pessoa))
# print(pessoa['nome'])
# print(pessoa['sobrenome'])

# for chave in pessoa:
#     print(chave, pessoa[chave])

# pessoa = {}

# chave = 'nome'

# pessoa[chave] = 'Juliano Cesar'
# pessoa['sobrenome'] = 'Magoga'

# print(pessoa[chave])
# pessoa[chave] = 'Maria'
# # del pessoa['sobrenome']
# print(pessoa)

# if pessoa.get('sobrenome') is None:
#     print("Não Existe")
# else:
#     print(pessoa['sobrenome'])


# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# import copy

pessoa = {
    'nome': 'Juliano Cesar',
    'sobrenome': 'Magoga',
    # 'idade': 23
    # 'l1': [0,1,2]
}

# pessoa.setdefault('idade', None)
# print(pessoa['idade'])
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)

# pessoa2 = pessoa.copy() # shallow copy
# pessoa2 = copy.deepcopy(pessoa) # deep copy

# pessoa2['nome'] = "Claudio"
# pessoa2['sobrenome'] = "Miranda"
# pessoa2['l1'][1] = 9999
# print(pessoa)
# print(pessoa2)

# print(pessoa.get('nome', 'Não existe'))

# nome =  pessoa.pop('nome')
# print(nome)
# print(pessoa)

# ultime_chave =  pessoa.popitem()
# print(ultime_chave)
# print(pessoa)

# pessoa.update({'nome':'novo valor', 'idade': 23})
# pessoa.update(nome='novo valor', idade=23)
# pessoa.update((('nome','novo valor'), ('idade', 23)))
# lista = [['nome','novo valor'], ['idade', 23]]
tupla = ('nome','novo valor'), ('idade', 23)
pessoa.update(tupla)
print(pessoa)