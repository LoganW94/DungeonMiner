

class Units:

	def __init__(self, location):

		self.ID = None
		self.hp = 50
		self.str = 10
		self.ap = 0
		self.dex = 0
		self.sp = 0
		self.status = "Passive"	
		self.lvl = 1
		self.type = "Unit"
		self.default_state = "IDLE"
		self.current_state = self.default_state
		self.location = location
		self.can_move = True

	def update(self, input, x, y, map):
		unit = map[x][y][1]
		
		self.check_collide(input, x, y, map)
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
		self.type = "Unit"

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
		state["status"] = self.status
		state["Type"] = self.type
#		state[""] = self.
		return(state)

	def check_collide(self, input, x, y, map):
		current_tile = map[x][y][0]
		current_location = current_tile.tile_info()["Location"]
		if input == "NORTH":
			next_tile =  map[current_location[0]][current_location[1] - 1]
			self.check_tile(next_tile)
		elif input == "EAST":
			next_tile = map[current_location[0] + 1][current_location[1]]
			self.check_tile(next_tile)
		elif input == "SOUTH":
			next_tile = map[current_location[0]][current_location[1] + 1]
			self.check_tile(next_tile)
		elif input == "WEST":
			next_tile = map[current_location[0] - 1][current_location[1]]
			self.check_tile(next_tile)

	def check_tile(self, next_tile):
		if len(next_tile) == 2:
			if isinstance(next_tile[1], Units):
				self.can_move = False
		else:				
			self.can_move = next_tile[0].tile_info()["Is_passable"]

	def move_north(self):
		if self.can_move == True:
			unit_x = self.location[0]
			unit_y = self.location[1]
			unit_y -=1			
			self.location = (unit_x, unit_y)

	def move_south(self):
		if self.can_move == True:
			unit_x = self.location[0]
			unit_y = self.location[1]
			unit_y +=1
			self.location = (unit_x, unit_y)

	def move_east(self):
		if self.can_move == True:
			unit_x = self.location[0]
			unit_y = self.location[1]
			unit_x +=1
			self.location = (unit_x, unit_y)		

	def move_west(self):
		if self.can_move == True:
			unit_x = self.location[0]
			unit_y = self.location[1]
			unit_x -=1
			self.location = (unit_x, unit_y)			

	def idle_state(self):
		self.status = self.default_state

	def attack(self):
		print("attacked")

	def take_damage(self):
		print("got hurt")

	def death_state(self):
		print("died")		
