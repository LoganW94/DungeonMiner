"""
step() takes input and moves units
keeps 3d array of map x,y,(items/units)
list of NPCs
List of Baddies
list of items 

spit out 
"""
import units
import npc
import player
import baddies

size = 0

class World:

	def __init__(self):
		self.size = size
		self.npc_list = []
		self.baddie_list = []
		self.map_arr =[]

	def update(self, user_input):
		'''
		will iterate through all units and update their position
		'''
		print(user_input)	

#	def load_map(self):

#	def spawn_player(self):

#	def spawn_baddie(self):

#	def spawn_npc(self):	

