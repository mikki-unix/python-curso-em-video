n = [
  float(input('Digite o primeiro número: ')),
  float(input('Digite o segundo número: ')),
  float(input('Digite o teceiro número: '))
]

maior = n[0]
menor = n[1]
for atual in n:
  if atual > maior:
    maior = atual

  if atual < menor:
    menor = atual

print(
  '\n* Maior número: ', maior,
  '\n* Menor número: ', menor
)

