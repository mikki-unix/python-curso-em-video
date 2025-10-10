n = input('Digite o nome completo de uma pessoa: ').strip()

print(
  '\nEssa pessoa é um ou uma Silva? {}'
  .format('silva' in n.lower())
)