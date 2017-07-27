"""
draws world to screen

gets map_arr from world
"""
from screen import Screen
import pygame
from camera import Camera

"colors"
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (211,211,211)
yellow = (255,255,0)
violet = (160,10,226)
orange = (255,165,0)

display_width = 800
display_height = 600

class Draw_World:

	def __init__(self):
		self.display = Screen.new(display_width, display_height, red, "Dungeon Miner")
		self.cam = Camera(display_height, display_width)

	def draw(self, world_json):
		self.display.fill(white)
		map_arr = world_json["Map"]
		"should check to see if tile is visible to camera, and if so draws it."
		for x in range(world_json["Size"]):
			for y in range(world_json["Size"]):
				tile = map_arr[x][y][0]
				
		
