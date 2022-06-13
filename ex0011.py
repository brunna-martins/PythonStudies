#Programa que leia largura e altura de uma parede em metros.
#Calcular a área e a quantidade de tinta necessária para pintá-la sabendo que
#cada litro de tinta pinta uma área de 2m^2.
largura = float(input('Digite a largura da sua parede, em metros: '))
altura = float(input('Digite a altura da sua parede, em metros: '))
areaParede = largura*altura
tintaNecessaria = areaParede/2
print('A área da sua parede é de {} metro(s) quadrado(s) e, por isso, você gastará {} litro(s) de tinta.'.format(areaParede,tintaNecessaria))