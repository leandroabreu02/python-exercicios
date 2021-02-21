# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais
palavras  = ('Areia', 'Bota', 'Canivete', 'Dado', 'Escova', 'Folha', 'Galho', 'Hipogrifo', 'Isca', 'Jaleco', 'Kiwi', 'Ladeira')
for p in palavras:
  print(f'\nNa palavra {p.upper()} temos ', end='')
  for letra in p:
    if letra.lower() in 'aeiou':    # para suportar acento: 'aáâàeéêèiíîìoóôòuúûù'
      print(letra, end=' ')



