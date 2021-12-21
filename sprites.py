import pygame
import random
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, image_path):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = DISPLAY_WIDTH // 2, DISPLAY_HEIGHT - self.rect.height*3
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

    def __init__(self, image_path, x, y, value):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.value = value

    def update(self, x_velo):
        self.rect.x += x_velo


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


class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.y_velo = 2

        self.image = pygame.Surface((BOMB_HW, BOMB_HW))
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        pygame.draw.rect(self.image, PINK, [self.rect.x, self.rect.y, BOMB_HW, BOMB_HW])

    def update(self):
        self.rect.y += self.y_velo

        if self.rect.bottom >= DISPLAY_HEIGHT:
            self.kill()


class Block(pygame.sprite.Sprite):
    def __init__(self, display, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((BLOCK_WIDTH, BLOCK_HEIGHT))
        self.image.fill(BLOCK_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        pygame.draw.rect(display, BLOCK_COLOR, [self.rect.x, self.rect.y, self.rect.width, self.rect.height])


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = EXPLOSIONS[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.frame_delay = 50
        self.kill_center = center
        self.previous_update = pygame.time.get_ticks()

    def update(self):
        current_update = pygame.time.get_ticks()
        if current_update - self.previous_update > self.frame_delay:
            self.previous_update = current_update
            self.frame += 1
        if self.frame == len(EXPLOSIONS):
            self.kill()
        else:
            self.image = EXPLOSIONS[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = self.kill_center


class Ufo(pygame.sprite.Sprite):
    def __init__(self, image_path):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.width*2, self.rect.height*3
        self.x_velo = 1

    def update(self):
        self.rect.x += self.x_velo
        if self.rect.right > DISPLAY_WIDTH or self.rect.left < 0:
            self.x_velo *= -1
