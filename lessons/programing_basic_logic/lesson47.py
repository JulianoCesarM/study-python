import os

palavra_secreta = "python"
letra_acertada = ''
contagem = 0

while True:
  letra = input('Digite uma letra: ')
  contagem += 1

  if len(letra) > 1:
    print("Digite apenas uma letra")
    continue

  if letra in palavra_secreta:
    letra_acertada += letra

  palavra_formada = ''
  for letra_secreta in palavra_secreta:
    if letra_secreta in letra_acertada:
      palavra_formada += letra_secreta
    else:
      palavra_formada += '*'
  print(palavra_formada)

  if palavra_formada == palavra_secreta:
    os.system('cls')
    print(f'Palavra secreta: {palavra_secreta}! Parabéns, palavra advinhada.')
    break

print(f'O numero de tentativas foi {contagem} vezes')