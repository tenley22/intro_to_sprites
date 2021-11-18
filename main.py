# go to terminal (@ bottom of screen) and write "pip install pygame" after PS C: line
import pygame
import math
import random
from settings import *
from sprites import Player, Enemy, Missile

############################################################
############################################################

pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

# Sounds
shoot_sound = pygame.mixer.Sound("assets/shoot.wav")

### SPRITE GROUPS ###
all_sprites = pygame.sprite.Group()              # group for all sprites
player_group = pygame.sprite.Group()             # create sprite group for player
missile_group = pygame.sprite.Group()            # create missile sprite group

# Player
player = Player("assets/player.png")            # create player object
player_group.add(player)                        # add player to its group
all_sprites.add(player)                         # add player to sprites group



running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                missile = Missile(player.rect.centerx - MISSILE_WIDTH//2, player.rect.top)
                missile_group.add(missile)
                all_sprites.add(missile)
                shoot_sound.play

    screen.fill(BLACK)

    missile_group.draw(screen)
    player_group.draw(screen)               # call draw and update for each sprite
    all_sprites.update()                    # all_sprites take care of calling all sprite updates

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
