cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31m',
         'verde': '\033[1;32m'}

valor = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Qual o valor da renda? R$'))
anos = int(input('Em quantos anos deseja pagar? '))

#prestação não pode exceder 30% da renda

prestacao = valor / (anos * 12)
if prestacao > (salario * 0.30):
    print('{}Empréstimo negado.{}\nValor das prestações: R${:.2f}'.format(cores['vermelho'], cores['limpa'], prestacao))
else:
    print('{}Empréstimo aprovado!{}\nValor das prestações: R${:.2f}'.format(cores['verde'], cores['limpa'], prestacao))