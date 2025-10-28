from datetime import date

print('Digite o ano de nascimento de sete pessoas:')

atual = date.today().year
menoridade = 0
maioridade = 0
for c in range(1, 8):
  pessoaAtual = 'Pessoa {}: '.format(c)
  anoPessoa = int(input(pessoaAtual))

  idade = atual - anoPessoa
  if idade > -1:
    if idade >= 21:
      maioridade += 1
    else:
      menoridade += 1

print("""
Quantidade de pessoas com...
* Pelo menos 21 anos: {}
* Menos de 21 anos: {}
""".format(maioridade, menoridade))
