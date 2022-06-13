name = input('What is your name? ')
print('Pleasure to meet you, {:!^20}'.format(name))
n1 = int(input('Um valor = '))
n2 = int(input('Outro valor ='))
s = n1 + n2
m = n1*n2
d = n1 / n2
di = n1 // n2
e = n1**n2
print('Sum is {}, \nproduct is {} and \ndivision is {}.'.format(s,m,d),end=' !!! ')
print('Integer division is {} and power is {}.'.format(di,e))