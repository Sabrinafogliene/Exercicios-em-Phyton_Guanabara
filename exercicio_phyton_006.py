#Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e a sua raiz quadrada.
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** 2
print ('O dobro de {} vale {}.\nO triplo de {} vale {}.\nA raiz quadrada de {} é igual a {}.'.format(n, d, n, t, n, r)) #4 variáveis
print ('O dobro de {} vale {}.\nO triplo de {} vale {}.\nA raiz quadrada de {} é igual a {}.'.format(n, (n*2), n, (n*3), n, (n**2))) #uma variável