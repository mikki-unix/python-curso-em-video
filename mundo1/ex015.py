d = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos KM rodados ao todo? '))

print(
  '\nO total à pagar é R${:.2f}'
  .format(60 * d + 0.15 * km)
)