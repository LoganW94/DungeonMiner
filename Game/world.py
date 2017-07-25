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
		self.size = size
		self.npc_list = []
		self.baddie_list = []
		self.player_list = []
		self.unit_list = [] #"may replace the above unit lists, to allow for sorting by level for choosing turns"
		self.map_arr =[]
		self.num_baddies = 0
		self.num_npcs = 0
		self.num_players = 0
		self.filename = "lastsave"

		self.new_map()
		#self.save_map()

	def update(self, user_input):
		'''
		will iterate through all units and update their position
		'''
		print(user_input)

	def new_map(self):
		row = []
		for x in range(self.size):
			for y in range(self.size):
				cell =[]
				location = (x,y)
				cell.append(new_tile(location))
				row.append(cell)
			self.map_arr.append(row)

#	def load_map(self):			

	def save_map(self):
		filename = "saves/" + self.filename + ".txt"
		f = open(filename, 'w+')
		for x in range(self.size):
			print(self.map_arr[x])
			string = ''.join(self.map_arr[x])
			f.write(string)
		f.close

#   def load_save(self):

	def new_tile(self, location):
		tile = Tile(location)
		return(tile)							

	def spawn_player(self):
		player = Player()
		self.player_list.append(player)
		self.num_players +=1
		return(player)

	def spawn_baddie(self, location):
		baddie = Baddie(location)
		self.baddie_list.append(baddie)
		self.num_baddies += 1
		return(baddie)

	def spawn_npc(self):
		npc = NPC()
		self.npc_list.append(npc)
		self.num_npcs += 1
		return(npc)		

	def return_world(self):
		return(self.map_arr)	