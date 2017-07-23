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

size = 20

class World:

	def __init__(self):
		self.size = size
		self.npc_list = []
		self.baddie_list = []
		self.player_list = []
		self.map_arr =[]
		self.num_baddies = 0
		self.num_npcs = 0
		self.num_players = 0
		self.filename = "newfile"

		self.new_map()
		self.save_map()

	def update(self, user_input):
		'''
		will iterate through all units and update their position
		'''
		print(user_input)

	def new_map(self):
		for x in range(self.size):
			for y in range(self.size):
				row = []
				objects =[]
				"TODO: get location and pass though spawn into unit constructor"
				self.spawn_baddie()


	def save_map(self):
		filename = self.filename + ".txt"
		f = open(filename, 'w+')
		for x in range(self.size):
			#print(x)
			f.write(self.map_arr[x])
		f.close					

#	def load_map(self):

	def spawn_player(self):
		player = Player()
		self.player_list.append(player)
		self.num_players +=1
		return(player)

	def spawn_baddie(self):
		baddie = Baddie()
		self.baddie_list.append(baddie)
		self.num_baddies += 1
		return(baddie)

	def spawn_npc(self):
		npc = NPC()
		self.npc_list.append(npc)
		self.num_npcs += 1
		return(npc)	

