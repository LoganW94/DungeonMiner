import pygame

class User_Input:

	def __init__(self):

		"""
		 TODO Load controller config if present
		"""
		self.direction = "IDLE"

	def get_input(self):
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				"rework so player can set key for each command"
				key = pygame.key.name(event.key)
				if key == 'w':
					self.direction = "NORTH"
				elif key == 's':
					self.direction = "SOUTH"
				elif key == 'a':
					self.direction = "WEST"
				elif key == 'd':	
					self.direction = "EAST"
				else:
					self.direction = "IDLE"

		return(self.direction)			 
									

