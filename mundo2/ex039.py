from datetime import date

nasc = int(input('Digite o ano de nascimento de um jovem,\npara saber se ele deve se alistar:\n'))
atual = date.today().year
idade = atual - nasc

if idade < 18:
  diff = 18 - idade
  print(
    '\nEle tem {} anos de idade. Faltam {} anos para precisar se alistar'
    '\nSeu ano de alistamento será em {}'
    .format(idade, diff, atual + diff)
  )
elif idade == 18:
  print('\nJá possui 18 anos, portanto deve se alistar este ano')
else:
  diff = idade - 18
  print(
    '\nEle tem {} anos. Se ainda não se alistou, está {} anos atrasado'
    '\nSeu ano de alistamento foi em {}'
    .format(idade, diff, atual - diff)
  )