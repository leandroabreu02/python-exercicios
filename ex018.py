# Faça um programa que leia um ãngulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
angulo = float(input('Digite um ângulo qualquer em grau: '))
radiano = (angulo / 180) * math.pi
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)
print('O ângulo {}° tem {:.2f} de seno, {:.2f} de cosseno e {:.2f} de tangente'.format(angulo, seno, cosseno, tangente))




# pi radiano = 180 graus