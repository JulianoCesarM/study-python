"""
Introdução ao desempacotamento 
"""

# nome1, nome2, nome3 = ["Maria", "Helena", 'Luiz']
# nome1, *_ =["Maria", "Helena", 'Luiz']

_, _, nome2, *resto = ["Maria", "Helena", 'Luiz']
print(nome2, resto)