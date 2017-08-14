import pygame
from game import Game

pygame.init()

clock = pygame.time.Clock()
FPS = 25

g = Game()

def start():
	while True:

		g.update()

		pygame.display.update()
		clock.tick(FPS)

start()	