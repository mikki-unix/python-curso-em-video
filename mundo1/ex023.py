n = int(input('Digite um número entre 0 e 9999: '))

while n < 0 | n > 9999:
  n = int(input('Inválido. Digite um número entre 0 e 9999: '))

print("""
* Milhares: {}
* Centenas: {}
* Dezenas: {}
* Unidades: {}
"""
.format(
  n // 1000 % 10,
  n // 100 % 10,
  n // 10 % 10,
  n % 10,
)
)