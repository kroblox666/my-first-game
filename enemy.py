import pygame
import random

def create_enemies(count, width):
    enemies = []
    
    for i in range(count):
        x = random.randint(0, width - 40)
        y = random.randint(-800, -40)
        enemies.append(pygame.Rect(x, y, 50, 50))
    
    return enemies


def move_enemies(enemies, height, width, player_width):
    for enemy in enemies:
        enemy.y += 4
        
        if enemy.y > height:
            enemy.y = -50
            enemy.x = random.randint(0, width-player_width)