n = input('Digite o nome completo de uma pessoa: ').strip().split()

print("""
* Primeiro nome: {}
* Segundo nome: {}
"""
.format(n[0], n[len(n)-1])
)