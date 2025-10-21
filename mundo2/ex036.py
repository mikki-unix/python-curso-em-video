casa = float(input('Valor da casa R$'))
salario = float(input('Salário do comprador R$'))
anos = int(input('Em quantos anos pretende pagar? '))

parcelas = 12 * anos
prestacao = casa / parcelas

if prestacao > salario * 0.3:
  print('\nEmpréstimo negado.\nA prestação de R${:.2f} supera 30% do salário do comprador'.format(prestacao))
else:
  print('\nEmpréstimo aprovado!\nDeverá pagar {} prestações no valor de R${:.2f}'.format(parcelas, prestacao))