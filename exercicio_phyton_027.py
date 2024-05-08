#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex:Ana Maria de Souza
#primeiro = Ana
#último = Souza
nome = str(input('Digite seu nome completo: ')).strip()
primeiro = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {} e seu último nome é {}'.format(primeiro[0], primeiro[len(primeiro)-1]))