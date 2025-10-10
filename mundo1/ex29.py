km = float(input('Quantos Km/h o carro está andando? '))

print(
  '\nUltrapassou o limite!\nRecebeu uma multa no valor de R${:.2f}'
  .format((km - 80) * 7) if km > 80
  else '\nTudo OK!'
)
