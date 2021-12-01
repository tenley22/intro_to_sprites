import pygame
import random
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, image_path):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = DISPLAY_WIDTH // 2, DISPLAY_HEIGHT - self.rect.height
        self.x_velo = 0  # velocity

    def update(self):
        self.rect.x += self.x_velo

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.x_velo = 5
        elif keys[pygame.K_LEFT]:
            self.x_velo = -5
        else:
            self.x_velo = 0

        if self.rect.right >= DISPLAY_WIDTH:
            self.rect.right = DISPLAY_WIDTH
        if self.rect.left <= 0:
            self.rect.left = 0


class Enemy(pygame.sprite.Sprite):
    y_level = 0
    change_x = 1
    row_height = SPACING

    def __init__(self, image_path, x_val, y_val, row):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image_path)
        self.y_velo = 0
        self.x_velo = 2
        self.rect = self.image.get_rect()
        self.rect.x = x_val
        self.rect.y = y_val
        self.row = row

    def update(self):
        self.rect.x += Enemy.change_x

        if self.rect.right >= DISPLAY_WIDTH or self.rect.left <= 0:
            Enemy.y_level += 1
            Enemy.change_x *= -1
        self.rect.y = (Enemy.y_level + self.row)*(SPACING)


class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.y_velo = 2

        self.image = pygame.Surface((MISSILE_WIDTH, MISSILE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        pygame.draw.rect(self.image, WHITE, [self.rect.x, self.rect.y, MISSILE_WIDTH, MISSILE_HEIGHT])

    def update(self):
        self.rect.y -= self.y_velo

        if self.rect.bottom <= 0:
            self.kill()


class Block():
    pass