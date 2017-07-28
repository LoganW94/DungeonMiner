import pygame
from world import World
from user_input import User_Input
from draw_world import Draw_World
from artificial_intelligence import Artificial_Intelligence

pygame.init()

clock = pygame.time.Clock()
FPS = 60

w = World()
u_input = User_Input()
ai = Artificial_Intelligence()
d = Draw_World() 

def start():

	while True:
		ai_input = ai.get_input()
		p_input = u_input.get_input()

		w.update(p_input, ai_input)

		d.draw(w.return_world())

		pygame.display.update()
		clock.tick(FPS)

start()	