

class Camera:

	def __init__(self, width, height):
		self.cam_x = 0
		self.cam_y = 0
		self.location = (self.cam_x, self.cam_y)
		self.width = width
		self.height = height

	def update(self, player_location):
		"function will figure out, based on the player's location where they are in pixels, and update camera reletive to that location"

		self.location = (self.cam_x, self.cam_y)

		
		