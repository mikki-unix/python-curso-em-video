from random import randint

ram = randint(0, 5)
print('Tente adivinhar o número escolhido!\nEntre 0 a 5, qual número acha que é?')
chute = int(input('\nDigite um número: '))

print('\nVocê acertou!' if chute == ram else '\nErrou! Tenta outra vez!')
