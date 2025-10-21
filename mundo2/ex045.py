from time import sleep
from random import randint

print('Vamos jogar jokenpô!')

jogadas = [
  'PEDRA', 'PAPEL', 'TESOURA'
]

resultados = [
  ['Empate!', 'Eu venci!', 'Você venceu!'],
  ['Você venceu!', 'Empate!', 'Eu venci!'],
  ['Eu venci!', 'Você venceu!', 'Empate!']
]

while True:
  jogador = int(input(
    '\nEscolha o que jogar!\n'
    '1 - Pedra | 2 - Papel | 3 - Tesoura\n'
  )) - 1
  computador = randint(0,2)

  print('\nJO-KÊN-PO...!')
  sleep(1.5)
  print(
    'Você jogou {} e eu joguei {}'
    .format(jogadas[jogador], jogadas[computador])
  )
  sleep(1.5)
  print(resultados[jogador][computador])
  sleep(2)

  if int(input('\nQuer jogar de novo?\n1 - Sim | 2 - Não\n')) == 2: break
  else: print('\nOkay, então vamos mais uma vez!')

print('\nFoi bom jogar com você!')
