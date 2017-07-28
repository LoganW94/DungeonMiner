"""
step() takes input and moves units
keeps 3d array of map x,y,(items/units)
list of NPCs
List of Baddies
list of items 

spit out 
"""
from npc import NPC
from player import Player
from baddies import Baddie
from tile import Tile
import json

size = 50

class World:

	def __init__(self):
		
		self.npc_list = []
		self.baddie_list = []
		self.player_info = {}
		self.map_arr =[]
		self.num_baddies = 0
		self.num_npcs = 0
		self.num_players = 0
		self.filename = "lastsave"
		self.world_json = {}

		"temp code for testing"
		self.new_map()
		self.spawn_player((0,0))
		self.format_world()
		self.save_map()

	def update(self, user_input):
		'''
		will iterate through all units in order by speed
		'''
		print(user_input)

	def new_map(self):
		self.size = size
		for x in range(self.size):
			row = []
			for y in range(self.size):
				cell =[]
				location = (x,y)
				cell.append(Tile(location))
				row.append(cell)
			self.map_arr.append(row)

	def load_map(self):
		self.size = size
		filename = "saves/" + self.filename + ".txt"	
		with open(filename, 'r') as infile:
			self.world_json = json.load(infile)
			infile.close

	def format_world(self):
		json_map = []
		for x in range(self.size):
			row = []
			for y in range(self.size):
				cell = []
				tile = self.map_arr[x][y][0]
				cell.append(tile.tile_info())
				row.append(cell)
			json_map.append(row)	

		self.world_json["Player"] = self.player_info
		self.world_json["Baddies"] = self.baddie_list
		self.world_json["NPCs"] = self.npc_list	
		self.world_json["Map"] = json_map
		self.world_json["Size"] = self.size
		

	def save_map(self):
		filename = "saves/" + self.filename + ".txt"
		with open(filename, 'w') as outfile:
			json.dump(self.world_json, outfile)
		outfile.close

	def new_tile(self, location):
		tile = Tile(location)
		return(tile)							

	def spawn_player(self, location):
		player = Player(location)
		self.num_players +=1
		self.player_info = player.unit_info()
		print(self.player_info)
		return(player)

	def spawn_baddie(self, location):
		baddie = Baddie(location)
		baddie_info = baddie.unit_info()
		self.baddie_list.append(baddie)
		self.num_baddies += 1
		return(baddie)

	def spawn_npc(self):
		npc = NPC()
		npc_info = npc.unit_info()
		self.npc_list.append(npc)
		self.num_npcs += 1
		return(npc)		

	def return_world(self):
		return(self.world_json)	