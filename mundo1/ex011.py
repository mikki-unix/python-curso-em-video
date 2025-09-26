print('Programa para calcular a quantidade de tinta necessária para pintar paredes!', end='\n\n')

l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura, também em metros: '))

print(
  '\nA área da parede é de {:.1f}m²'
  '\nSerá necessário {:.1f}L de tinta para pintá-la'
  .format(l*a, (l*a)/2)
)