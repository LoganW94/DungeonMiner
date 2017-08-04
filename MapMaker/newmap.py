import button
import sys
import os
from tile import Tile
import json

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (211,211,211)
yellow = (255,255,0)
violet = (160,10,226)
orange = (255,165,0)

class New_Map:

	grid = []

	def __init__(self, display, mouse_pointer, font):
		self.display = display
		self.pointer = mouse_pointer
		self.font = font
		self.file_name = "Newmap"
		self.mapsize = None
		self.grid = []

	def get_grid(self):
		return self.grid

	def new_map(self, file_name, mapsize, tile_size):

		self.mapsize = int(mapsize)
		self.description = file_name
		self.file_name = file_name
		
		default_x = 200
		default_y = 50
		init_x = default_x
		default_size = tile_size

		self.grid = [] * self.mapsize
	
		for x in range(self.mapsize):
			row = [] * self.mapsize
			for y in range(self.mapsize):
				cell = []
				tile = button.Tile(self.display, default_x, default_y, default_size, self.font, blue, 3, self.pointer)
				cell.append(tile)
				row.append(cell)
				default_x += default_size

			self.grid.append(row)	
			default_y += default_size
			default_x = init_x	
		print(self.grid)	

	def loaded_map(self, json_in, tile_size):

		map_size = json_in["Map_size"]

		self.mapsize = map_size
		map_file = json_in["Map"]
		self.grid = [] * self.mapsize

		x = 0
		y = 0
		default_x = 200
		default_y = 50
		init_x = default_x
		default_size = tile_size
		

		for x in range(map_size):
			row = []
			for y in range(map_size):
				item = map_file[x][y][0]

				ID = item["ID"]
				cell = []
				if ID == "007":
					color = blue
				elif ID == "005":
					color = orange
				elif ID == "006":
					color = grey
				elif ID == "004":
					color = green
				else:
					color = red	
				tile = button.Tile(self.display, default_x, default_y, default_size, self.font, color, 3, self.pointer)
				cell.append(tile)
				row.append(cell)			
				default_x += default_size	
				
			self.grid.append(row)	
			default_y += default_size
			default_x = init_x			


	def final_grid(self, grid):
		to_json = {}
		to_json["Map_size"] = self.mapsize

		cul = []

		for x in range(self.mapsize):
			row = []
			for y in range(self.mapsize):
				t = grid[x][y][0].color
				location = (x,y)
				c = []
				if t == blue:
					tile = Tile(location, "007")
				elif t == orange:	
					tile = Tile(location, "005")
				elif t == green:
					tile = Tile(location, "004")
				elif t == grey:
					tile = Tile(location, "006")
				c.append(tile.tile_info())
				row.append(c)				
				
			cul.append(row)
		
		to_json["Map"] = cul

		file_name = ("saves/" + self.file_name + ".json")
		f1=open(file_name, 'w+')
		json.dump(to_json, f1)
		f1.close()
