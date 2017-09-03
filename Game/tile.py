import json

"colors"
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (211,211,211)
yellow = (255,255,0)
violet = (160,10,226)
orange = (255,165,0)

class Tile:

	def __init__(self, location, ID):
		self.location = location
		self.ID = ID
		self.type = "Tile"
		self.tile = {}
		self.tile_number = 0
		self.distance = 0
		self.predeccesor = None
		self.value = 0
		self.visited = False
		
	def tile_info(self):
		self.tile["Location"] = self.location
		self.tile["ID"] = self.ID
		self.tile["Is_passable"] = self.is_passable()
		self.tile["Type"] = self.type
		self.tile["Number"] = self.tile_number
		self.tile["Distance"] = self.distance
		self.tile["Visited"] = False
		self.tile["Predeccesor"] = self.predeccesor
		self.tile["Value"] = self.value
		self.tile["Number"] = self.tile_number
		return(self.tile)

	def set_info(self, key, value):
		if key == "Value":
			self.value = value
		elif key == "Distance":
			self.distance = value
		elif key == "Number":
			self.tile_number = value
		elif key == "Predeccesor":
			self.predeccesor = value
		elif key == "Visited":
			self.visited = value			

	def find_value(self):
		value = 0
		grass_val = 2
		dirt_val = 1
		if tile_info["ID"] == "005":
			value += dirt_val
		elif tile_info["ID"] == "004":
			value += grass_val

		self.value = value 			

	def is_passable(self):
		test = True
		if self.ID == "006" or self.ID == "007":
			test = False
		return(test)		