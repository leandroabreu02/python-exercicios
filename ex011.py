# Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de inta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
area = altura * largura
tinta = area / 2
print('A parede tem área {}m² e pede {}l de tinta para pintar completamente'.format(area, tinta))