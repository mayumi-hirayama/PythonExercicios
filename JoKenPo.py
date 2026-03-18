from random import randint
from time import sleep

cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31m',
         'amarelo': '\033[1;33m',
         'verde': '\033[1;32m'}

opcoes = ('Pedra', 'Papel', 'Tesoura')
comput = randint(0, 2)
print('''Escolha:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input(''))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)

if jogador == comput:
    print('{}EMPATE!{} Eu também escolhi {}.'.format(cores['amarelo'], cores['limpa'], opcoes[comput]))
elif jogador == 0: #PEDRA
   if comput == 1:
       print('{}PERDEU!{} Eu escolhi {}!'.format(cores['vermelho'], cores['limpa'], opcoes[comput]))
   elif comput == 2:
       print('{}GANHOU!{} Eu escolhi {}.'.format(cores['verde'], cores['limpa'], opcoes[comput]))
elif jogador == 1: #PAPEL
    if comput == 0:
        print('{}GANHOU!{} Eu escolhi {}.'.format(cores['verde'], cores['limpa'], opcoes[comput]))
    elif comput == 2:
        print('{}PERDEU!{} Eu escolhi {}!'.format(cores['vermelho'], cores['limpa'], opcoes[comput]))
elif jogador == 2: #TESOURA
    if comput == 0:
        print('{}PERDEU!{} Eu escolhi {}!'.format(cores['vermelho'], cores['limpa'], opcoes[comput]))
    elif comput == 1:
        print('{}GANHOU!{} Eu escolhi {}.'.format(cores['verde'], cores['limpa'], opcoes[comput]))
else:
    print('{}Escolha inválida.{}'.format(cores['vermelho'], cores['limpa']))