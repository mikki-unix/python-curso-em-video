c = 0
soma = 0
for n in range(1, 7):
  num = int(input('Digite o {}º número inteiro: '.format(n)))
  if num % 2 == 0:
    c += 1
    soma += n

print(
  '\nA soma dos {} pares digitados é igual à {}'
  .format(c, soma)
)
