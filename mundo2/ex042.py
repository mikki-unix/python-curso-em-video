print('Digite o comprimento de três retas para saber se elas formam um triângulo:\n')

retas = [
  float(input('Reta 1: ')),
  float(input('Reta 2: ')),
  float(input('Reta 3: '))
]

if (
  (retas[0] < retas[1] + retas[2])
  & (retas[1] < retas[0] + retas[2])
  & (retas[2] < retas[0] + retas[1])
):
  print('\nAs retas formam um triângulo!')

  if retas[0] == retas[1] == retas[2]:
    print('Este é um triângulo EQUILÁTERO: todos os seus lados têm comprimentos IGUAIS')
  elif retas[0] != retas[1] != retas[2] != retas[0]:
    print('Este é um triãngulo ESCALENO: todos os seus lados têm comprimentos DIFERENTES')
  else:
    print('Este é um triângulo ISÓCELES: apenas DOIS dos seus lados têm comprimentos IGUAIS')

else:
  print('\nAs retas não formam um triângulo')
