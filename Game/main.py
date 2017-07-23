import pygame
from world import World
from user_input import User_Input
from draw_world import Draw_World

pygame.init()

clock = pygame.time.Clock()
FPS = 60

w = World()
u_input = User_Input()
d = Draw_World(w) 

def start():

	while True:

		w.update(u_input.get_input())

		d.draw()

		pygame.display.update()
		clock.tick(FPS)

start()	