import pygame
from player import create_player, move_player
from enemy import create_enemies, move_enemies
from bullets import create_bullet, move_bullets

pygame.init()

WIDTH = 400
HEIGTH = 500
    
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("динозавр бегает от метиоритов")

clock = pygame.time.Clock()

player = create_player()

enemies = create_enemies(5, WIDTH)
bullets = []
cooldown = 15
bullet_cooldown = cooldown

running = True

while running:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()
    
    keys = pygame.key.get_pressed()
    
    if bullet_cooldown > 0:
        bullet_cooldown -= 1
        
    if keys[pygame.K_SPACE]:
        if bullet_cooldown == 0:
            bullets.append(create_bullet(player.centerx, player.top))
            bullet_cooldown = cooldown
    
    
    
    
    move_player(player, keys, WIDTH)
    move_enemies(enemies, HEIGTH, WIDTH, player.width)
    move_bullets(bullets)
    
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                enemy.y = -50
                bullet.y = -100
            
    
    clock.tick(60)
    screen.fill("green")

    pygame.draw.rect(screen, "black", player)
    
    for enemy in enemies:
        pygame.draw.rect(screen, "white", enemy)
        
        if player.colliderect(enemy):
            running = False
            
    for bullet in bullets:
        pygame.draw.rect(screen, "red", bullet )
    
    pygame.display.update()
