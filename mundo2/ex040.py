notas = [
  float(input('Digite a nota 1: ')),
  float(input('Digite a nota 2: '))
]

media = (notas[0] + notas[1]) / 2
avaliacao = 'APROVADO(A)'

if media < 5.0:
  avaliacao = 'REPROVADO(A)'
elif media < 7.0:
  avaliacao = 'RECUPERAÇÃO'

print('\nMédia: {:.1f} - {}'.format(media,avaliacao))
