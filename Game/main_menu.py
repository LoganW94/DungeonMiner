


class Main_Menu:
	def __init__(self):
		self.load_assets()
		self.player_name = None
		self.world_name = None
		self.state = 1

		self.button0 = {"txt": "New Game", "Selected": True, "function": self.new_game}
		self.button1 = {"txt": "Load Game", "Selected": False, "function": self.new_game}
		self.button1_alt = {"txt": "Save Game", "Selected": False, "function": self.save_game}
		self.button2 = {"txt": "Settings", "Selected": False, "function": self.settings}
		self.current_state = 0

		self.menu_state = {
		0: self.button0,
		1: self.button1,
		2: self.button2}

	def update(self, input):
		if input == "NORTH":
			if self.current_state == 0:
				self.menu_state[self.current_state]["Selected"] = False
				self.current_state = 2
				self.menu_state[self.current_state]["Selected"] = True
			elif self.current_state == 1:
				self.menu_state[self.current_state]["Selected"] = False
				self.current_state = 0
				self.menu_state[self.current_state]["Selected"] = True
			elif self.current_state == 2:
				self.menu_state[self.current_state]["Selected"] = False
				self.current_state = 1
				self.menu_state[self.current_state]["Selected"] = True
		elif input == "SOUTH":				
			if self.current_state == 0:
				self.menu_state[self.current_state]["Selected"] = False
				self.current_state = 1
				self.menu_state[self.current_state]["Selected"] = True
			elif self.current_state == 1:
				self.menu_state[self.current_state]["Selected"] = False
				self.current_state = 2
				self.menu_state[self.current_state]["Selected"] = True
			elif self.current_state == 2:
				self.menu_state[self.current_state]["Selected"] = False
				self.current_state = 0
				self.menu_state[self.current_state]["Selected"] = True
		elif input == "RETURN":
			x = self.menu_state[self.current_state]["function"]		
			x()
		

	def new_game(self):
		"sets up basic info for player and other per game settings"
		self.state = 2

	def load_game(self):
		"loads in a previous save"

	def save_game(self):
		""	

	def settings(self):
		"can change settings"	

	def return_menu(self):
		self.menu_state = {
		0: self.button0,
		1: self.button1,
		2: self.button2}	
		return(self.menu_state)
			

	def change_state(self):
		return(self.state)	
	
	def load_assets(self):
		"Loads menu graphics"	
	