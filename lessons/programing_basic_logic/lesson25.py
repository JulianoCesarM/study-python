"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""


nome = "Juliano"
preco = 100.98456

variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
print(variavel)

# 8 - quantas casas tem, 0 - preenche com 0 caso alguma casa não tenha valor
print('O hexadecimal de %d é %08x' % (1500,1500))