from npc import NPC
from player import Player
from baddies import Baddie
from tile import Tile
from objects import Object
import json
from random import randint

size = 100

class World:

	def __init__(self):
		"holds a list of all units instances"
		self.unit_list = []
		"just holds the info to be sent to draw"
		self.info_list = []
		self.player_info = {}
		self.map_arr =[]
		self.num_baddies = 0
		self.num_npcs = 0
		self.num_players = 0
		self.filename = "lastsave"
		self.json_map = []
		self.world_json = {}

		self.counter = 0
		self.wait = False
		self.wait_time = 6

		"temp code for testing"
		
	def update(self, user_input, ai_input):
		self.info_list = []

		for x in self.unit_list:
			if x.ID == "001":
				self.info_list.append(x.update(user_input, self.json_map))
			else:
				self.info_list.append(x.update(ai_input, self.json_map))
		self.format_world()	
						

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

	def load_map(self, filename):
		file = "maps/" + filename + ".json"	
		with open(file, 'r') as infile:
			json_in = json.load(infile)
			infile.close()

		self.size = json_in["Map_size"]
		print(self.size)
		mapfile = json_in["Map"]
		cul = []

		for x in range(self.size):
			row = []
			for y in range(self.size):
				location = (x,y)
				item = mapfile[x][y][0]
				cell = []
				ID = item["ID"]
				tile = Tile(location, ID)
				cell.append(tile.tile_info())
				row.append(cell)
			cul.append(row)	
		self.json_map = cul
		print
		self.populate()	
		self.format_world()


	def format_world(self):
		self.world_json["Player"] = self.player_info
		self.world_json["Units"] = self.info_list	
		self.world_json["Map"] = self.json_map
		self.world_json["Size"] = self.size
		

	def save_map(self):
		filename = "saves/" + self.filename + ".json"
		with open(filename, 'w') as outfile:
			json.dump(self.world_json, outfile)
		outfile.close()							

	def spawn_player(self, location):
		player = Player(location)
		self.unit_list.append(player)
		self.num_players +=1
		self.player_info = player.unit_info()
		self.info_list.append(self.player_info)
		return(player)

	def spawn_baddie(self, location):
		baddie = Baddie(location)
		self.info_list.append(baddie.unit_info())
		self.unit_list.append(baddie)
		self.num_baddies += 1
		return(baddie)

	def spawn_npc(self, location):
		npc = NPC(location)
		self.info_list.append(npc.unit_info())
		self.unit_list.append(npc)
		self.num_npcs += 1
		return(npc)		

	def return_world(self):
		return(self.world_json)

	def populate(self):
		"eventually will iterate over map and spawn all baddies, NPCs, items, and the player"
		self.spawn_player((25,35))
		self.spawn_baddie((1,3))
		self.spawn_baddie((5,20))
		self.spawn_baddie((48,25))
		self.spawn_baddie((30,30))
		self.spawn_npc((25,5))		