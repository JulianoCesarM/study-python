"""
Fatiamento de strings
 012345678
 olá mundo
-987654321

fatiamento [i:f:p][::] 
obs: a função len retorna a quantidade de caracteres da str
"""

variavel = "Olá mundo"
print(variavel[4:])
print(variavel[4:7])
print(variavel[4:8])
print(variavel[0:5])
print(variavel[:5])
print(variavel[-8:-2])
print(variavel[5])
print(variavel[0:9:2]) # 2 - step by step
print(variavel[-1:-10])
print(variavel[-1:-10:-1])
print(variavel[-1:-10:-2]) # -2 - step by step
print(len(variavel))