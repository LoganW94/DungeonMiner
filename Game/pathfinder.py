from npc import NPC
from player import Player
from baddies import *
from units import Units
from tile import Tile
from objects import *

class Path:
	def __init__(self):
		self.max_distance = 10

	def	find_path(self, start, map, map_size):
		start_tile = map[start[0]][start[1]][0]
		distance = 1
		tile_number = 0
		checked_tiles = []
		unchecked_tiles = []

		tiles = self.find_neighbors(start, map, map_size)
		checked_tiles.append(start_tile)
		for x in tiles:
			tile_number +=1
			self.set_tile_info(x, tile_number, distance, start)
			unchecked_tiles.append(x)
		
		while True:
			new_tiles = []
			distance += 1
			if distance == self.max_distance:
				break
			for x in unchecked_tiles:	
				tiles = self.find_neighbors(x.tile_info()["Location"], map, map_size)
				checked_tiles.append(x)
				unchecked_tiles.remove(x)
				for y in tiles:
					if y not in checked_tiles and y not in unchecked_tiles:
						self.set_tile_info(y, tile_number, distance, x)
						tile_number +=1
						new_tiles.append(y)
			
		"return next tile"
		temp_next_tile = map[start[0]][start[1]][0].tile_info()["Location"]
		return temp_next_tile

	def find_value(self, tile, map):
		tile_info = tile.tile_info()
		tile_location = tile_info["Location"]
		value = 0

		tile.set_info("Value", value)
		
	def set_tile_info(self, tile, tile_number, distance, predeccesor):
		tile.set_info("Number", tile_number)
		tile.set_info("Distance", distance)
		tile.set_info("Value", distance)
		tile.set_info("Predeccesor", predeccesor)

	def find_neighbors(self, location, map, map_size):
		current_location = map[location[0]][location[1]][0].tile_info()["Location"]
		tiles = []

		if current_location[0] > 0 and current_location[0] < map_size: 
			tiles.append(map[current_location[0]-1][current_location[1]][0])
			tiles.append(map[current_location[0]+1][current_location[1]][0])
		if current_location[1] > 0 and current_location[0] < map_size: 	
			tiles.append(map[current_location[0]][current_location[1]+1][0])
			tiles.append(map[current_location[0]][current_location[1]-1][0])		

		return tiles