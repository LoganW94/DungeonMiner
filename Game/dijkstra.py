from npc import NPC
from player import Player
from baddies import *
from units import Units
from tile import Tile
from objects import *

class Path:
	def __init__(self, start, map):
		self.checked_tiles = []
		self.new_tiles = []
		self.tile_number = 0
		self.max_distance = 20

		next_tile = self.find_path(start, map)
		return(temp_next_tile)

	def	find_path(self, start, map):
		start_tile = map[start[0]][start[1]][0]

		distance = 0
		while distance < max_distance:
			if len(self.new_tiles) == 0:
				distance += 1
				tiles = find_neighbors(start, map)
				self.checked_tiles.append(start_tile)
				for x in tiles:
					self.new_tiles.append(x)
			else:
				for x in self.new_tiles:
					distance += 1
					tiles = find_neighbors(x.tile_info()["Location"], map)
					for y in tiles:
						y.set_info("Distance", distance)
						y.set_info("")ssxmbbmbscbssx
						if y not in self.checked_tiles:
							self.checked_tiles.append(y)
						

		

	def find_neighbors(self, location, map):
		x = location[0]
		y = location[1]

		north = (x, y-1)
		north = map[north[0]][north[1]][0]
		east = (x+1, y)
		east = map[east[0]][east[1]][0]
		south = (x, y+1)
		south = map[south[0]][south[1]][0]
		west = (x-1, y)
		west = map[west[0]][west[1]][0]

		return(north, east, south, west)



	