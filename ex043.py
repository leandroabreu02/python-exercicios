# Desenvolva um lógica que leia o peso e a altura de uma pessoa, calcule seu imc e mostre seu status, de acordo com a tabela abaixo
# - abaixo de 18.5: abaixo do pesso
# - entre 18.5 e 25: peso ideal
# - 25 até 30: sobrepeso
# - 30 até 40: obesidade
# - acima de 40: obesidade mórbida
peso = float(input('Qual seu peso em Km? '))
altura = float(input('Qual sua altura em m? '))
imc = peso / (altura ** 2)
if imc < 18.5:
  print('Seu imc deu {:.2f}, você está abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
  print('Seu imc deu {:.2f}, você está no peso ideal'.format(imc))
elif 25 <= imc < 30:
  print('Seu imc deu {:.2f}, você está com sobrepeso'.format(imc))
elif 30 <= imc < 40:
  print('Seu imc deu {:.2f}, você está com obseidade'.format(imc))
else:
  print('Seu imc deu {:.2f}, você está com obesidade mórbida'.format(imc))