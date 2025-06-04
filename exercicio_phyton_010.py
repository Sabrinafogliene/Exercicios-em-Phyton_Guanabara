#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares e quantos euros ela pode comprar.

#real = float(input('Quanto dinheiro você tem na carteira? R$'))
#dolar = real / 5.19
#euro = real / 5.54
#print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
#print('Com R${:.2f} você pode comprar EUR{:.2f}'.format(real, euro))
#===========================================================
real = float(input('Quanto dinheiro você tem na carteira: R$'))
dolar = real / 5.63
euro = real / 6.44
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar EUR{:.2f}'.format(real, euro))