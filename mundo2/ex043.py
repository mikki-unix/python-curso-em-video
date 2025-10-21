peso = float(input('Digite seu peso (em kg): '))
altura = float(input('Digite sua altura (em metros): '))

imc = peso / altura ** 2

avaliacao = 'Obesidade grau III'
if imc < 18.5: avaliacao = 'Magreza'
elif imc < 25: avaliacao = 'Peso normal'
elif imc < 30: avaliacao = 'Sobrepeso'
elif imc < 35: avaliacao = 'Obesidade grau I'
elif imc < 40: avaliacao = 'Obesidade grau II'

print('\nIMC: {:.1f} - {}'.format(imc, avaliacao))
