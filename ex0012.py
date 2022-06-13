#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
precoAtual = float(input('Digite o preço atual do produto, em reais: R$'))
precoDesconto = 0.95*precoAtual
print('O preço desse produto com desconto de 5% é de R${:.2f}.'.format(precoDesconto))