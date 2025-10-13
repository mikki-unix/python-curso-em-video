salario = float(input('Digite o salário do funcionário: '))

aumento = 10 if salario > 1250.00 else 15

print(
  'Com um aumento de {}%, seu salário agora é de R${:.2f}'
  .format(aumento, salario + aumento / 100 * salario)
)