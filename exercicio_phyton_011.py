#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua àrea e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
#larg = float(input('Largura da parede: '))
#alt = float(input('Altura da parede: '))
#área = larg * alt
#print('Sua parede tem a dimensão de {}x{} e sua àrea é de {}m².'.format(larg, alt, área))
#tinta = área / 2
#print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))
#===================================
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {} x {} e a sua área é de {}m².'.format(larg, alt, area))
tinta = area/2
print('Para pintar essa parede, será necessário {}l de tinta'.format(tinta))