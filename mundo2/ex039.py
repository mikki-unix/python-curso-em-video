from datetime import date

nasc = int(input('Digite o ano de nascimento de um jovem, para saber se ele deve se alistar:\n'))

idade = date.today().year - nasc

if idade < 18:
  print('\nEle tem {} anos de idade, faltam {} anos para precisar se alistar'.format(idade, 18 - idade))
elif idade == 18:
  print('\nJá possui 18 anos, portanto deve se alistar')
else:
  print('\nEle tem {} anos. Se ainda não se alistou, está {} anos atrasado'.format(idade, idade - 18))