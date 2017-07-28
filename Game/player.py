from units import Units

class Player(Units):

	def __init__(self, location):
		
		Units.__init__(self, location)
		self.ID = "001"
