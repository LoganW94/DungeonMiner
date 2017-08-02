import json

class Tile:

	def __init__(self, location, ID):
		self.location = location
		ids = {}
		with open("ID_list.txt", 'r') as infile:
			ids = json.load(infile)
			infile.close

		self.ID = ids[ID]
		

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