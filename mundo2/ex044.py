precoOriginal = float(input('Valor das compras: R$'))
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

  if parcelas > 1:
    precoFinal = precoOriginal

    if parcelas >= 3:
      print('Será aplicado juros de 20% por parcela')
      precoFinal = precoOriginal + (precoOriginal * 0.20 * parcelas)

    print('A compra foi divida em {} vezes de R${:.2f}'.format(parcelas, precoFinal / parcelas))

print('Sua compra de R${:.2f} terá o valor final de R${:.2f}'.format(precoOriginal, precoFinal))
