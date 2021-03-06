#Import section
#-------------------------------------
import pygame
from pygame.locals import *
import random
from common_class import Game_object
from variable import *
#-------------------------------------

pygame.init()
screen = pygame.display.set_mode((sc_w,sc_h))
Clock = pygame.time.Clock()

#background
background = pygame.Surface((sc_w,sc_h))
background.fill(bg_color)

#menu
menu = pygame.Surface((100,ssize*max_item))
menu.fill(menu_color)
menu_rect = menu.get_rect()

#submenu
submenu = pygame.Surface((100,ssize))
submenu.fill(submenu_color)


player = Game_object("player",player_color,"sp1.png")

obj1 = Game_object("object1",(90,90,90),"sp2.png")
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
		print(i.rect.left,i.rect.top,pos)
		if (i.rect.left < pos[0]) and (i.rect.left > pos[0]-ssize):
			 if (i.rect.top< pos[1]) and (i.rect.top > pos[1]-ssize):
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

def show_submenu(screen,menu,submenu):
	global ssize,max_item
	sc = 1
	selected_object = select_obj(all_object,pygame.mouse.get_pos())
	print(selected_object)
	if selected_object :
		pass
	else:
		sc = 0
	pos = pygame.mouse.get_pos()
	sub_pos = pygame.mouse.get_pos()
	while sc:

		screen.blit(menu,pos)
		screen.blit(submenu,sub_pos)
		cur_pos = pygame.mouse.get_pos()
		print(cur_pos,pos)
		if (cur_pos[0] >= pos[0]) and (cur_pos[0] <= pos[0] + 100):
			print("cycle")
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
	pygame.display.update()

while True:
	#screen.blit(background,(0,0))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_UP:
				#player.y -= ssize
				pass
		elif event.type == MOUSEBUTTONDOWN:
			if event.button == 3:
				#Second cycle
				#show_submenu(screen,menu,submenu)
				pass
			elif event.button == 1:
				if turn == "player":
					player.target = conv(pygame.mouse.get_pos())
					if player.update(all_object):
						turn = "other"
	if turn == "other":
		rand_move = random.randint(0,100)
		if rand_move < 40:
			obj1.target = conv((player.rect.left,player.rect.top))
			if obj1.update(all_object):
				turn = "player"
		else:
			obj1.target = (0,0)
			turn = "player"
	Clock.tick(60)
	rects = all_sprites.draw(screen)
	pygame.display.update(rects)
