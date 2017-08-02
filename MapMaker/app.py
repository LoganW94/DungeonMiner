import pygame
from screen import Screen
import handler
import button
import pointer
import cursor
from newmap import New_Map

"app specific imports"
import json

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

class App:
	'this class handles the app design'
	def __init__(self, handler):

		self.handler = handler
		
		"variables"  
		self.displayWidth = 1600
		self.displayHeight = 900
		self.current_state = 0
		self.map_location = None
		self.current_map = None
		self.left_menu_x = 50
		self.left_menu_y = 50
		self.default_height = 20
		self.lngth = 150
		self.txtbx_y = self.lngth + 30
		self.txt_length = 60
		self.tile_arr =[[]]
		self.button_list = []
		self.description = None
		self.mapsize = None
		self.playerone = "default"
		self.playertwo = "default"
		self.playerthree = "default"
		self.playerfour = "default"
		self.grid = []

		self.font = pygame.font.SysFont(None, 25)

		"define display"
		self.display = Screen.new(self.displayWidth, self.displayHeight, white, 'MapMaker Alpha', 'assets/icon2.png')

		"init objects"
		self.mouse_cursor = cursor.Cursor(self.display)
		self.mouse_pointer = pointer.Pointer(self.displayWidth/2, self.displayHeight/2, self.display, black)

		"Start menu state"
		self.inti_state()
		
		self.set_lists_handler()

	def get_current_state(self):
		return(self.current_state)

	def set_current_state(self, current_state):
		self.current_state = current_state

	def inti_state(self):
		self.set_current_state(0)
		self.mouse_cursor.set_default()
		state = 0

		new_button = button.Button(self.display, "New Map", self.left_menu_x, self.left_menu_y, self.default_height, 80, self.font, grey, state, self.new_map_state)

		load_button =  button.Button(self.display, "Load Map", self.left_menu_x, self.left_menu_y + 30, self.default_height, 85, self.font, grey, state, self.load_state)

		state_list = [new_button, load_button]
		self.button_list = state_list
		self.set_lists_handler()

	def new_map_state(self):
		self.set_current_state(1)
		self.mouse_cursor.set_default()

		state = 1
	
		text_description = button.Display_Box(self.display, "File Name", self.left_menu_x, self.left_menu_y, self.default_height, self.lngth, self.font, white, state)
		description = button.Text_Box(self.display, self.left_menu_x +self.txtbx_y, self.left_menu_y, self.default_height, 200, self.font, state, self.mouse_cursor, self.handler)

		text_mapsize = button.Display_Box(self.display, "Map Size", self.left_menu_x, self.left_menu_y +30, self.default_height, self.lngth, self.font, white, state)
		mapsize = button.Text_Box(self.display, self.left_menu_x +self.txtbx_y, self.left_menu_y +30, self.default_height, 30, self.font, state, self.mouse_cursor, self.handler)

		save_button = button.Button(self.display, "Generate Map", self.left_menu_x, self.left_menu_y + 200, self.default_height, 170, self.font, grey, state, self.create_new_map)

		main_menu_button = button.Button(self.display, "Main Menu", self.left_menu_x, self.left_menu_y + 300, self.default_height, 150, self.font, grey, state, self.inti_state)

		state_list = [text_description, description, text_mapsize, mapsize, save_button, main_menu_button]	

		self.button_list = state_list
		self.set_lists_handler()

	def load_state(self):
		self.set_current_state(2)
		self.mouse_cursor.set_default()
		state = 2

		file_location_box = button.Text_Box(self.display, self.left_menu_x, self.left_menu_y, self.default_height, 200, self.font, state, self.mouse_cursor, self.handler)

		load_map_button = button.Button(self.display, "Load map", self.left_menu_x, self.left_menu_y + 30, self.default_height, 100, self.font, grey, state, self.load_map)

		main_menu_button = button.Button(self.display, "Main Menu", self.left_menu_x, self.left_menu_y + 300, self.default_height, 150, self.font, grey, state, self.inti_state)

		xplorer_launch = button.Button(self.display, "Launch file explorer", self.left_menu_x, self.left_menu_y - 30, self.default_height, 200, self.font, grey, state)

		state_list =[file_location_box, load_map_button, main_menu_button, xplorer_launch]

		self.button_list = state_list
		self.set_lists_handler()	

	def	mapmaker_state(self):
		self.set_current_state(3)
		self.mouse_cursor.set_default()	
		state = 3
		
		text_green = button.Display_Box(self.display, "grass", (self.left_menu_x + 20), self.left_menu_y, self.default_height, self.txt_length, self.font, white, state)
		paint_green = button.Paint_Button(self.display, self.left_menu_x, self.left_menu_y, self.default_height, self.font, green, state, self.mouse_pointer)

		text_grey = button.Display_Box(self.display, "rock", (self.left_menu_x + 20), self.left_menu_y+self.default_height, self.default_height, self.txt_length, self.font, white, state)
		paint_grey = button.Paint_Button(self.display, self.left_menu_x, self.left_menu_y+self.default_height, self.default_height, self.font, grey, state, self.mouse_pointer)

		text_white = button.Display_Box(self.display, "dirt", (self.left_menu_x + 20), self.left_menu_y+(self.default_height*2), self.default_height, self.txt_length, self.font, white, state)
		paint_white = button.Paint_Button(self.display, self.left_menu_x, self.left_menu_y+(self.default_height*2), self.default_height, self.font, orange, state, self.mouse_pointer)

		text_blue = button.Display_Box(self.display, "water", (self.left_menu_x + 20), self.left_menu_y+(self.default_height*3), self.default_height, self.txt_length, self.font, white, state)
		paint_blue = button.Paint_Button(self.display, self.left_menu_x, self.left_menu_y+(self.default_height*3), self.default_height, self.font, blue, state, self.mouse_pointer)

		save_map_array = button.Button(self.display, "Save Map", self.left_menu_x, self.left_menu_y + (self.default_height * 10), self.default_height, 100, self.font, grey, state, self.save_map_array)

		main_menu_button = button.Button(self.display, "Main Menu", self.left_menu_x, self.left_menu_y + 300, self.default_height, 100, self.font, grey, state, self.inti_state)

		state_list =[text_green, paint_green, 
		text_grey, paint_grey, text_white, paint_white, text_blue, 
		paint_blue, save_map_array, main_menu_button]

		self.button_list = state_list
		self.set_lists_handler()

	def create_new_map(self):
		self.description = (self.button_list[1])._txt.title()
		self.mapsize = (self.button_list[3])._txt

		self.map = New_Map(self.display, self.mouse_pointer, self.font)
		self.map.new_map(self.description, self.mapsize, 10)
		self.mapmaker_state()
		self.tile_arr = self.map.get_grid()
		self.handler.set_lists(self.obj_list, self.button_list, self.tile_arr)

	def load_map(self):

		i = self.button_list[0]

		url = i._txt
		url = url + ".json"
		try:
			self.open_file(url)
		except:
			print('no file found @ %s' % url)

		self.map = New_Map(self.display, self.mouse_pointer, self.font)
		self.map.loaded_map(self.json_in)
		self.mapmaker_state()
		self.tile_arr = self.map.get_grid()
		self.handler.set_lists(self.obj_list, self.button_list, self.tile_arr)

	def open_file(self,url):		
		with open(url, "r") as f:
			self.json_in=f.read().replace('\n', '')

	def print_map(self):
		try:
			print(self.json_in)
		except:
			print('no map loaded')

	def save_map_array(self):
		self.map.final_grid(self.tile_arr)

	def set_lists_handler(self):
		self.obj_list = [self.mouse_pointer, self.mouse_cursor]
		self.handler.set_lists(self.obj_list, self.button_list, self.tile_arr)
		self.handler.set_screen(self.display, self.displayWidth, self.displayHeight)
			