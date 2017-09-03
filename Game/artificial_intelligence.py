from npc import NPC
from player import Player
from baddies import *
from units import Units
from tile import Tile
from objects import *
from pathfinder import Path

class Artificial_Intelligence:

	def __init__(self):
		self.default_state = "IDLE"
		self.direction = self.default_state
		self.keys={
		"w": "NORTH", 
		"s": "SOUTH", 
		"a": "WEST", 
		"d": "EAST",
		"c": self.default_state}

	def get_input(self, unit, map, map_size):
		self.direction = self.default_state
		start = unit.unit_info()["Location"]
		next_tile = Path().find_path(start, map, map_size)
		#next_tile = start

		if next_tile.tile_info()["Location"][0] > start[0]:
			key = "d"
		elif next_tile.tile_info()["Location"][0] < start[0]:
			key = "a"	
		elif next_tile.tile_info()["Location"][1] > start[1]:
			key = "s"
		elif next_tile.tile_info()["Location"][1] < start[1]:
			key = "w"
		else:
			key = "c"			
	
		self.direction = self.keys[key]
		return(self.direction)

	
	def fsm(self, unit):
		"finite state machine or game tree"	

		"sudo code"
		idle_state()


	def idle_state(self):
		""
		next_tile = Path(start, map)
		x = next_tile[0]
		y = next_tile[1]

	def attack_state(self):
		""

	def move_state(self):
		""		
