# com módulo é bem melhor...
from math import hypot

print('> O quadrado da hipotenusa é igual a soma do quadrado dos catetos...\n')

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

print('\nA hipotenusa corresponde à {:.2f}'.format(hypot(co, ca)))