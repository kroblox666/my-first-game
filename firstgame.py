import pygame
import random
pygame.init()

WIDTH = 400
HEIGTH = 500
enemies = []

for i in range(5):
    x = random.randint(0, WIDTH-40)
    y = random.randint(-800, -40)
    enemies.append(pygame.Rect(x, y, 50, 50))
    
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("динозавр бегает от метиоритов")

player = pygame.Rect(180, 450, 50, 50)

clock = pygame.time.Clock()

running = True

while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 9
    if keys[pygame.K_RIGHT]:
        player.x += 9
        
    if player.right > WIDTH:
        player.right = WIDTH
    if player.left < 0:
        player.left = 0
        
        
    clock.tick(60)
    screen.fill("green")

    pygame.draw.rect(screen, "black", player)
    
    for enemy in enemies:
        enemy.y += 9
        if enemy.y > HEIGTH:
            enemy.y = -50
            enemy.x = random.randint(0, WIDTH-player.width)
        pygame.draw.rect(screen, "white", enemy)
        
        if player.colliderect(enemy):
            running = False
    
    pygame.display.update()
