dinheiro=float(input('Informe o valor em reais: R$ '))
dolar = dinheiro/6.05
print('Com R${:.2f} é possível comprar US${:.2f}.'.format(dinheiro, dolar))