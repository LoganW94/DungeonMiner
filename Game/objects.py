

class Object:
	def __init__(self, location, ID):
		self.location = location
		self.ID = ID
		self.type = "Object"

	def item_info(self):
		item = {}
		item["Location"] = self.location
		item["ID"] = self.ID
		item["Type"] = self.type
		return(item)

class Ladder(Object):
	def __init__(self, location):
		self.ID = "008"
		Object.__init__(self, location, self.ID)
			

