# go to terminal (@ bottom of screen) and write "pip install pygame" after PS C: line
import random
import pygame
import math
from settings import *
from sprites import Player, Enemy, Missile, Bomb, Block, Explosion

############################################################
############################################################

pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

# Sounds
shoot_sound = pygame.mixer.Sound("assets/shoot.wav")
enemy_kill = pygame.mixer.Sound("assets/invaderkilled.wav")

# Fonts
score = 0
score_object = SMALL_FONT.render(f"Score: {score}", True, WHITE)
score_rect = score_object.get_rect()
score_rect.center = 100, 20

### SPRITE GROUPS ###
all_sprites = pygame.sprite.Group()              # group for all sprites
player_group = pygame.sprite.Group()             # create sprite group for player
missile_group = pygame.sprite.Group()            # create missile sprite group
enemy_group = pygame.sprite.Group()
bomb_group = pygame.sprite.Group()
block_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()

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

# blocks
start_locations = [50, 190, 340, 480]
for start in start_locations:
    for row_index, row in enumerate(SHEILDS):
        #print(row_index, row)
        for col_index, col in enumerate(row):
            if col == 'x':
                x_pos = col_index*BLOCK_WIDTH + start
                y_pos = row_index*BLOCK_HEIGHT + 500
                block = Block(screen, x_pos, y_pos)
                block_group.add(block)
                all_sprites.add(block_group)

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

    bomb_current_fire = pygame.time.get_ticks()
    if bomb_current_fire - bomb_previous_fire > BOMB_DELAY:
        bomb_previous_fire = bomb_current_fire
        bomber = random.choice(list(enemy_group))
        bomb = Bomb(bomber.rect.centerx - MISSILE_WIDTH // 2, bomber.rect.top)
        bomb_group.add(bomb)
        all_sprites.add(bomb)

    # COLLISION
    enemy_kills = pygame.sprite.groupcollide(missile_group, enemy_group, True, True)
    player_enemy_collide = pygame.sprite.groupcollide(player_group, enemy_group, True, True)
    missile_block_collide = pygame.sprite.groupcollide(missile_group, block_group, True, True)
    bomb_block_collide = pygame.sprite.groupcollide(bomb_group, block_group, True, True)
    enemy_block_collide = pygame.sprite.groupcollide(enemy_group, block_group, False, True)
    bomb_player
    # pygame.sprite.groupcollide(group1, group2, dokill1, dokill2)
    # dokill 1&2 are booleans (use true or false) true means the group disappears when collided, false means it doesn't
    if enemy_kills:
        enemy_kill.play()
        score += 10
        for hit in enemy_kills:
            explosion = Explosion(hit.rect.center)
            explosion_group.add(explosion)
            all_sprites.add(explosion)

    # game over
    if player_enemy_collide:
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

    # text
    score_object = SMALL_FONT.render(f"Score: {score}", True, WHITE)
    screen.blit(score_object, score_rect)

    # call draw and update for each sprite
    bomb_group.draw(screen)
    enemy_group.draw(screen)
    missile_group.draw(screen)
    player_group.draw(screen)
    block_group.draw(screen)
    explosion_group.draw(screen)

    # update all groups
    enemy_group.update(enemy_velocity)
    all_sprites.update()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
