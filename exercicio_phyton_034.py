#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para salários inferiores ou iguais, o aumento é de 15%.
salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    salárioNovo = salário + (salário * 15 / 100)
else:
    salárioNovo = salário + (salário * 10 / 100)

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salário, salárioNovo))