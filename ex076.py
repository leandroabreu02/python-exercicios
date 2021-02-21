# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência
# No final, mostre uma listagem de preços, organizando os dados em forma tabular
produtos = ('Mouse', 29.90, 
            'Teclado', 68.90,
            'Monitor', 200, 
            'Processador', 600, 
            'Placa de vídeo', 699, 
            'Placa mãe', 349.90,
            'Memória Ram', 399.90,
            'Cooler', 209.90,
            'SSD', 479.90,
            'HD', 269.90,
            'Fonte', 390.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(produtos)):
  if pos % 2 == 0:
    print(f'{produtos[pos]:.<30}', end='')
  else:
    print(f'R${produtos[pos]:>7.2f}')
print('-' * 40)
