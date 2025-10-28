print('Dê informações sobre quatro pessoas:')

somaIdades = 0
homemMaisVelho = ['', 0]
mulheresMenoridade = 0

for c in range(1, 5):
  print('==Pessoa {}=='.format(c))
  nome = input('Nome: ')
  idade = int(input('Idade: ' ))

  while idade < 0:
    idade = int(input('Idade inválida. Digite novamente: '))

  genero = input('Gênero [NB/F/M]: ').upper()

  somaIdades += idade

  if (genero == 'M') & (idade > homemMaisVelho[1]):
      homemMaisVelho = [nome, idade]
  elif (genero == 'F') & (idade < 20):
      mulheresMenoridade += 1

print("""
* Média de idades: {:.1f}
* Homem mais velho: {} ({} anos)
* Mulheres com menos de 20 anos: {}
""".format(
  somaIdades / 4,
  homemMaisVelho[0], homemMaisVelho[1],
  mulheresMenoridade
))
