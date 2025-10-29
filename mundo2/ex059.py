menu = """
Escolha uma opção:
[1] Somar
[2] Multiplicar
[3] Encontrar o maior
[4] Digitar outros números
[5] Encerrar o programa
"""

opcao = -1
while opcao != 5:
  n = [
    float(input('Digite um número: ')),
    float(input('Digite outro número: '))
  ]
  opcao = -1

  while (opcao != 4) & (opcao != 5):
    print(menu)

    opcao = int(input('Digite sua escolha: '))

    while (opcao < 1) | (opcao > 5):
      opcao = int(input('Opção inválida. Digite novamente: '))

    if opcao == 1:
      print('\nA soma entre eles é: {:.1f}'.format(n[0] + n[1]))
    elif opcao == 2:
      print('\nA multiplicação é: {:.1f}'.format(n[0] * n[1]))
    elif opcao == 3:
      print('\nO maior número é: ', end='')
      if n[0] > n[1]:
        print(n[0])
      else:
        print(n[1])
