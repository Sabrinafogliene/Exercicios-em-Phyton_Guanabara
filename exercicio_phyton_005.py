#Faça um programa que leia um número e mostre na tela o seu sucessor e o seu antecessor.
n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s)) #usando 3 varáveis
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1))) #usando apenas uma variável