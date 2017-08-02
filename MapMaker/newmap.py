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
		self.file_name = None
		self.mapsize = None

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

		row = []
		self.grid = []
		for x in range(self.mapsize):
			for y in range(self.mapsize):
				tile = button.Tile(self.display, default_x, default_y, default_size, self.font, white, 3, self.pointer)
				row.append(tile)
				default_x += default_size

			self.grid.append(row)
			row = []	
			default_y += default_size
			default_x = init_x	

	def loaded_map(self, json_in, tile_size):

		self.g = GameMap.load(json_in)

		x = 0
		y = 0
		default_x = 200
		default_y = 50
		init_x = default_x
		default_size = tile_size
		
		row = []
		self.grid = []

		for x in range(self.g.get_map_size()):
			for y in range(self.g.get_map_size()):
				grid_item = self.g.get_grid_item(x,y)

				if(isinstance(grid_item,Terrain)):
					t_type = grid_item.terrtype
					print(t_type)
					if t_type == 'W':
						color = blue
					elif t_type == 'P':
						color = white
					elif t_type == 'R':
						color = grey
					elif t_type == 'T':
						color = green
					else:
						color = red	
					tile = button.Tile(self.display, default_x, default_y, default_size, self.font, color, 3, self.pointer)
					row.append(tile)
					default_x += default_size	
				self.grid.append(row)
				row = []	
			default_y += default_size
			default_x = init_x			


	def final_grid(self, grid):

		x = 0
		y = 0
		to_json = {}
		to_json["Map_size"] = self.mapsize

		self.grid = grid
		cul = []

		for i in self.grid:
			row = []
			for r in i:
				
				if r.color == blue:
					tile = Tile((x,y), "007")
				elif r.color == orange:	
					tile = Tile((x,y), "005")
				elif r.color == green:
					tile = Tile((x,y), "004")
				elif r.color == grey:
					tile = Tile((x,y), "006")

				row.append(tile.tile_info())					
				x+=1
			y+=1
			x=0		
			cul.append(row)
		x=0
		y=0
		to_json["Map"] = cul
		print(cul)

		file_name = ("saves/" + self.file_name + ".json")
		f1=open(file_name, 'w+')
		json.dump(to_json, f1)
		f1.close()		

	