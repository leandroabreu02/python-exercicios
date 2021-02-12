# Escreva um programa que converta uma temperatura digitada em °C e converta para °F
celsius = float(input('Informe a temperatura em °C '))
fahrenheit = (celsius * 9/5 + 32)
print('A temeperatura de {0}°C corresponde a {1}°F!'.format(celsius, fahrenheit))