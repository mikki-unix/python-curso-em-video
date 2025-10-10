from random import shuffle

alunos = [
  input('Aluno(a) 1: '),
  input('Aluno(a) 2: '),
  input('Aluno(a) 3: '),
  input('Aluno(a) 4: ')
]

shuffle(alunos)

print(
  '\nOs trabalhos serão apresentados nesta ordem:\n{}'
  .format(alunos)
)