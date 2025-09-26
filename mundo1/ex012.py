p = float(input('Digite o preço de um produto: '))

print(
  '\nCom um desconto de 5%...'
  '\nEsse produto custa R${:.2f} !'
  .format(p - (p*0.05))
)