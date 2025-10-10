n = input('Escreva seu nome completo: ').strip()

print("""
* Maiúsculo: {}
* Minúsculo: {}
* Qtd letras: {}
* Qtd letras primeiro nome: {}
"""
.format(
  n.upper(),
  n.lower(),
  len(n.replace(' ', '')),
  #n.find(' ')
  len(n.split()[0])
)
)