from npc import NPC
from player import Player
from baddies import *
from units import Units
from tile import Tile
from objects import *

class Path:
	def __init__(self):
		self.max_distance = 20
		self.target = None
		self.distance = 0
		self.tile_number = 0

	def	find_path(self, start, map, map_size):
		start_tile = map[start[0]][start[1]][0]
		checked_tiles = self.build_list(start, map, map_size, start_tile)
		print(checked_tiles)
		return self.shortest_path(checked_tiles)

	def build_list(self, start, map, map_size, start_tile):
		unchecked_tiles = []
		checked_tiles = []				
		tiles = self.find_neighbors(start, map, map_size)
		checked_tiles.append(start_tile)
		
		for x in tiles:
			self.tile_number +=1
			self.set_tile_info(x, self.tile_number, self.distance, start)
			unchecked_tiles.append(x)
		
		while True:
			new_tiles = []
			self.distance += 1
			if self.distance == self.max_distance:
				break
			for x in unchecked_tiles:	
				tiles = self.find_neighbors(x.tile_info()["Location"], map, map_size)
				checked_tiles.append(x)
				unchecked_tiles.remove(x)
				for y in tiles:
					if y not in checked_tiles and y not in unchecked_tiles:
						self.set_tile_info(y, self.tile_number, self.distance, x)
						self.tile_number +=1
						if y.tile_info()["Is_passable"] == True:
							new_tiles.append(y)
						tile_loc = y.tile_info()["Location"]	
						if len(map[tile_loc[0]][tile_loc[1]]) == 2:
							unit = map[tile_loc[0]][tile_loc[1]][1]	
							if isinstance(unit, Player):
								self.target = y
		for t in checked_tiles:
			self.find_value(t, map)
			if t.tile_info()["Value"] > 5:
				checked_tiles.remove(t)
		return checked_tiles		

	def shortest_path(self, checked_tiles, target = None):
		path = checked_tiles

		return path

	def find_value(self, tile, map):
		"move this to constructor for Tile"
		
		tile_info = tile.tile_info()
		tile_location = tile_info["Location"]
		value = 0

		if len(map[tile_location[0]][tile_location[1]]) == 2:
			if isinstance(map[tile_location[0]][tile_location[1]][1], Units):
				val = map[tile_location[0]][tile_location[1]][0].tile_info()["Value"]
				value += val
			elif isinstance(map[tile_location[0]][tile_location[1]][1], Object):
				val = map[tile_location[0]][tile_location[1]][0].tile_info()["Value"]
				value += val
	

		value += tile_info["Distance"]	
		tile.set_info("Value", value)
		
	def set_tile_info(self, tile, tile_number, distance, predeccesor):
		tile.set_info("Number", tile_number)
		tile.set_info("Distance", distance)
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