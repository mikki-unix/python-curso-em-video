print('Digite os comprimentos de três retas para saber se elas formam um triângulo.')

retas = [
  float(input('Reta 1: ')),
  float(input('Reta 2: ')),
  float(input('Reta 3: '))
]

if (
  (retas[0] < retas[1] + retas[2])
  & (retas[1] < retas[0] + retas[2])
  & (retas[2] < retas[0] + retas[1])
): print('\nEssas retas podem formar um triângulo!')

else: print('\nAs retas não formam um triângulo.')
