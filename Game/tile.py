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
		
	def tile_info(self):
		tile = {}
		tile["Location"] = self.location
		tile["ID"] = self.ID
		tile["Is_passable"] = self.is_passable()
		tile["Type"] = self.type
		return(tile)

	def is_passable(self):
		test = True
		if self.ID == "006" or self.ID == "007":
			test = False
		return(test)		