# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# ex: leandro cardoso abreu
# primeiro = leandro
# último = abreu
nome = input('Qual seu nome completo? ')
primeiro_nome = (nome.split())
ultimo_nome = (nome.split())
print(primeiro_nome[0])
print(ultimo_nome[-1])