from screen import Screen
import pygame
from camera import Camera
import json
from random import randint
from units import Units
from objects import *
from tile import Tile

"colors"
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
light_blue = (0,0,100)
medium_blue = (0,0,195)
grey = (200,200,200)
yellow = (255,255,0)
violet = (160,10,226)
orange = (255,165,0)

display_width = 960
display_height = 640
tile_size = 16
"to impliment"
tile_height = 16
tile_width = 14 #may need tweeked

class Draw:

	def __init__(self, font, p_font):
		self.display = Screen.new(display_width, display_height, red, "Dungeon Miner")
		self.cam = Camera(display_height, display_width, tile_size)
		self.font = font
		self.p_font = p_font

		with open("ID_list.txt", 'r') as infile:
			self.id_list = json.load(infile) 
			infile.close

	def draw_world(self, world_json):
		self.display.fill(black)
		map_arr = world_json["Map"]
		player = world_json["Player"]
		self.cam.update(world_json["Player"]["Location"])

		for x in range(world_json["Size"]):
			for y in range(world_json["Size"]):
				tile = map_arr[x][y][0]				
				location = tile.tile_info()["Location"]
				if len(map_arr[x][y]) == 2:
					if isinstance(map_arr[x][y][1], Units):
						unit = map_arr[x][y][1].unit_info()
						unit_x = location[0] * tile_size - self.cam.location[0]
						unit_y = location[1] * tile_size - self.cam.location[1]
						if unit_x >= 0 and unit_y >= 0 and unit_x <= display_width - tile_size and unit_y <= display_height - tile_size:
							ID = unit["ID"]
							self.draw_unit(ID, unit_x, unit_y)
					elif isinstance(map_arr[x][y][1], Object):
						item = map_arr[x][y][1]
						item_x = location[0] * tile_size - self.cam.location[0]
						item_y = location[1] * tile_size - self.cam.location[1]
						if item_x >= 0 and item_y >= 0 and item_x <= display_width - tile_size and item_y <= display_height - tile_size:
							ID = item.item_info()["ID"]
							self.draw_item(ID, item_x, item_y)
				elif isinstance(map_arr[x][y][0], Tile):
					tile_x = x * tile_size - self.cam.location[0]
					tile_y = y * tile_size - self.cam.location[1]
					if tile_x >= -tile_size and tile_y >= -tile_size and tile_x <= display_width + tile_size and tile_y <= display_height + tile_size: 
						ID = tile.tile_info()["ID"]
						self.draw_tile(ID, tile_x, tile_y)

	def draw_main_menu(self, menu, font):
		self.display.fill(black)
		y = 100

		for x in menu:
			if menu[x]["Selected"] == True:
				color = blue
			else:
				color = white
			text = menu[x]["txt"]		
			txt_size = font.size(menu[x]["txt"])
			text = font.render(text, True, color)
			x = (display_width/2) - (txt_size[0]/2)
			self.display.blit(text, (x, y))
			y += 200


	def draw_intro(self, intro, font):
		self.display.fill(black)
		color = white
		text = font.render(intro, True, color)
		txt_size = font.size(intro)
		x = (display_width/2) - (txt_size[0]/2)
		y = (display_height/2) - (txt_size[1]/2)
		self.display.blit(text, (x, y))	

	def draw_game_menu(self, menu, font):
		""

	def draw_HUD(self):
		"all the stuff that displays on screen during gameplay"		

	def draw_tile(self, ID, tile_x, tile_y):
		colors = {
		0: blue,
		1: medium_blue,
		2: light_blue}

		if self.id_list[ID] == "Grass":
			color = green
			char = "; '"
		elif self.id_list[ID] == "Rock":
			color = grey
			char = "+" 
		elif self.id_list[ID] == "Water":
			color = colors[randint(0,1)]
			char = "(("
		elif self.id_list[ID] == "Dirt":
			color = orange
			char = "::"

		text = self.font.render(char, True, color)
		self.display.blit(text, (tile_x, tile_y))		

	def draw_unit(self, ID, unit_x, unit_y):

		if self.id_list[ID] == "Player":
			color = violet
			char = "@"
			text = self.p_font.render(char, True, color)
			self.display.blit(text, (unit_x - 2, unit_y))
		elif self.id_list[ID] == "NPC":
			color = yellow
			char = "N"
			text = self.font.render(char, True, color)
			self.display.blit(text, (unit_x, unit_y)) 
		elif self.id_list[ID] == "Baddie":
			color = red
			char = "B"
			text = self.font.render(char, True, color)
			self.display.blit(text, (unit_x, unit_y))
		
				

	def draw_item(self, ID, item_x, item_y):
		
		if self.id_list[ID] == "Ladder":
			color = orange
			char = "H" 

		text = self.font.render(char, True, color)
		self.display.blit(text, (item_x, item_y))

	def draw_cell(self, color, x, y):
		char = u'\u2533'
		text = self.font.render(char, True, color)
		self.display.blit(text, (x, y))	
