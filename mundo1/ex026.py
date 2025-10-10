frase = input('Digite uma frase: ').lower()

print("""
* Quantidade de letras A na frase: {}
* Primeira letra A está na posição: {}
* Última letra A está na posição: {} 
"""
.format(
  frase.count('a'),
  frase.find('a')+1,
  frase.rfind('a')+1
)
)