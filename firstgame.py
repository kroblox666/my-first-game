import pygame

pygame.init()

WIDTH = 400
HEIGTH = 500

screen = pygame.display.set_mode((WIDTH,HEIGTH))
pygame.display.set_caption("потм будет название")

player = pygame.Rect(180, 450, 50, 50)

clock = pygame.time.Clock()

while True:
  for events in pygame.event.get():
    if events.type == pygame.QUIT:
      exit()
      
  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_LEFT]:
    player.x -= 1
  if keys[pygame.K_RIGHT]:
    player.x += 1
    
  clock.tick(60)
  screen.fill("green")
  
  pygame.draw.rect(screen, "black", player)
  pygame.display.update()