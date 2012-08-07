

import pygame
from pygame.locals import *
import random


#EDITED

#Variable
max_item = 10
sc_w = 800
sc_h = 600
bg_color = (0,120,120)
menu_color = (255,255,255)
submenu_color = (0,0,0)
player_color = (100,9,80)
player_color2 = (0,180,3)
ssize = 32 # Sprite size
turn = "player"

pygame.init()
screen = pygame.display.set_mode((sc_w,sc_h))
Clock = pygame.time.Clock()

#background
background = pygame.Surface((sc_w,sc_h))
background.fill(bg_color)

#menu
menu = pygame.Surface((100,ssize*max_item))
menu.fill(menu_color)

#submenu
submenu = pygame.Surface((100,ssize))
submenu.fill(submenu_color)

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
		
	def update(self):
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
		co = self.check_collide(all_object)
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

player = game_object("player",player_color,"sp1.png")

obj1 = game_object("object1",(90,90,90),"sp2.png")
all_object = [player,obj1]

all_sprites = pygame.sprite.LayeredDirty(all_object)
all_sprites.clear(screen, background)

player.check_collide(all_object)
#Def section
def change_color(m_item):
	if m_item == 0:
		player.surface.fill(player_color2)
	if m_item == 1:
		player.surface.fill(player_color)

def select_obj(all_obj,pos):
	for i in all_obj:
		print(i.x,i.y,pos)
		if (i.x < pos[0]) and (i.x > pos[0]-ssize):
			 if (i.y < pos[1]) and (i.y > pos[1]-ssize):
				 print("you select %s"%(i,))
				 return i

def conv(coord):
	x=coord[0]
	y=coord[1]
	x=(x/ssize)*ssize
	y=(y/ssize)*ssize
	print(x,y)
	return (x,y)

def check_collide(s1,s2):
	if s1.rect.colliderect(s2.rect):
		print("COLLIDE!")
while True:
	screen.blit(background,(0,0))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_UP:
				#player.y -= ssize
				pass
			elif event.key == K_DOWN:
				#player.y += ssize
				pass
			elif event.key == K_LEFT:
				#player.x -= ssize
				pass
			elif event.key == K_RIGHT:
				#player.x += ssize
				pass
		elif event.type == MOUSEBUTTONDOWN:
			if event.button == 3:
				sc = 1
				selected_object = select_obj(all_object,pygame.mouse.get_pos())
				if selected_object :
					pass
				else:
					sc = 0
				
				#Second cycle
				pos = pygame.mouse.get_pos()
				sub_pos = pygame.mouse.get_pos()
				while sc:
					screen.blit(menu,pos)
					screen.blit(submenu,sub_pos)
					cur_pos = pygame.mouse.get_pos()
					if (cur_pos[0] > pos[0]) and (cur_pos[0] < pos[0] + 100):
						menu_item = (cur_pos[1] - pos[1])/ssize
						if ( menu_item < max_item ) and ( menu_item >= 0):
							sub_pos = pos
							sub_pos = (sub_pos[0],sub_pos[1]+(menu_item*ssize))
					for event in pygame.event.get():
						if event.type == QUIT:
							pygame.quit()
							sys.exit()
						elif event.type == MOUSEBUTTONDOWN:
							if event.button == 3:
								sc = 0
							if event.button == 1:
								if (cur_pos[0] > pos[0]) and (cur_pos[0] < pos[0] + 100):
									print("You select %s item"%(menu_item))
									selected_object.menu_action(menu_item)
									sc = 0
								else:
									sc = 0
					pygame.display.update()
					
			elif event.button == 1:
				if turn == "player":
					player.target = conv(pygame.mouse.get_pos())
					if player.update():
						player.check_collide(all_sprites)
						turn = "other"
	if turn == "other":
		rand_move = random.randint(0,100)
		if rand_move < 40:
			obj1.target = conv((player.rect.left,player.rect.top))
			if obj1.update():
				obj1.check_collide(all_sprites)
				turn = "player"
		else:
			obj1.target = (0,0)
			turn = "player"
	Clock.tick(60)
	rects = all_sprites.draw(screen)
	pygame.display.update(rects)
