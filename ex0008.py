#Programa que leia valor em metros e o exiba convertido em centímetros e milímetros.
valorM = float(input('Digite um valor em metros: '))
valorCm = valorM*100
valorMm = valorM*1000
print('Valor em centímetros: {}cm.\nValor em milímetros: {}mm.'.format(valorCm,valorMm))