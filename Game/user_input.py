import pygame

class User_Input:

	def __init__(self):

		"""
		 TODO Load controller config if present
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
				self.direction = self.keys[key]
		return(self.direction)		
	"""			
							if self.key == 'w':
								self.direction = "NORTH"
							if self.key == 's':
								self.direction = "SOUTH"
							if self.key == 'a':
								self.direction = "WEST"
							if self.key == 'd':	
								self.direction = "EAST"
							if self.key == "c":
								self.direction = self.default_state"""

		

									
#	def controller_config(self):
