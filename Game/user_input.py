import pygame

class User_Input:

	def __inti__(self):

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
				if key == 'W':
					self.direction = "NORTH"
				if key == 'S':
					self.direction = "SOUTH"
				if key == 'A':
					self.direction = "WEST"
				if key == 'D':	
					self.direction = "EAST"
				else:
					self.direction = "IDLE" 
									

