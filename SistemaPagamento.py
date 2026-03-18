valor = float(input('Digite o valor do produto: R$'))
print('''Selecione a forma de pagamento: 
[1] À vista, dinheiro ou PIX
[2] À vista, no cartão
[3] Parcelado''')
pag = int(input(''))

if pag == 1:
    total = valor - (valor * 0.10)
    print('Valor à pagar, com 10% de desconto: R${:.2f}'.format(total))
elif pag == 2:
    total = valor - (valor *0.05)
    print('Valor à pagar, com 5% de desconto: R${:.2f}'.format(total))
elif pag == 3:
    parcela = int(input('Parcelar em quantas vezes? '))
    if parcela == 2:
        print('Valor à pagar: R${:.2f}'.format(valor))
    elif parcela >= 3:
        total = valor + (valor *0.20)
        print('Valor à pagar, com 20% de juros: R${:.2f}'.format(total))