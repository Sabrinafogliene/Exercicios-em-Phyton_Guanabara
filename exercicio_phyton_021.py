#Faça um programa em phyton que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('ex_021.mp3')
pygame.mixer.music.play()
pygame.event.wait()