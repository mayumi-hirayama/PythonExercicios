cores = {'limpa':'\033[m',
         'verde':'\033[32m',
         'vermelho':'\033[31m'}
from random import randint
from time import sleep
num = randint(0, 5)
print('Vou pensar  em um número entre 0 e 5. Tente adivinhar...')
chute = int(input('Que número eu pensei? '))
if chute == num:
    print('PROCESSANDO...')
    sleep(3)
    print('{}Parabéns, você ganhou! Eu pensei no número {}.{}'.format(cores['verde'], num, cores ['limpa']))
else:
    print('PROCESSANDO...')
    sleep(3)
    print('{}Perdeu! Eu pensei no número {}. Tente novamente.{}'.format(cores['vermelho'], num, cores['limpa']))