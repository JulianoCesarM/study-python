"""
Repetições
while

Executa uma ação quando uma condição for verdadeira

loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador < 10:
  contador += 1
  
  if contador >= 3 and contador <= 6:
    print(f"Não vou mostrar o {contador}.")
    continue

  print(contador)
  if contador == 8:
    break
print("Acabou")