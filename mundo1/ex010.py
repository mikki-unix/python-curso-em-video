r = int(input('Quantos R$ você possui? '))

print(
  '\nConsiderado que em 2017 um dólar era igual à R$3,27...'
  '\nVocê poderia comprar {:.0f} dólares!'
  .format(r//3.27)
)