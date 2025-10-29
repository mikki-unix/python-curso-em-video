print('==Progressão Aritmética==')
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

n = 1
while n != 11:
  an = a1 + (n - 1) * r
  print(an, end=' → ')
  n+=1
print('Fim')
