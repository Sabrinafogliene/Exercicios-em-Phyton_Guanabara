#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado.
alugado = int(input('Quantos dias alugados? '))
kmrodados = float(input('Quantos Km rodados? '))
pagar = (alugado * 60) + (kmrodados * 0.15)
print('O total a pagar é de R${:.2f}'.format(pagar))