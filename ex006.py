# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)      # raiz = pow(numero, (1/2))
print('O dobro de {} vale {}'.format(numero, dobro))
print('O triplo de {} vale {}. \nA raiz de {} vale {:.2f}'.format(numero, triplo, numero, raiz))