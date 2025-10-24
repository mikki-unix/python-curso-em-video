precoOriginal = float(input('Valor do produto: R$'))
opcao = int(input("""
Escolha uma opção de pagamento:
1 - Dinheiro físco ou Cheque
2 - Cartão de crédito
"""))

while (opcao < 1) or (opcao > 2):
  opcao = int(input('Opção inválida. Escolha novamente: '))

if opcao == 1:
  precoFinal = precoOriginal - (precoOriginal * 0.1)
else:
  parcelas = int(input('Em quantas vezes? '))

  while parcelas < 1:
    parcelas = int(input('Número inválido. Digite novamente: '))

  precoFinal = precoOriginal - (precoOriginal * 0.05)
  if parcelas == 2:
    precoFinal = precoOriginal
  elif parcelas >= 3:
    precoFinal = precoOriginal + (precoOriginal * 0.20 * parcelas)

print('\nO preço final será de R${:.2f}'.format(precoFinal))
