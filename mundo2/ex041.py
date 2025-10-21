from datetime import date

nasc = int(input('Insira o ano de nascimento do(a) atleta: '))

idade = date.today().year - nasc

categoria = 'MASTER'
if idade <= 9: categoria = 'MIRIM'
elif idade <= 14: categoria = 'INFANTIL'
elif idade <= 19: categoria = 'JUNIOR'
elif idade <= 20: categoria = 'SÊNIOR'

print('\nAtlela possui {} anos, e está na categoria {}'.format(idade, categoria))
