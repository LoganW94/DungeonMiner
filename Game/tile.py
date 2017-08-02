from random import randint

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

	def __init__(self, location):
		self.location = location
		ids = {
		0: "004",
		1: "005",
		2: "006",
		3: "007"}

		self.ID = ids[randint(0,3)]
		

	def tile_info(self):
		tile = {}
		tile["Location"] = self.location
		tile["ID"] = self.ID
		tile["Is_passable"] = self.is_passable()
		return(tile)

	def is_passable(self):
		test = True
		if self.ID == "006" or self.ID == "007":
			test = False
		return(test)	