"""
draws world to screen

gets map_arr from world
"""
from screen import Screen
import pygame

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

	def __inti__(self):
		print("init")
#		self.world = w
		self.display = Screen.new(display_width, display_height, red, "Rouge like")

	def draw(self):
		self.display.fill(white)	
		print("draw")
		
