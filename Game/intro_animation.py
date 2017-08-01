

class Intro_Animation:
	def __init__(self):
		self.load_assets()
		self.counter = 0
		self.state = 0

		"temp code"
		self.texts = {
		0: "Dungeon Miner",
		1: "Ace Games inc",
		2: "Copyright 2017",
		3: "Complaints dept: @realDonaldTrump",
		4: " "}

		self.current_text = self.texts[0]

	def update(self):

		if self.counter <= 100:
			state = 0
		elif self.counter <= 200:
			state = 1
		elif self.counter <= 300:
			state = 2
		elif self.counter <= 400:
			state = 3
		elif self.counter <= 500:
			self.state = 1
			state = 4				
		self.current_text = self.texts[state]
		self.counter += 0.5

	def return_intro(self):
		return(self.current_text)

	def change_state(self):
		return(self.state)		

	def load_assets(self):	
		"Loads menu graphics"