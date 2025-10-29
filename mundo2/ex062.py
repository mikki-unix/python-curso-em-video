print('==Progressão Aritmética==')
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

n = 1
fim = 11
while True:
  if n == fim:
    print('Fim')
    nx = int(input('Quer mostrar mais quantos termos? '))
    if nx <= 0:
      break
    fim += nx

  an = a1 + (n - 1) * r
  print(an, end=' → ')
  n+=1
