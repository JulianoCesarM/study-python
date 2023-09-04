"""
Repetições
while

Executa uma ação quando uma condição for verdadeira

loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador < 10:
  contador += 1
  print(contador)

contador = 1
while contador < 10:
  contador *= 2
  print(contador)

contador = 10
while contador > 0:
  contador -= 1
  print(contador)

print("Acabou")