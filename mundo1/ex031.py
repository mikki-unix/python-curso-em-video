distancia = float(input('Qual a distância da viagem (em Km)? '))

cobranca = 0.50 if distancia <= 200.0 else 0.45

print(
  'A passagem vai custar R${:.2f}'
  .format(cobranca * distancia)
)
