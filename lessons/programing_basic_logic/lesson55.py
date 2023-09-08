import decimal

numero_1 = decimal.Decimal('0.1') # Usado para ter uma extrtema precisão
numero_2 = 0.7 
numero_3 = numero_1 + numero_2

print(numero_3)
print(f'{numero_3:.2f}') # Formatação e transforma o float em str
print(round(numero_3, 2)) # Formatação e não modifica o tipo    