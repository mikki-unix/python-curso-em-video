from random import randint
from time import sleep

print('Vamos jogar jokenpô!')

jogadas = [
  'PEDRA', 'PAPEL', 'TESOURA'
]

resultados = [
  ['Empate!', 'Eu venci!', 'Você venceu!'],
  ['Você venceu!', 'Empate!', 'Eu venci!'],
  ['Eu venci!', 'Você venceu!', 'Empate!']
]

jogarDeNovo = 1

while jogarDeNovo == 1:
  jogador = int(input(
    '\nEscolha o que jogar:\n'
    '1 - Pedra | 2 - Papel | 3 - Tesoura\n'
  )) - 1

  while (jogador < 0) or (jogador > 2):
    jogador = int(input('Opção inválida. Escolha novamente: ')) - 1

  computador = randint(0,2)

  print('\nJO-KEN-PÔ...!')
  sleep(1.5)
  print(
    'Você jogou {} e eu joguei {}'
    .format(jogadas[jogador], jogadas[computador])
  )
  sleep(1.5)
  print(resultados[jogador][computador])
  sleep(2)

  jogarDeNovo = int(input('\nQuer jogar de novo?\n1 - Sim | 2 - Não\n'))

  while (jogarDeNovo < 1) or (jogarDeNovo > 2):
    jogarDeNovo = int(input('Opção inválida. Escolha novamente: '))

  if jogarDeNovo == 1: print('\nOkay, então vamos mais uma vez!')

print('\nFoi bom jogar com você!')
