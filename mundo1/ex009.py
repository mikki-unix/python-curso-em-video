n = int(input('Digite um número para a tabuada: '))

print('\n{:~^20}'.format('Tabuada do nº ' + str(n)))

# m = múltiplo
for m in range(1, 11):
  print('{} x {} = {}'.format(n, m, n*m))

print('~'*20)