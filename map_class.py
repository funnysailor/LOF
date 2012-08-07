#Map class
from variable import *
from tile import Tile

class Game_map():
	def __init__(self):
		self.size = (0,0)
		self.text_map = []
		self.tile_map = []
		self.objects = []
	def generate_text_map(self):
		for y in self.size[1]:
			temp = []
			for x in self.size[0]:
				temp.append(ter0)
			self.text_map.append(temp)
	def generate_tile_map(self):
		for y in self.size[1]:
			for x in self.size[0]:
				self.tile_map.append(Tile(x,y,"t1.png"))
			
