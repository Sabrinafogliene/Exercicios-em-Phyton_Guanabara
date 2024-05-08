#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip().upper()
print('Na frase a letra "A" aparece {} vezes.'.format(frase.count('A')))
print('A primeira posição em que o "A" aparece é a {}'.format(frase.find('A')))
print('A última posição em que o "A" aparece é a {}'.format(frase.rfind('A')))