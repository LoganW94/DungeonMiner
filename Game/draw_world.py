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

	def __init__(self, font):
		self.display = Screen.new(display_width, display_height, red, "Dungeon Miner")
		self.cam = Camera(display_height, display_width, tile_size)
		self.font = font

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
				location = tile["Location"]
				tile_x = location[0] * tile_size - self.cam.location[0]
				tile_y = location[1] * tile_size - self.cam.location[1]

				if tile_x >= 0 and tile_y >= 0 and tile_x <= display_width + tile_size and tile_y <= display_height + tile_size: 
					self.draw_tile(tile, tile_x, tile_y)

		for x in range(len(world_json["Units"])):
			unit = world_json["Units"][x]
			location = unit["Location"]

			unit_x = location[0] * tile_size - self.cam.location[0]
			unit_y = location[1] * tile_size - self.cam.location[1]

			if unit_x >= 0 and unit_y >= 0 and unit_x <= display_width + tile_size and unit_y <= display_height + tile_size:
				self.draw_unit(unit, unit_x, unit_y)		

	def draw_tile(self, tile, tile_x, tile_y):
		ID = tile["ID"]

		if self.id_list[ID] == "Grass":
			color = green
			char = "#"
		elif self.id_list[ID] == "Rock":
			color = grey
			char = "+" 
		elif self.id_list[ID] == "Water":
			color = blue
			char = "~"
		elif self.id_list[ID] == "Dirt":
			color = orange
			char = "::"

		text = self.font.render(char, True, color)
		self.display.blit(text, (tile_x, tile_y))		

	def draw_unit(self, unit, unit_x, unit_y):
		ID = unit["ID"]

		if self.id_list[ID] == "Player":
			color = violet
			char = "@"
		elif self.id_list[ID] == "NPC":
			color = yellow
			char = "N" 
		elif self.id_list[ID] == "Baddie":
			color = red
			char = "B"

		text = self.font.render(char, True, color)
		self.display.blit(text, (unit_x, unit_y))		
