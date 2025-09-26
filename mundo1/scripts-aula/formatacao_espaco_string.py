palavra = input('Digite algo: ')

# : é o início da especificação da formatação
# ~ foi o carácter que escolhi para preencher o espaço
# <^> define a direção em que a string deve ficar
# o número no final define o espaço total do campo em que a string será exibida
print('\nÀ esquerda: \n{:~<20}'.format(palavra))
print('\nCentralizado: \n{:~^20}'.format(palavra))
print('\nÀ direita: \n{:~>20}'.format(palavra))