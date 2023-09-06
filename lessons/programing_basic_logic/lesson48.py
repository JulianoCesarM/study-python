"""
Lista em Python
Tipo list - Mutável
Suporta valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, clear, extend... 
Create, Update, Read, Delete - lista[i](CRUD)
"""

# string = 'ABCDE'
# # print(bool([])) 
# # print(list, type(lista)) 

#        0  1  2  3
lista = [10,20,30,40]

# #        0    1     2                3    4 
# lista = [123, True, 'Juliano Cesar', 1.2, []]
# print(lista, type(lista))
# lista[-3] = 'Maria'
# print(lista[2].upper(), type(lista[2]))


# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

# lista.append(50)
# lista.pop()
# lista.append(60)
# lista.append("BBB")
# ultimo_valor = lista.pop()
# print(lista, 'Removido, ', ultimo_valor)

# lista.append("Luiz")
# nome = lista.pop()
# lista.append(1233)
# del lista[-1] # Delet last element
# lista.clear()
# lista.insert(0, 5) # 0 -> index
# lista.insert(100, 6)

# print(lista)

# lista_a = [1,2,3]
# lista_b = [4,5,6]
# lista_c = lista_a + lista_b
# # lista_d = lista_a.extend(lista_b)
# lista_a.extend(lista_b)
# print(lista_c)
# print(lista_a)

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['luiz', 'maria', 1 ,True,1.2]
# lista_b = lista_a # O lista_b NÃO COPIA os valores da lista_a, ele somente aponta para onde os valores estão na memória
lista_b = lista_a.copy() 
lista_a[0] = "Qualquer coisa"

print(lista_b)