s = float(input('Digite seu salário: '))

print(
  '\nCom 15% de aumento...'
  '\nSeu salário é seria de R${:.2f} !'
  .format(s + (s*0.15))
)