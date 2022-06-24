#Programme importen
import pygame
import random
import math
import time

#Spielfeld
pygame.init()
height=600 #Maße
width=600 #Maße
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('CODE HUB')

green=(0,150,0)
blue=(0,0,250)
clock=pygame.time.Clock()

scale=20

playerx=random.choice(range(0,580,20))
playery=random.choice(range(0,580,20))
player_height=18
player_width=18
playerx_change=0
playery_change=0
player_color=(0,0,255)
playerx_position=[]
playery_position=[]

index_x=0
index_y=0
total=1

gameover=False

food_width=17
food_height=17
foodx=random.choice(range(0,580,20))
foody=random.choice(range(0,580,20))
food_color=(255,255,255)


font=pygame.font.Font('freesansbold.ttf',32)
text=font.render('GAME OVER',True,green,blue)
textRect=text.get_rect()
textRect.center=(width//2,height//2)

def food(x,y,w,h,color):
	pygame.draw.rect(screen,color,(x,y,w,h))

def player(x,y,w,h,color):
	pygame.draw.rect(screen,color,(x,y,w,h))

def collision(x1,x2,y1,y2):
	distance=math.sqrt(pow((x1-x2),2)+pow((y1-y2),2))
	if distance<15:
		return True

loop=True

while loop:
	screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			loop=False
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT and playerx_change != scale:
				playerx_change=-scale
				playery_change=0
			elif event.key==pygame.K_RIGHT and playerx_change!=-scale:
				playerx_change=scale
				playery_change=0
			elif event.key==pygame.K_UP and playery_change!=scale:
				playerx_change=0
				playery_change=-scale
			elif event.key==pygame.K_DOWN and playery_change!=-scale:
				playerx_change=0
				playery_change=scale

	playerx+=playerx_change
	playery+=playery_change	
	if playerx>580 :
		playerx_change=0
		playerx=580
		gameover=True
	elif playerx<0:
		playerx_change=0
		playerx=0
		gameover=True
	if playery>580:
		playery=580
		playery_change=0
		gameover=True	
	elif playery<0:
		pllayery=0
		playery_change=0
		gameover=True

	if collision(playerx,foodx,playery,foody):
		foodx= random.choice(range(0,580,20))
		foody=random.choice(range(0,580,20))
		total+=1
	if total>1:
		for x in range(1,total):
			index_x=len(playerx_position)-x
			index_y=len(playery_position)-x
			player(playerx_position[index_x],
				playery_position[index_y],player_width,player_height,player_color)
			if collision(playerx,playerx_position[index_x],playery,playery_position[index_y]):
				gameover=True
	
	if gameover==True:
		screen.blit(text,textRect)
		playery_change=0
		playerx_change=0
	playerx_position.append(playerx)
	playery_position.append(playery)

	food(foodx,foody,food_width,food_height,food_color)
	player(playerx,playery,player_width,player_height,player_color)
	pygame.display.update()
	clock.tick(5)