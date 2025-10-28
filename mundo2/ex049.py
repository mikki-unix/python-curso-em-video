n = int(input('Número para a tabuada: '))

print('\n~~Tabuada do {}~~'.format(n))
for m in range (1, 11):
  print('{} x {} = {}'.format(n, m, n * m))
