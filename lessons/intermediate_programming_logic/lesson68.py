"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
x=1 # x - escopo módulo

def escopo():
    global x # Manipulando o x de fora
    x=10 # x - escopo da função escopo
    
    def outra_funcao():
        global x
        x=11 # x - escopo da função outra_função
        y=2
        print(x,y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)