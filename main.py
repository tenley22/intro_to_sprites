# go to terminal (@ bottom of screen) and write "pip install pygame" after PS C: line
import pygame
import math
from settings import *
from sprites import Player, Enemy, Missile

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

# Player
player = Player("assets/player.png")            # create player object
player_group.add(player)                        # add player to its group
all_sprites.add(player)                         # add player to sprites group

# enemy
for row in range(5):
    if row == 0:
        enemy_img = RED_ALIEN
    elif 1 <= row < 3:
        enemy_img = GREEN_ALIEN
    else:
        enemy_img = YELLOW_ALIEN
    for column in range(10):
        mult = SPACING
        enemy = Enemy(enemy_img, 5 + mult * column, 10 + mult * row, row)
        enemy_group.add(enemy)
        all_sprites.add(enemy)


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

    enemy_kills = pygame.sprite.groupcollide(missile_group, enemy_group, True, True)
    # pygame.sprite.groupcollide(group1, group2, dokill1, dokill2)
    # dokill 1&2 are booleans (use true or false) true means the group disappears when collided, false means it doesn't
    if enemy_kills:
        enemy_kill.play()

    screen.fill(BLACK)

    enemy_group.draw(screen)
    missile_group.draw(screen)
    player_group.draw(screen)               # call draw and update for each sprite
    all_sprites.update()                    # all_sprites take care of calling all sprite updates

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
