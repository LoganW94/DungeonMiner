

class Artificial_Intelligence:

	def __init__(self):
		self.direction = "IDLE"

	def get_input(self):
	
		"add ai that spits out key"
		key = None

		if key == 'w':
			self.direction = "NORTH"
		elif key == 's':
			self.direction = "SOUTH"
		elif key == 'a':
			self.direction = "WEST"
		elif key == 'd':	
			self.direction = "EAST"
		else:
			self.direction = "IDLE"

		return(self.direction)		