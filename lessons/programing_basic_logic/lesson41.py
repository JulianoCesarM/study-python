string = "Valor qualquer"


i=0
while i < len(string):
  letra = string[i]
  print(letra)
  
  if letra == ' ':
    break # O else nunca será executado.

  i+= 1
else:
  print("O else foi executado.")
print("Fora do while")