from npc import NPC
from player import Player
from baddies import Baddie
from tile import Tile
from objects import Object
import json
from random import randint


class World:

	def __init__(self):
		self.player_info = {}
		self.map_arr =[]
		self.num_baddies = 0
		self.num_npcs = 0
		self.filename = "lastsave"
		self.json_map = []
		self.world_json = {}
		self.state = 2
		self.counter = 0
		self.wait = False
		self.wait_time = 6
		
	def update(self, user_input, ai_input):
		if user_input == "MENU":
			self.state = 1
			
		for x in range(self.world_json["Size"]):
			for y in range(self.world_json["Size"]):
				if len(self.json_map[x][y]) == 2:
					unit = self.json_map[x][y][1]
					unit_info = unit.unit_info()
					if unit_info["ID"] == "001":
						unit.update(user_input, x, y, self.json_map)
						self.player_info = unit.unit_info()
					else:
						unit.update(ai_input, x, y, self.json_map)					
						
	def new_map(self):
		self.size = size
		ids = {
		0: "004",
		1: "005",
		2: "006",
		3: "007"}
		for x in range(self.size):
			info_row = []
			for y in range(self.size):
				info_cell = []
				location = (x,y)
				ID = ids[randint(0,3)]
				tile = Tile(location, ID)
				info_cell.append(tile.tile_info())
				info_row.append(info_cell)
			self.json_map.append(info_row)

		self.populate()
		self.format_world()				

	def load_map(self, filename):
		file = "maps/" + filename + ".json"	
		with open(file, 'r') as infile:
			json_in = json.load(infile)
			infile.close()

		self.size = json_in["Map_size"]
		mapfile = json_in["Map"]
		grid = []

		for x in range(self.size):
			row = []
			for y in range(self.size):
				tile = mapfile[x][y][0]
				cell = []
				cell.append(tile)
				row.append(cell)
			grid.append(row)
		self.json_map = grid
			
		self.populate()
		self.format_world()

	def format_world(self):
		self.world_json["Player"] = self.player_info
		self.world_json["Map"] = self.json_map
		self.world_json["Size"] = self.size

	def save_map(self):
		filename = "saves/" + self.filename + ".json"
		with open(filename, 'w') as outfile:
			json.dump(self.world_json, outfile)
		outfile.close()							

	def spawn_player(self, location):
		player = Player(location)
		x = location[0]
		y = location[1]
		self.player_info = player.unit_info()
		self.json_map[x][y].append(player)
	

	def spawn_baddie(self, location):
		baddie = Baddie(location)
		self.num_baddies += 1
		x = location[0]
		y = location[1]
		self.json_map[x][y].append(baddie)

	def spawn_npc(self, location):
		npc = NPC(location)
		self.num_npcs += 1
		x = location[0]
		y = location[1]
		self.json_map[x][y].append(npc)		

	def return_world(self):
		return(self.world_json)

	def populate(self):
		"eventually will iterate over map and spawn all baddies, NPCs, items, and the player"
		self.spawn_player((25,35))
		self.spawn_baddie((20,15))
		self.spawn_baddie((10,20))
		self.spawn_baddie((30,25))
		self.spawn_npc((24,30))

	def change_state(self):
		return self.state			