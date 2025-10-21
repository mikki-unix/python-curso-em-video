precoOriginal = float(input('Valor do produto: R$'))
opcao = int(input("""
Escolha uma opção de pagamento:
1 - Dinheiro físco ou Cheque
2 - Cartão de crédito
"""))

if opcao == 1:
  precoFinal = precoOriginal - (precoOriginal * 0.1)
else:
  parcelas = int(input('\nEm quantas vezes? '))

  precoFinal = precoOriginal - (precoOriginal * 0.05)
  if parcelas == 2:
    precoFinal = precoOriginal
  elif parcelas >= 3:
    precoFinal = precoOriginal + (precoOriginal * 0.20 * parcelas)

print('\nO preço final será de R${:.2f}'.format(precoFinal))
