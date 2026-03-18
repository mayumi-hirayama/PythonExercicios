cores = {'limpa': '\033[m',
         'amarelo': '\033[1;33m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m'}

peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite sua altura em m: '))

imc = peso / (altura * altura)
print('Seu IMC é de {:.1f}'.format(imc))

if imc < 18.5:
    print('{}Abaixo do peso.{}'.format(cores['amarelo'], cores['limpa']))
elif imc > 18.5 and imc <=25:
    print('{}Peso ideal.{}'.format(cores['verde'], cores['limpa']))
elif imc > 25 and imc <= 30:
    print('{}Sobrepeso.{}'.format(cores['amarelo'], cores['limpa']))
elif imc > 30 and imc <= 40:
    print('{}Obesidade.{}'.format(cores['vermelho'], cores['limpa']))
elif imc > 40:
    print('{}Obesidade mórbida.{}'.format(cores['vermelho'], cores['limpa']))