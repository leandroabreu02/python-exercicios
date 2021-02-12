# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado
dias = float(input('Quantidade de dias alugado: '))
km = float(input('Quantidade de km rodados: '))
total_pagar = dias * 60 + km * 0.15
print('O total a pagar é R$ {:.2f}'.format(total_pagar))