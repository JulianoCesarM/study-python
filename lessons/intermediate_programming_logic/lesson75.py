# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def calcular(texto, multiplicador):
    def multiplicando(valor):
        return f'{texto}: {valor * multiplicador}'
    return multiplicando

duplicando = calcular('Duplicando',2)
triplicando = calcular('Triplicando',3)
quaduplicando = calcular('Quadruplicando',4)

valor = 15

print(duplicando(valor))
print(triplicando(valor))
print(quaduplicando(valor))