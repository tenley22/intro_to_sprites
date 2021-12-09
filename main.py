# go to terminal (@ bottom of screen) and write "pip install pygame" after PS C: line
import random

import pygame
import math
from settings import *
from sprites import Player, Enemy, Missile, Bomb

############################################################
############################################################

pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

# Sounds
shoot_sound = pygame.mixer.Sound("assets/shoot.wav")
enemy_kill = pygame.mixer.Sound("assets/invaderkilled.wav")

### SPRITE GROUPS ###
all_sprites = pygame.sprite.Group()              # group for all sprites
player_group = pygame.sprite.Group()             # create sprite group for player
missile_group = pygame.sprite.Group()            # create missile sprite group
enemy_group = pygame.sprite.Group()
bomb_group = pygame.sprite.Group()

# Player
player = Player("assets/player.png")            # create player object
player_group.add(player)                        # add player to its group
all_sprites.add(player)                         # add player to sprites group

# enemy
x_offset = 30
y_offset = 100
v_spacing = DISPLAY_HEIGHT//18
h_spacing = DISPLAY_WIDTH//12
for row in range(6):
    if row == 0:
        enemy_img = RED_ALIEN
    elif 0 < row < 3:
        enemy_img = GREEN_ALIEN
    else:
        enemy_img = YELLOW_ALIEN
    for column in range(10):
        x_pos = column*h_spacing + x_offset
        y_pos = row*v_spacing + y_offset
        enemy = Enemy(enemy_img, x_pos, y_pos)
        enemy_group.add(enemy)


missile_previous_fire = pygame.time.get_ticks()
bomb_previous_fire = pygame.time.get_ticks()

running = True
enemy_velocity = 1

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                missile_current_fire = pygame.time.get_ticks()
                if missile_current_fire - missile_previous_fire > MISSILE_DELAY:
                    missile_previous_fire = missile_current_fire
                    missile = Missile(player.rect.centerx - MISSILE_WIDTH//2, player.rect.top)
                    missile_group.add(missile)
                    all_sprites.add(missile)
                    shoot_sound.play

    bomber = random.choice(list(enemy_group))
    bomb_current_fire = pygame.time.get_ticks()
    if bomb_current_fire - bomb_previous_fire > BOMB_DELAY:
        bomb = Bomb(bomber.rect.centerx - MISSILE_WIDTH // 2, bomber.rect.top)
        bomb_group.add(bomb)
        all_sprites.add(bomb)


    enemy_kills = pygame.sprite.groupcollide(missile_group, enemy_group, True, True)
    player_enemy_collide = pygame.sprite.groupcollide(player_group, enemy_group, True, True)
    #bomb_collide = pygame.sprite.groupcollide(player_group, bomb_group, True, True)
    # pygame.sprite.groupcollide(group1, group2, dokill1, dokill2)
    # dokill 1&2 are booleans (use true or false) true means the group disappears when collided, false means it doesn't
    if enemy_kills:
        enemy_kill.play()
    # game over
    if player_enemy_collide: #or bomb_collide:
        running = False
    enemies = enemy_group.sprites()
    for enemy in enemies:
        if enemy.rect.right >= DISPLAY_WIDTH:
            enemy_velocity = -1
            if enemies:
                for alien in enemies:
                    alien.rect.y += 2

        elif enemy.rect.x <= 0:
            enemy_velocity = 1
            if enemies:
                for alien in enemies:
                    alien.rect.y += 2

    screen.fill(BLACK)

    bomb_group.draw(screen)
    enemy_group.draw(screen)
    missile_group.draw(screen)
    player_group.draw(screen)               # call draw and update for each sprite

    # update all groups
    enemy_group.update(enemy_velocity)
    all_sprites.update()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
