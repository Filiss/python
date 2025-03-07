import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo MP3
import os

if os.path.exists("desa021.mp3"):
    pygame.mixer.music.load("desa021.mp3")
else:
    print("Arquivo MP3 não encontrado.")
    exit()

# Toca o arquivo MP3
pygame.mixer.music.play()

# Mantém o programa rodando enquanto a música toca
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)