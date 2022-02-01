"""
For / Else em Python
"""
variavel = ['Luiz Otávio', 'Joãozinho', 'Maria']

comeca_com_j = False
for valor in variavel:
    if valor.lower().startswith('j'):
        comeca_com_j = True

if comeca_com_j:
    print('Existe um palavra que começa com J.')
else:
    print('Não existe uma palavra que começa com J.')

print('---------------------------------------------')

comeca_com_j = False
for valor in variavel:
    if valor.lower().startswith('j'):
        continue
    print(valor)

