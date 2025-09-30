# pra esse dá pra usar formatação da string tbm
# mas pensando em treinar o import, vou usar a função trunc

from math import trunc

n = float(input('Digite um número: '))

print('\nO número {} tem a parte inteira {}'.format(n, trunc(n)))