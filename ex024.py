# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
cidade = input('Digite o nome de uma cidade: ').strip()
primeiro_nome = (cidade.split())[0]
primeiro_nome_minusculo = primeiro_nome.lower()
tem_santos = 'santo' in primeiro_nome_minusculo
print('Tem Santo? {}'.format(tem_santos)) 