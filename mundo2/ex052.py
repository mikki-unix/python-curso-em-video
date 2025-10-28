n = int(input('Digite um número inteiro: '))

m = 0
for d in range(1, n):
  if n % d == 0: m += 1
  if m > 2: break

print('\nÉ um número primo' if m == 2 else '\nNão é um número primo')
