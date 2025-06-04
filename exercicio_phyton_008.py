#Escreva um programa que leia um valor em metros e o exiba convertido em kilômetros, hectômetros, decâmetros, decímetros, centímetros e milímetros.
#medida = float(input('Uma distância em metros: '))
#km = medida * 0.001
#hm = medida * 0.01
#dam = medida * 0.1
#dm = medida * 10
#cm = medida * 100
#mm = medida * 1000

#print('A medida de {}m corresponde a {}km, {}hm, {}dam, {}dm, {}cm e {}mm'.format(medida, km, hm, dam, dm, cm, mm)) # {:.0f} caso queira retirar a exibição das casas depois da vírgula.
medida = float(input('Digite uma distância em metros: '))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {}km, {}hm, {}dam, {}dm, {}cm, {}mm .'.format(medida, km, hm, dam, dm, cm, mm))
