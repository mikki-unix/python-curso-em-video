from random import choice

alunos = [
  input('Aluno(a) 1: '),
  input('Aluno(a) 2: '),
  input('Aluno(a) 3: '),
  input('Aluno(a) 4: ')
]

print(
  '\nQuem deve apagar o quadro é {}.'
  .format(choice(alunos))
)