import pygame
pygame.mixer.init()
pygame.mixer.music.load('ms021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('Agora você escuta?') 