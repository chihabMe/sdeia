import pygame,sys

pygame.init()

width,height = 600,400
screen = pygame.display.set_mode((width,height))
clock  = pygame.time.Clock()
sky_height = int(0.8*height)
ground_height = int(0.2*height)
font = pygame.font.Font(None,25)

sky = pygame.Surface((width,sky_height))
ground = pygame.Surface((width,ground_height))
score = font.render('score 0',False,'black')
sky.fill('aqua')
ground.fill("green")
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit( )
	screen.blit(sky,(0,0))
	screen.blit(ground,(0,height-ground_height))
	screen.blit(score,(10,10))
	pygame.display.update()	
	clock.tick(60)
