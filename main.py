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

player_img = pygame.image.load("sprites/player.png")
enemy_img = pygame.image.load("sprites/enemy.png")
bullet_img = pygame.image.load("sprites/bullet.png")
background_img = pygame.image.load("sprites/space.jpg")


player_img = pygame.transform.scale(player_img, (50, 50))
enemy_img = pygame.transform.scale(enemy_img, (40, 40))
bullet_img = pygame.transform.scale(bullet_img, (5, 10))
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGTH))

score = 0
font = pygame.font.SysFont(None, 30)

def draw_game_over(screen, width, height, score):
    font_large = pygame.font.SysFont(None, 60)
    font_small = pygame.font.SysFont(None, 30)
    
    text_game_over = font_large.render("ты проиграл хахаххаахха", True, (235, 173, 241))
    text_score = font_small.render(score, True, (255, 255, 255))
    text_restart = font_small.render("Нажмите w для перезапуска", True, (255, 255, 255))
    
    screen.blit(text_game_over, (width // 2 - text_game_over.get_width(), height//2-80))
    screen.blit(text_score, (width // 2 - text_score.get_width(), height//2-10))
    screen.blit(text_restart, (width // 2 - text_restart.get_width(), height//2+40))

enemies = create_enemies(5, WIDTH)
bullets = []
cooldown = 0    
bullet_cooldown = cooldown

running = True
game_over = False

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
    
    
    
    
    move_player(player, keys, WIDTH, HEIGTH )
    move_enemies(enemies, HEIGTH, WIDTH, player.width)
    move_bullets(bullets)
    
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                enemy.y = -50
                bullet.y = -100
                score += 1
            
    
    clock.tick(60)
    screen.blit(background_img, (0, 0))
    screen.blit(player_img, (player.x, player.y))
    
    
    for enemy in enemies:
        screen.blit(enemy_img, (enemy.x, enemy.y))
        
        if player.colliderect(enemy):
            running = False
            
    for bullet in bullets:
        screen.blit(bullet_img, (bullet.x, bullet.y))
        
        text = font.render(f"Счёт: {score}", True, "white")
        screen.blit(text, (10, 10))
    pygame.display.update()















































































































































































































































































































































































































































































































