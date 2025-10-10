c = input('Digite o nome da sua cidade: ').strip()

print(
  '\nComeça com Santo? {}'
  .format(
    # 'santo' in c.lower().split()[0]
    c.lower()[:5] == 'santo'
  )
)
