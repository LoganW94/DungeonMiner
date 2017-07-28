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

	while True:
		#ai = Artificial_Intelligence()
		p_input = u_input.get_input()

		w.update(p_input)

		d.draw(w.return_world())

		pygame.display.update()
		clock.tick(FPS)

start()	