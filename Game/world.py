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

size = 20

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

		self.new_map()
		#self.save_map()

	def update(self, user_input):
		'''
		will iterate through all units in order by speed
		'''
		print(user_input)

	def new_map(self):
		self.size = size
		row = []
		for x in range(self.size):
			for y in range(self.size):
				cell =[]
				location = (x,y)
				cell.append(Tile(location))
				row.append(cell)
			self.map_arr.append(row)

	def load_map(self):
		self.size = size	

	def format_world(self):	
		self.world_json["map"] = self.map_arr
		self.world_json["size"] = self.size
		self.world_json["player"] = self.player_info	

	def save_map(self):
		filename = "saves/" + self.filename + ".txt"
		f = open(filename, 'w+')
		
		f.close

#   def load_save(self):


	def new_tile(self, location):
		tile = Tile(location)
		return(tile)							

	def spawn_player(self):
		player = Player()
		self.num_players +=1
		self.player_info = player.unit_info()
		print(player_state)
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