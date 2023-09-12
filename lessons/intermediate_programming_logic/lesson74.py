"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

# print(falar_bom_dia("Juliano"))
# print(falar_boa_noite("Juliano")) # Closure

for nome in ['Maria', 'Joana', "Luiz"]:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome)) # Closure