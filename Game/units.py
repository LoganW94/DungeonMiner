

class Units:

	def __init__(self, location):

		self.ID = None
		self.hp = 0
		self.str = 0
		self.ap = 0
		self.dex = 0
		self.sp = 0
		self.default_state = "IDLE"
		self.previous_state = self.default_state
		self.current_state = self.default_state
		self.location = location

	def update(self, input):
		if input == "NORTH":
			self.move_north()
		elif input == "EAST":
			self.move_east()
		elif input == "SOUTH":
			self.move_south()
		elif input == "WEST":
			self.move_west()
		else:
			self.idle_state()

		#self.update_states(input)
		return(self.unit_info())	

	def set_unit_info(self, state):
		self.hp = state["HP"]
		self.str = state["STR"]
		self.ap = state["AP"]
		self.dex = state["DEX"]
		self.sp = state["SP"]
		self.location = state["Location"]
		self.current_state = state["Current State"]	

	def unit_info(self):
		state = {}
		state["ID"] = self.ID
		state["HP"] = self.hp
		state["STR"] = self.str
		state["AP"] = self.ap
		state["DEX"] = self.dex
		state["SP"] = self.sp
		state["Location"] = self.location
		state["Current State"] = self.current_state
#		state[""] = self.
#		state[""] = self.
#		state[""] = self.
#		state[""] = self.
#		state[""] = self.
		return(state)
		self.idle_state()
		self.update_states()		


	def move_north(self):
		unit_x = self.location[0]
		unit_y = self.location[1]
		unit_y -=1
		self.location = (unit_x, unit_y)

	def move_south(self):
		unit_x = self.location[0]
		unit_y = self.location[1]
		unit_y +=1
		self.location = (unit_x, unit_y)

	def move_east(self):
		unit_x = self.location[0]
		unit_y = self.location[1]
		unit_x +=1
		self.location = (unit_x, unit_y)

	def move_west(self):
		unit_x = self.location[0]
		unit_y = self.location[1]
		unit_x -=1
		self.location = (unit_x, unit_y)

	def idle_state(self):
		self.previous_state = self.current_state
		self.current_state = self.default_state

	def attack(self):
		print("attacked")

	def take_damage(self):
		print("got hurt")

	def death_state(self):
		print("died")		
"""
	def step_back(self):
		"goes back one step. sets previous state to IDLE"
		self.current_state = self.previous_state
		self.previous_state = self.default_state						
	
	def update_states(self, input):
		'eventually it might be best to have a list of states that holds the last 5 or so'
		self.previous_state = self.current_state
		self.current_state = input"""