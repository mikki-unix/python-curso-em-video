from random import randint
from time import sleep

print('='*25)
print('{:^25}'.format('Jogo da Adivinhação!'))
print('='*25)

sleep(2)
computador = randint(0, 10)
print('Pensei num número entre 0 e 10. Tente adivinhar qual ele é!')
sleep(2)
jogador = int(input('Digite seu chute: '))
tentativas = 1

while jogador != computador:
  jogador = int(input('Errou! Digite outro chute: '))
  tentativas += 1

if tentativas == 1:
  print('\nCaraca, de primeira! Você tem muita sorte!')
elif tentativas <= 5:
  print(
    '\nIsso, eu pensei no {}!\nVocê conseguiu acertar em {} tentativas!'
    .format(computador, tentativas)
  )
elif tentativas <= 10:
  print(
    '\nCerto, pensei em {}!\nMas, nossa, foram algumas tentativas, hein?\n{} para ser exato!'
    .format(computador, tentativas)
  )
else:
  print(
    '\nCorreto, {}!'
    '\nEita... parece que passamos por todos os números até acertar!'
    '\nAo todo, foram {} tentativas'
    .format(computador, tentativas)
  )
