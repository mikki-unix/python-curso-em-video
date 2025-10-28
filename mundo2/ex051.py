print('==Progressão Aritmética==')

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

for n in range(a1, (a1 + (11 - 1) * r), r):
  print(n, end=' → ')
print('Fim')