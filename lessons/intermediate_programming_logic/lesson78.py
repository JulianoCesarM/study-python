# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Juliano')
# s1 = set()  # vazio
# s1 = {'Juliano', 1, 2, 3}  # com dados
# print(s1)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# s1 = s1 = {1,2,3,{123}} # Não aceitam valores mutáveis; set ou lista ou tupla dentro de set
# l1 = [1,2,3,3,3,3,3,1]
# s1 = set(l1)
# l2 = list(s1)
# print(s1)
# print(l2)

# s1 = {1,2,3}
# print(3 in s1)
# print(2 not in s1)

# for num in s1:
#     print(num)

# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Juliano')
# s1.add(1,2) # só aceita 1 valor por vez
s1.add(1)
s1.update(('Olá mundo', 1,2,3,4)) # O parentezes dentro dele se torna um iteravel; fazendo ser possivel colocar varios valores
# s1.clear()
s1.discard('Olá mundo')
s1.discard('Juliano')
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^ s2
print(s3)