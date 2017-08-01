

class Camera:

	def __init__(self, width, height, tile_size):
		cam_x = 0
		cam_y = 0
		self.tile_size = tile_size
		self.location = (cam_x, cam_y)
		self.width = width
		self.height = height

	def update(self, location):
		"converts to pixel"
		x = (location[0] * self.tile_size)
		y = (location[1] * self.tile_size)
	
		'moves everything to center of screen'
		cam_x = x + self.tile_size/2 - self.height/2
		cam_y = y + self.tile_size/2 - self.width/2
		self.location = (cam_x, cam_y)
