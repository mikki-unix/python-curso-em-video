casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário do comprador: '))
anos = int(input('Digite em quantos anos pretende pagar: '))

parcelas = 12 * anos
mensalidade = casa / parcelas

if mensalidade > salario * 0.3:
  print('\nEmpréstimo negado.\nO preço de R${:.2f} por parcela supera 30% do salário do comprador'.format(mensalidade))
else:
  print('\nEmpréstimo aprovado!\nDeverá pagar {} parcelas no valor de R${:.2f}'.format(parcelas, mensalidade))