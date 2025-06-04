#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e com todas as letras minúsculas;
#Quantas letras ao todo (sem considerar os espaços);
#Quantas letras tem o primeiro nome.
#nome = str(input('Digite seu nome completo: ')).strip()
#print('Analisando seu nome...')
#print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
#print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
#print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#dividido = nome.split()
#print('Seu primeiro nome é {} e ele tem {} letras.'.format(dividido[0], len(dividido[0])))

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
dividido = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(dividido[0], len(dividido[0])))