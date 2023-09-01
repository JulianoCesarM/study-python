"""
f-strings

s - string
d - int
f - float (.<numero de digitos>f)

(caracteres)(<>^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - força o numero a aparecer antes dos zeros
Ex.: 0>-100,.1f (O zero será colocado nos espaços vazios)
Conversation flags - !r !s !a
"""

variavel = "ABC"

print(f'{variavel}')
print(f'{variavel: >10}.') # Espaços á direita
print(f'{variavel: <10}.') # Espaços á esquerda
print(f'{variavel: ^10}.') # Espaços centralizados
print(f'{-1000.165486:0=+10,.1f}')

print(f'O hexadecimal de 1500 é {1500:08X}')

print(f'{variavel!r}')