import pygame
from world import World
from user_input import User_Input
from draw_world import Draw_World

pygame.init()

clock = pygame.time.Clock()
FPS = 60

w = World()
u_input = User_Input()
d = Draw_World() 

def start():

	gameExit = False

	while not gameExit:

		u_input.get_input()

		w.update(u_input.direction)

		d.draw()

		pygame.display.update()
		clock.tick(FPS)

start()	