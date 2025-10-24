n = int(input('Digite um número inteiro na base decimal: '))

escolha = int(input("""
Escolha a base para conversão:
1 - Binário
2 - Octal
3 - Hexadecimal
""")) - 1

while (escolha < 0) or (escolha > 2):
  escolha = int(input('Opção inválida. Escolha novamente: ')) - 1

if escolha == 0: c = bin(n)
elif escolha == 1: c = oct(n)
else: c = hex(n)

bases = ['BINÁRIO', 'OCTAL', 'HEXADECIMAL']

print('\nO número decimal {} convertido para {} é igual à {}'.format(n, bases[escolha], c[2:]))
