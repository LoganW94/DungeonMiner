

class Camera:

	def __init__(self, width, height, tile_size):
		cam_x = 0
		cam_y = 0
		self.tile_size = tile_size
		self.location = (cam_x, cam_y)
		self.width = width
		self.height = height

	def update(self, player_location):
		"function will figure out, based on the player's location where they are in pixels, and update camera reletive to that location"
		"in coords"
		#print(player_location[0], player_location[1])

		player_x = (player_location[0] * self.tile_size)
		player_y = (player_location[1] * self.tile_size)
#	
		'in pixels'
		cam_x = player_x + self.tile_size/2 - self.height/2
		cam_y = player_y + self.tile_size/2 - self.width/2
		self.location = (cam_x, cam_y)

		
		