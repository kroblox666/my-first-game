import pygame

def create_player():
    return pygame.Rect(180, 450, 50, 50)

def move_player(player, keys, width):
    
    if keys[pygame.K_LEFT]:
        player.x -= 4
    
    if keys[pygame.K_RIGHT]:
        player.x += 4
    
    
    if player.right > width:
        player.right = width
    if player.left < 0:
        player.left = 0
        