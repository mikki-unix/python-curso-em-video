print('Digite o peso de cinco pessoas:')

maiorPeso = 0
menorPeso = 0
for p in range(1, 6):
  pesoAtual = float(input('Pessoa {}: '.format(p)))

  if p == 1:
    maiorPeso = pesoAtual
    menorPeso = pesoAtual

  if pesoAtual > maiorPeso:
    maiorPeso = pesoAtual
  if pesoAtual < menorPeso:
    menorPeso = pesoAtual

print("""
* Maior peso: {}
* Menor peso: {}
""".format(maiorPeso, menorPeso)
)
