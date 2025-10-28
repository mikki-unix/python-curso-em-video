frase = input('Digite uma frase sem acentos: ').strip().upper().split()
frase = ''.join(frase)
fraseInvertida = frase[::-1]

"""
fraseInvertida = ''
for i in range (len(frase) - 1, -1, -1):
  fraseInvertida += frase[i]
"""

print('O inverso da frase {} é {}'.format(frase, fraseInvertida))
print('É um palíndromo!'
  if frase == fraseInvertida
  else 'Não é um palíndromo'
)
