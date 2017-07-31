from world import World
from user_input import User_Input
from draw import Draw
from artificial_intelligence import Artificial_Intelligence
from main_menu import Main_Menu
from ingame_menu import Ingame_Menu
from intro_animation import Intro_Animation

class Game:
	def __init__(self):
		self.w = World()
		self.u_input = User_Input()
		self.ai = Artificial_Intelligence()
		self.d = Draw()
		self.intro = Intro_Animation()
		self.menu_main = Main_Menu()
		self.game_menu = Ingame_Menu()

		self.states = {0: "Intro", 1: "Main Menu", 2: "Game", 3: "ingame Menu"}
		self.current_state = 2

	def update(self):
	
		if self.current_state == "Intro":
			self.intro_animation()
		elif self.current_state == "Main Menu":
			self.main_menu()
		elif self.current_state == "Game":
			self.run_game()
		elif self.current_state == "ingame Menu":
			self.ingame_menu()

	def run_game(self):
		ai_input = self.ai.get_input()
		p_input = self.u_input.get_input()

		self.w.update(p_input, ai_input)

		self.d.draw_world(self.w.return_world())

	def main_menu(self):
		self.menu_main.update()

	def intro_animation(self):
		self.intro.update()

	def ingame_menu(self):
		self.game_menu.update()
	
