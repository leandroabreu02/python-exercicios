# Faça um program que leia o comprimento do catedo oposto e do cateto adjacente de um triângulo retângulo, calcule e motre o comprimento da hipotenusa
import math
oposto = float(input('Quanto vale o cateto oposto? '))
adjacente = float(input('Quanto vale o cateto adjacente? '))
hipotenusa = math.sqrt(oposto ** 2 + adjacente ** 2)
print('A hipotenusa do triângulo vale {:.2f}'.format(hipotenusa))