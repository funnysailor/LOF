#!/usr/bin/env python

import pygame
from variable import *
#Common class for object in game

class game_object(pygame.sprite.DirtySprite):
	def __init__(self,name,color,fimage):
		pygame.sprite.DirtySprite.__init__(self)
		self.name = name
		self.color = color
		self.image = pygame.image.load(fimage).convert()
		self.rect = self.image.get_rect()
		self.target = (0,0)
		self.dirty = 0
	def menu_action(self,menu_id):
		print("menu for %s you select %s submenu"%(self.name,menu_id))
		
	def update(self,rect_list):
		if self.target == (0,0):return 0
		dir_x = 0
		dir_y = 0
		t_x = self.target[0]
		t_y = self.target[1]
		x = self.rect.left
		y = self.rect.top
		if x > t_x:dir_x=ssize*(-1)
		elif x < t_x:dir_x=ssize
		if y > t_y:dir_y=ssize*(-1)
		elif y < t_y:dir_y=ssize
		self.rect.move_ip((dir_x,dir_y))
		co = self.check_collide(rect_list)
		if co:
			self.rect.move_ip((dir_x*(-1),dir_y*(-1)))
			print co
		self.dirty = 1
		return 1

	def check_collide(self,rect_list):
		for i in rect_list:
			if i == self:
				continue
			elif self.rect.colliderect(i.rect):
				return i.name
			else:
				return 0
