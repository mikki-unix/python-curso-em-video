a = int(input('Digite um ano qualquer: ' ))

print(
  a,
  'é um ano bissexto'
  if (a % 4 == 0) & (a % 100 == 0)
  else 'não é um ano bissexto'
)
