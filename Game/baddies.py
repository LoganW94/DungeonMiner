from units import Units

class Baddie(Units):

	def __init__(self, location):
		Units.__init__(self, location)
		self.ID = "003"


class Big_Baddie(Baddie):

	def __init__(self, location):
		Baddie.__init__(self, location)	

class Little_Baddie(Baddie):

	def __init__(self, location):
		Baddie.__init__(self, location)			