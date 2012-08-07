#Tile Class
import pygame
from variable import *

class Tile():
	def __init__(self,x,y,fimage):
		self.x = x
		self.y = y
		self.image = pygame.image.load(fimage).convert()
	def draw():
		pass
