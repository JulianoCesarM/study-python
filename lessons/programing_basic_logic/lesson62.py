"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

cpf_enviado_usuario = '74682489070'
nove_digitos = cpf_enviado_usuario[:9]

contador_1 = 10

result_1 = 0
for digito in nove_digitos:
    result_1 += int(digito)*contador_1 
    contador_1-=1

result_1 = (result_1 * 10) % 11
result_1 = result_1 if result_1 <= 9 else 0

dez_digitos = nove_digitos + str(7)
contador_2 = 11
result_2 = 0
for digito in dez_digitos:
    result_2 += int(digito)*contador_2 
    contador_2-=1

result_2 = (result_2 * 10) % 11
result_2 = result_2 if result_2 <= 9 else 0


cpf_gerado_pelo_calculo = f'{nove_digitos}{result_1}{result_2}'

if cpf_gerado_pelo_calculo == cpf_enviado_usuario:
    print(f'O cpf é válido: {cpf_gerado_pelo_calculo}')
else:
    print('CPF inválido')