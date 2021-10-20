import pygame, time
from pygame.locals import *

pygame.init()
height, width = 1440, 720
font = pygame.font.Font("font.ttf", 36)
screen = pygame.display.set_mode((height, width))

running = True
bg_color = (252, 231, 243)
owipos = [(width // 2) - 200, (height // 2) - 200]
counterpos =  [(width // 2) - 100, (height // 2) - 320]
transparent = (0, 0, 0, 0)
red = (255, 0, 0)
score = 0

owi = pygame.image.load("u.png")
owi2 = pygame.image.load("wah.png")

kaget_sound = pygame.mixer.Sound("kaget.wav")
kaget_sound.set_volume(0.05)
counter = font.render(f"Score : {score}", True, red)

while(running):
	pygame.mixer.init()
	screen.fill(bg_color)
	screen.blit(owi, owipos)
	screen.blit(counter, counterpos)
	
	pygame.display.flip()
	
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			score += 1
			counter = font.render(f"Score : {score}", True, red)
			pygame.mixer.stop()
			screen.fill(bg_color)
			screen.blit(owi2, owipos)
			screen.blit(counter, counterpos)
			kaget_sound.play()
			pygame.display.update()
			time.sleep(0.15)

