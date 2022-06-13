#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com
#15% de aumento.
salarioAtual = float(input('Digite seu salário atual, em reais: R$'))
salarioAumento = salarioAtual*1.15
print('Seu salário, com 15% de aumento, é de R${:.2f}'.format(salarioAumento))