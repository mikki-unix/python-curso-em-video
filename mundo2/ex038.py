numeros = [
  int(input('Digite um número inteiro: ')),
  int(input('Digite outro número inteiro: '))
]

if numeros[0] > numeros[1]:
  print('O primeiro número é o maior!')
elif numeros[1] > numeros[0]:
  print('O segundo número é o maior!')
else:
  print('Os números são iguais, portanto não há um maior')