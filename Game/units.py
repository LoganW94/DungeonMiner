

class Units:

	def __init__(self, location):

		self.hp = 0
		self.strenth = 0
		self.ap = 0
		self.dex = 0
		self.speed = 0
		self.default_state = "IDLE"
		self.previous_state = self.default_state
		self.current_state = self.default_state
		self.location = location

	def step(self, input):
		if input == "NORTH":
			self.move_north()
			self.update_states(input)
		elif input == "EAST":
			self.move_east()
			self.update_states(input)
		elif input == "SOUTH":
			self.move_south()
			self.update_states(input)
		elif input == "WEST":
			self.move_west()
			self.update_states(input)
		elif input == self.default_state:
			self.idle_state()
			self.update_states(input)

	def step_back(self):
		"goes back one step. sets previous state to IDLE"
		self.current_state = self.previous_state
		self.previous_state = self.default_state						
	
	def update_states(self, input):
		'eventually it might be best to have a list of states that holds the last 5 or so'
		self.previous_state = self.current_state
		self.current_state = input

	def move_north(self):
		print("moved north")

	def move_south(self):
		print("moved south")

	def move_east(self):
		print("moved east")

	def move_west(self):
		print("moved west")

	def idle_state(self):
		print("stood still")	

	def attack(self):
		print("attacked")

	def take_damage(self):
		print("got hurt")

	def death_state(self):
		print("died")		
