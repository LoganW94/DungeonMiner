import pygame
from game import Game

pygame.init()

clock = pygame.time.Clock()
FPS = 60

g = Game()

def start():
	while True:
		g.run_game()	

		pygame.display.update()
		clock.tick(FPS)

start()	