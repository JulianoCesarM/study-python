# Fazer a conta sem lambda
# def cria_multiplicador(multiplicador):
#     def multplica(numero):
#         return numero * multiplicador
#     return multplica
# duplica = cria_multiplicador(2)
# print(duplica(2))


# def soma(x, y):
#     return x + y

# Fazer a conta com lambda
def executa(funcao, *args):
    return funcao(*args)

# lambda - é uma função sem nome 
# lambda seria a funcao em executa
# O resto seria empacotado em *args 
duplica = executa(lambda m: lambda n: n * m, 2)

print(
    executa(
        lambda x, y: x + y, 
        2, 3
    ),
    duplica(2)
)
print(
    executa(
        lambda *args: sum(args),
        1,2,3,4,5,6
    )
)

