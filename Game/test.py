def build_list(self, start, map, map_size, start_tile):
	unchecked_tiles = []
	checked_tiles = []				
	tiles = self.find_neighbors(start, map, map_size)
	checked_tiles.append(start_tile)
	
	for x in tiles:
		self.tile_number +=1
		self.set_tile_info(x, self.tile_number, self.distance, start)
		unchecked_tiles.append(x)

	while True:

		"break condition"
		if self.distance = self.max_distance:
			break

		"set start point and initial 4 paths"		
		if len(ordered_list) == 0:


	return ordered_list