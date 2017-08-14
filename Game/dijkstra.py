from npc import NPC
from player import Player
from baddies import *
from units import Units
from tile import Tile
from objects import *

class Path:
	def __init__(self, start, map):
		self.checked_tiles = []
		self.new_tiles = []
		self.tile_number = 0
		self.max_distance = 20
		path_north = []
		path_east = []
		path_south = []
		path_west = []
		self.paths = {
		0: path_north,
		1: path_east,
		2: path_south,
		3: path_west}

		#next_tile = self.find_path(start, map)

		"temp code"
		temp_next_tile = start
		return(temp_next_tile)

	def	find_path(self, start, map):
		location = start
		distance = 0

		while distance < self.max_distance:
			distance += 1
			path_num = 0
			for x in self.find_neighbors(location):
				if len(self.checked_tiles) > 0:
					for y in self.checked_tiles:
						if x[0] != y["Location"][0] and x[1] != y["Location"][1]:
							self.new_tiles.append(self.new_tile(x, map, distance))
				else:
					new_tile = self.new_tile(x, map, distance)
					self.new_tiles.append(new_tile)
					self.paths[path_num].append(new_tile)

			for x in self.new_tiles:
				if len(self.checked_tiles) = 0:

	def find_neighbors(self, location):
		x = location[0]
		y = location[1]

		north = (x, y-1)
		east = (x+1, y)
		south = (x, y+1)
		west = (x-1, y)

		return(north, east, south, west)

	def new_tile(self, location, map, distance):	
		tile = {}
		tile["Location"] = location
		tile["Number"] = self.tile_number
		tile["Distance"] = distance
		tile["Value"] =self.determine_value(map, location)

		return(tile)

	def determine_value(self, map, location):	
		value = 0

		if isinstance(map[location[0]][location[1]][1], Units)
			value -= 2
			if isinstance(map[location[0]][location[1]][1], Player)
				value -= 2

		return(value)

	
						







#gist.github.com/econchick/4666413

class Dijsktra():
	"example that is probably useless"
	def __init__(self):
		self.nodes = set()
		self.edges = defaultdict(list)
		self.distances = {}

	def add_node(self, value):
		self.nodes.add(value)

	def add_edge(self, from_node, to_node, distance):
	self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance

	def dijsktra(graph, initial):
		visited = {initial: 0}
		path = {}

		nodes = set(graph.nodes)

		while nodes: 
			min_node = None
			for node in nodes:
				if node in visited:
			    	if min_node is None:
			    		min_node = node
			    	elif visited[node] < visited[min_node]:
			      		min_node = node

			if min_node is None:
			  	break

			nodes.remove(min_node)
			current_weight = visited[min_node]

			for edge in graph.edges[min_node]:
			  	weight = current_weight + graph.distance[(min_node, edge)]
			  	if edge not in visited or weight < visited[edge]:
			    	visited[edge] = weight
			    	path[edge] = min_node

		return visited, path