from units import Units

class NPC(Units):

	def __init__(self, location):		
		Units.__init__(self, location)
		self.ID = "002"