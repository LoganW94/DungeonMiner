"""
draws world to screen

gets map_arr from world
"""
from screen import Screen
import pygame
from camera import Camera
import json

"colors"
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (200,200,200)
yellow = (255,255,0)
violet = (160,10,226)
orange = (255,165,0)

display_width = 800
display_height = 600
tile_size = 32

class Draw_World:

	def __init__(self):
		self.display = Screen.new(display_width, display_height, red, "Dungeon Miner")
		self.cam = Camera(display_height, display_width, tile_size)

		with open("ID_list.txt", 'r') as infile:
			self.id_list = json.load(infile)
			infile.close

	def draw(self, world_json):
		self.display.fill(black)
		map_arr = world_json["Map"]
		for x in range(len(world_json["Units"])):
			unit = world_json["Units"][x]
			if unit["ID"] == "001":
				self.cam.update(unit["Location"])

		"should check to see if tile is visible to camera, and if so draws it."
		for x in range(world_json["Size"]):
			for y in range(world_json["Size"]):
				tile = map_arr[x][y][0]
				self.draw_tile(tile)

		for x in range(len(world_json["Units"])):
			unit = world_json["Units"][x]
			self.draw_unit(unit)		

	def draw_tile(self, tile):
		location = tile["Location"]
		ID = tile["ID"]
		tile_x = location[0] * tile_size - self.cam.location[0]
		tile_y = location[1] * tile_size - self.cam.location[1]

		if self.id_list[ID] == "Grass":
			color = green
		elif self.id_list[ID] == "Rock":
			color = grey 
		elif self.id_list[ID] == "Water":
			color = blue
		elif self.id_list[ID] == "Dirt":
			color = orange
		else:
			color = red				
		"tile color"	
		self.display.fill(color, rect = ((tile_x, tile_y), (tile_size, tile_size)))
		"outline"
		self.display.fill(black, rect = ((tile_x, tile_y), (1, tile_size)))
		self.display.fill(black, rect = ((tile_x, tile_y), (tile_size, 1)))
		self.display.fill(black, rect = ((tile_x + tile_size, tile_y), (1, tile_size)))
		self.display.fill(black, rect = ((tile_x, tile_y + tile_size), (tile_size, 1)))

	def draw_unit(self, unit):
		location = unit["Location"]
		ID = unit["ID"]

		"should check to see if tile is visible to camera, and if so draws it."

		if self.id_list[ID] == "Player":
			unit_x = location[0] * tile_size - self.cam.location[0]
			unit_y = location[1] * tile_size - self.cam.location[1]
			color = violet
		elif self.id_list[ID] == "NPC":
			unit_x = location[0] * tile_size - self.cam.location[0]
			unit_y = location[1] * tile_size - self.cam.location[1]
			color = yellow 
		elif self.id_list[ID] == "Baddie":
			unit_x = location[0] * tile_size - self.cam.location[0]
			unit_y = location[1] * tile_size - self.cam.location[1]
			color = red
		else:
			color = white

		"unit color"	
		self.display.fill(color, rect = ((unit_x, unit_y), (tile_size, tile_size)))
		"outline"
		self.display.fill(black, rect = ((unit_x, unit_y), (1, tile_size)))
		self.display.fill(black, rect = ((unit_x, unit_y), (tile_size, 1)))
		self.display.fill(black, rect = ((unit_x + tile_size, unit_y), (1, tile_size)))
		self.display.fill(black, rect = ((unit_x, unit_y + tile_size), (tile_size, 1)))	

		
