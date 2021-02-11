# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
media = (nota1+nota2)/2
print('A nota média entre {:.1f} e {:.1f} é {:.1f}'.format(nota1, nota2, media))