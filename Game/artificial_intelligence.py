

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