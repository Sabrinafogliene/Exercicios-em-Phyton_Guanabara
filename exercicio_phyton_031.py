#Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
'''Minha primeira resolução
km = float(input('Qual a distância da sua viagem? '))
pc = km * 0.50
pl = km * 0.45
print('Você está prestes a começar uma viagem de {:.1f}km'.format(km))
if km <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(pc))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(pl))'''

#Resolução em aula
distância = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))


'''Resolução simplificada 
distância = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))'''

