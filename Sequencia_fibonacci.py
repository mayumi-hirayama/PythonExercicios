from time import sleep
print('-' * 22)
print('Sequência de Fibonacci')
print('-' * 22)
termo = int(input('Quantos termos deseja mostrar: '))
fib1 = 0
fib2 = 1
print(fib1, fib2, end=' ')
sleep(0.6)
while termo > 0:
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
    termo = termo - 1
    print(fib3, end=' ')
    sleep (0.6)