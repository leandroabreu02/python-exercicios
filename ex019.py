# Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escolhendo o nome do escolhido
import random
aluno1 = str(input('O primeiro aluno: '))
aluno2 = str(input('O segundo aluno: '))
aluno3 = input('O terceiro aluno: ')
aluno4 = input('O quarto aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
sorteado = random.choice(alunos)
print('O aluno escolhido foi {}'.format(sorteado))