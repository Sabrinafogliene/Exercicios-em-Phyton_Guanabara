#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
#salário = float(input('Qual é o salário do funcionário? R$'))
#novo = salário + (salário * 15 / 100)
#print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))

salário = float(input('Qual o valor do salário do funcionário? R$'))
novo = salário + (salário * 15/100)
print('Um funcionário que ganhava R${:.2f}, vai passar a ganhar R${:.2f}'.format(salário, novo))