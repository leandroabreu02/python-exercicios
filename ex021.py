# Faça um program em python que abra e reproduza áudio de um arquivo mp3

# Player de música
import pygame

stop = True
while stop == True:
  pygame.mixer.init()
  pygame.init()
  pygame.mixer.music.load('ex021.mp3')
  pygame.mixer.music.play()
  input()
  pygame.event.wait()
  cont = input('Deseja parar a música (s/n)? ')
  if cont == "s":
    stop= False

