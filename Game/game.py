import pygame
from world import World
from user_input import User_Input
from draw import Draw
from artificial_intelligence import Artificial_Intelligence
from main_menu import Main_Menu
from ingame_menu import Ingame_Menu
from intro_animation import Intro_Animation

pygame.init()
font = pygame.font.SysFont(None, 25)
lg_font = pygame.font.SysFont(None, 50)

class Game:
	def __init__(self):
		self.w = World()
		self.u_input = User_Input()
		self.ai = Artificial_Intelligence()
		self.d = Draw(font)
		self.intro = Intro_Animation()
		self.menu_main = Main_Menu(self.w)
		self.game_menu = Ingame_Menu()

		self.states = {0: "Intro", 1: "Main Menu", 2: "Game", 3: "Game Menu"}
		self.current_state = 1

	def update(self):
		if self.states[self.current_state] == self.states[0]:
			self.intro_animation()
		elif self.states[self.current_state] == self.states[1]:
			self.main_menu()
		elif self.states[self.current_state] == self.states[2]:
			self.run_game()
		elif self.states[self.current_state] == self.states[3]:
			self.ingame_menu()

	def run_game(self):
		ai_input = self.ai.get_input()
		p_input = self.u_input.get_input()

		self.w.update(p_input, ai_input)
		self.d.draw_world(self.w.return_world())
		self.current_state = self.w.change_state()
		self.menu_main.state = self.current_state

	def main_menu(self):
		p_input = self.u_input.get_input()

		self.menu_main.update(p_input)
		self.d.draw_main_menu(self.menu_main.return_menu(), lg_font)
		self.current_state = self.menu_main.change_state()
		self.w.state = self.current_state

	def intro_animation(self):
		self.intro.update()
		self.current_state = self.intro.change_state()
		self.d.draw_intro(self.intro.return_intro(), lg_font)

	def ingame_menu(self):
		p_input = self.u_input.get_input()

		self.game_menu.update(p_input)
		self.d.draw_world(self.w.return_world())
		self.d.draw_game_menu(self.game_menu.return_menu(), font)
	
