

class Intro_Animation:
	def __init__(self):
		self.load_assets()
		self.counter = 0
		self.state = 0
		"temp code"
		self.text1 = "Dungeon Miner pre pre pre alpha"
		self.text2 = "Ace Games inc"
		self.text3 = "Copyright 2016"
		self.text4 = "Complaints dept: @realDonaldTrump"
		self.text5 = " "
		self.texts = {
		0: self.text1,
		1: self.text2,
		2: self.text3,
		3: self.text4,
		4: self.text5}

		self.current_text = self.text1

	def update(self):

		if self.counter <= 100:
			state = 0
		elif self.counter <= 200:
			state = 1
		elif self.counter <= 300:
			state = 2
		elif self.counter <= 400:
			state = 3
		elif self.counter >= 500:
			self.state = 2				
		self.current_text = self.texts[state]
		self.counter += 1

	def return_intro(self):
		return(self.current_text)

	def change_state(self):
		return(self.state)		

	def load_assets(self):	
		"Loads menu graphics"