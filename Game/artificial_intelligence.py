

class Artificial_Intelligence:

	def __init__(self):
		self.default_state = "IDLE"
		self.direction = self.default_state
		self.keys={
		"w": "NORTH", 
		"s": "SOUTH", 
		"a": "WEST", 
		"d": "EAST",
		"c": self.default_state}

	def get_input(self):
		self.direction = self.default_state
		"add ai that spits out key"
		key = 'c'

		self.direction = self.keys[key]
		return(self.direction)		

"""
		if key == 'w':
			self.direction = "NORTH"
		elif key == 's':
			self.direction = "SOUTH"
		elif key == 'a':
			self.direction = "WEST"
		elif key == 'd':	
			self.direction = "EAST"
		elif key == 'c':
			self.direction = "IDLE"""

		