#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
#dólares ela pode comprar.
#dólar dia 13/06/2022: 1 dólar = 5.11 reais
reais = float(input('Quantos reais você tem na carteira? '))
dolares = reais/5.11
print('Você pode comprar {:.2f} dólar(es) com {:.2f} real(is).'.format(dolares,reais))