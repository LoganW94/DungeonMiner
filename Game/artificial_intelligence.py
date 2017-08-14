from npc import NPC
from player import Player
from baddies import *
from units import Units
from tile import Tile
from objects import *
from dijkstra import Path

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

	def get_input(self, unit, map):
		self.direction = self.default_state
		start = unit["Location"]

		next_tile = Path(start, map)
		x = next_tile[0]
		y = next_tile[1]

		if x > start[0]:
			key = "d"
		elif x < start[0]:
			key = "a"	
		elif y > start[1]:
			key = "s"
		elif y < start[1]:
			key = "w"
		else:
			key = "c"			
	
		self.direction = self.keys[key]
		return(self.direction)

	
	def fsm(self, unit):
		"finite state machine or game tree"			