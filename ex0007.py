#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
nome = input('Digite o nome de estudante: ')
n1 = float(input('Digite a primeira nota de {}: '.format(nome)))
n2 = float(input('Digite a segunda nota de {}: '.format(nome)))
media = (n1+n2)/2
print('A média de {} é {}.'.format(nome,media))
