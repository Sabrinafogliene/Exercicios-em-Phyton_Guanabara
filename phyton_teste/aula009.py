frase = 'Curso em Vídeo Phyton'
print(frase[:13])
# para exibir textos longos usa-se 3 aspas """ no começo e no final.
print(len(frase))
print(frase.upper())
print(frase.lower())
print(frase.replace('Phyton', 'Android'))#substitui temporariamente. Pra substituir definitivamente, tem q usar atribuição e o replace
print('Curso' in frase)
dividido = frase.split()
print(dividido)
print(dividido[1])