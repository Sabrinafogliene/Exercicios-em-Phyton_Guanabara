#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
##Ex:Digite um número: 6.127
###O número 6.127 tem a parte inteira 6.

#import math - importação completa
#from math import trunc - importação específica
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua parte inteira é {}'.format(num,trunc(num)))

#print('O valor digitado foi {} e a sua parte inteira é {}'. format(num, int(num))) - uma forma de resolver sem importar função.