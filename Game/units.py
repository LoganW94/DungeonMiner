

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
		self.can_move = True

	def update(self, input, map):
		if input == "NORTH":
			self.check_collide(map, input)
			self.move_north()
		elif input == "EAST":
			self.check_collide(map, input)
			self.move_east()
		elif input == "SOUTH":
			self.check_collide(map, input)
			self.move_south()
		elif input == "WEST":
			self.check_collide(map, input)
			self.move_west()
		else:
			self.idle_state()

		return(self.unit_info())	

	def set_unit_info(self, state):
		self.hp = state["HP"]
		self.str = state["STR"]
		self.ap = state["AP"]
		self.dex = state["DEX"]
		self.sp = state["SP"]
		self.location = state["Location"]
		self.current_state = state["Current State"]
		self.status = "Passive"	
		self.lvl = 1

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
		state["LVL"] = self.lvl = 1
#		state[""] = self.
#		state[""] = self.
#		state[""] = self.
#		state[""] = self.
		return(state)
		self.idle_state()
		self.update_states()

	def check_collide(self, map, input):
		current_tile = map[self.location[0]][self.location[1]][0]
		current_location = current_tile["Location"]
		if input == "NORTH":
			next_tile = (current_location[0], current_location[1] - 1)
		elif input == "EAST":
			next_tile = (current_location[0] + 1, current_location[1])
		elif input == "SOUTH":
			next_tile = (current_location[0], current_location[1] + 1)
		elif input == "WEST":
			next_tile = (current_location[0] - 1, current_location[1])

		self.can_move = map[next_tile[0]][next_tile[1]][0]["Is_passable"]

	def move_north(self):
		if self.can_move == True:
			unit_x = self.location[0]
			unit_y = self.location[1]
			unit_y -=1
			self.location = (unit_x, unit_y)
		else:
			self.idle_state()	

	def move_south(self):
		if self.can_move == True:
			unit_x = self.location[0]
			unit_y = self.location[1]
			unit_y +=1
			self.location = (unit_x, unit_y)
		else:
			self.idle_state()

	def move_east(self):
		if self.can_move == True:
			unit_x = self.location[0]
			unit_y = self.location[1]
			unit_x +=1
			self.location = (unit_x, unit_y)
		else:
			self.idle_state()			

	def move_west(self):
		if self.can_move == True:
			unit_x = self.location[0]
			unit_y = self.location[1]
			unit_x -=1
			self.location = (unit_x, unit_y)
		else:
			self.idle_state()			

	def idle_state(self):
		self.previous_state = self.current_state
		self.current_state = self.default_state


	def attack(self):
		print("attacked")

	def take_damage(self):
		print("got hurt")

	def death_state(self):
		print("died")		
