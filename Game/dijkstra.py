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
		path_north = []
		path_east = []
		path_south = []
		path_west = []
		self.paths = {
		0: path_north,
		1: path_east,
		2: path_south,
		3: path_west}

		next_tile = self.find_path(start, map)
		return(temp_next_tile)

	def	find_path(self, start, map):
		location = start
		distance = 0

		while distance < self.max_distance:
			self.new_tiles = []
			distance += 1
			path_num = 0
			for x in self.find_neighbors(location):
				if len(self.checked_tiles) > 0:
					for y in self.checked_tiles:
						if x[0] != y["Location"][0] and x[1] != y["Location"][1]:
							self.new_tiles.append(self.new_tile(x, map, distance))
							self.tile_number += 1
				else:
					new_tile = self.new_tile(x, map, distance)
					self.new_tiles.append(new_tile)
					self.paths[path_num].append(new_tile)
					self.tile_number += 1

			for x in self.new_tiles:
				self.checked_tiles.append(x)

			print(self.checked_tiles)

	def find_neighbors(self, location):
		x = location[0]
		y = location[1]

		north = (x, y-1)
		east = (x+1, y)
		south = (x, y+1)
		west = (x-1, y)

		return(north, east, south, west)

	def new_tile(self, location, map, distance):	
		tile = {}
		tile["Location"] = location
		tile["Number"] = self.tile_number
		tile["Distance"] = distance
		tile["Value"] =self.determine_value(map, location)

		return(tile)

	def determine_value(self, map, location):	
		value = 0
		unit = map[location[0]][location[1]][1]

		if isinstance(unit, Units)
			value -= 2
			if isinstance(unit, Player)
				value -= 2

		return(value)

	