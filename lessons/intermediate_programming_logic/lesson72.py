# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplicar(*args):
    total = 1
    for num in args:
        if num == 0:
            return f"A conta contem uma multiplicação com ZERO o total será 0"
        total *= num
    return f'Total da multiplicação é {total}'

multiplicacao = multiplicar(2,3,4,5,6)
print(multiplicacao)

# Crie uma função que fale se um número é par ou ímpar.
# Retorne se o número é par ou impar.
def par_ou_impar(x):
    result = x % 2 == 0
    if result == True:
        return f"Número {x} é Par"
    return f"Número {x} é Impar"
    
parImpar = par_ou_impar(3)
print(parImpar)