c = float(input('Digite a temperatura em ºC: '))
print(
  '\n{:.1f}ºC correspondem à {:.1f}ºF'
  .format(c, c * 9/5 + 32)
)