import pygame

def create_player():
    return pygame.Rect(180, 450, 50, 50)

def move_player(player, keys, width, height):
    
    if keys[pygame.K_LEFT]:
        player.x -= 4
    
    if keys[pygame.K_RIGHT]:
        player.x += 4
        
    if keys[pygame.K_UP]:
        player.y -= 4
        
    if keys[pygame.K_DOWN]:
        player.y += 4
    
    
    if player.right > width:
        player.right = width
    if player.left < 0:
        player.left = 0
    if player.top < 0:
        player.top = 0
    if player.bottom > height:
        player.bottom = height
        