import random

for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0,9))

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

    print(cpf_gerado_pelo_calculo)


