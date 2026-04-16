import pygame

def create_bullet(x, y):
    return pygame.Rect(x, y, 5, 10)

def move_bullets(bullets):
    for bullet in bullets:
        
        bullet.y -= 6
