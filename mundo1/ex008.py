m = int(float('Digite um valor em metros: '))

print(
  '\nConvertendo em outras medidas, temos:'
  '\n* {:.0f} cm'
  '\n* {:.0f} mm'
  .format(m*100, m*1000)
)