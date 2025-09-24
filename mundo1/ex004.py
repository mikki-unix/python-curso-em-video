valor = input('Digite algo: ')

print('\nSó espaços?', valor.isspace())
print('É um número?', valor.isnumeric())
print('É alfabético?', valor.isalpha())
print('É alfanumérico?', valor.isalnum())
print('Está em maiúsculas?', valor.isupper())
print('Está em minúsculas?', valor.islower())
print('Está capitalizado?', valor.istitle())