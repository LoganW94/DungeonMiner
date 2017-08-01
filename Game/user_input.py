import pygame

class User_Input:

	def __init__(self):

		"""
		TODO: Load controller config 
		TODO: rework keys to a txt doc loaded into all states and updated on save/controller config  
		"""
		self.default_state = "IDLE"
		self.direction = self.default_state
		self.keys={
		"w": "NORTH", 
		"s": "SOUTH", 
		"a": "WEST", 
		"d": "EAST"}

	def get_input(self):
		self.direction = self.default_state
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				"rework so player can set key for each command"
				key = pygame.key.name(event.key)
				if key in self.keys:
					self.direction = self.keys[key]
	
		return(self.direction)		
	

									
#	def controller_config(self):
