"""
operação ternaria
<valor> if <condicao> else <outro valor>
"""

# condicao = 10 == 11
# variavel = 'valor' if condicao else 'Outro valor'
# print(variavel)

# digito = 1
# novo_digito = digito if digito <= 9 else 0
# print(novo_digito)

# Complexo, não é uma boa prática
print('Valor' if True else 'Outro valor' if True else 'Fim')
print('Valor' if False else 'Outro valor' if True else 'Fim')
print('Valor' if False else 'Outro valor' if False else 'Fim')