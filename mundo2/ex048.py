c = 0
soma = 0
for n in range (3, 501, 2):
  if n % 3 == 0:
    c += 1
    soma += n

print('=' * 42)
print(
'Há {} valores múltiplos de 3 entre 1 e 500'
'\nE a soma deles é igual à: {}'
.format(c, soma)
)
print('=' * 42)
