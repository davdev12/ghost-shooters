import pygame
import random

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((618, 359)) # , flags=pygame.NOFRAME
pygame.display.set_caption("Pygame davbot12 Game")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

bg = pygame.image.load('images/bg.png').convert_alpha()

walk_left = [
    pygame.image.load('images/player_left/player_left1.png').convert_alpha(),
    pygame.image.load('images/player_left/player_left2.png').convert_alpha(),
    pygame.image.load('images/player_left/player_left3.png').convert_alpha(),
    pygame.image.load('images/player_left/player_left4.png').convert_alpha(),
]
walk_right = [
    pygame.image.load('images/player_right/player_right1.png').convert_alpha(),
    pygame.image.load('images/player_right/player_right2.png').convert_alpha(),
    pygame.image.load('images/player_right/player_right3.png').convert_alpha(),
    pygame.image.load('images/player_right/player_right4.png').convert_alpha(),
]


ghost = pygame.image.load('images/ghost.png').convert_alpha()
ghost_list_in_game = []


player_anim_count = 0
bg_x = 0

player_speed = 5
player_x = 150
player_y = 250

is_jump = False
jump_count = 8

lose_sound = pygame.mixer.Sound('sounds/Oops.wav')

shooting_sound = pygame.mixer.Sound('sounds/laser_shoot.wav')

bg_sound = pygame.mixer.Sound('sounds/bg.mp3')
bg_sound.play(loops=-1)

ghost_timer = pygame.USEREVENT +1
pygame.time.set_timer(ghost_timer, 2500)

label = pygame.font.Font('fonts/Bungee-Regular.ttf', 40)
lose_label = label.render('You lose!', False, (116, 52, 235))
restart_label = label.render('Try again', False, (235, 52, 52))
restart_label_rect = restart_label.get_rect(topleft=(180, 200))

bullets_label = pygame.font.Font('fonts/Bungee-Regular.ttf', 25)
bullets_left = 9999
bullet = pygame.image.load('images/bullet.png').convert_alpha()
bullets = []

counter_label = pygame.font.Font('fonts/Bungee-Regular.ttf', 30)
hit_counter = 9999999

gameplay = True

running = True
while running:
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 618, 0))

    if gameplay:
        # display hit_counter
        screen.blit(counter_label.render(f'Hit ghosts: {hit_counter:03d}', False, (231, 235, 16)), (340, 15))
        screen.blit(bullets_label.render(f'Bullets left: {bullets_left:03d}', False, (230, 235, 16)), (20, 15))
        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

        if ghost_list_in_game:
            for (i, el) in enumerate(ghost_list_in_game):
                screen.blit(ghost, el)
                el.x -= 10

                if el.x < -10:
                    ghost_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    gameplay = False
                    bg_sound.stop()
                    lose_sound.play()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 200:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_UP]:
                is_jump = True
        else:
            if jump_count >= -8:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 8
        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 2
        if bg_x == -618:
            bg_x = 0

        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 10

                if el.x > 630:
                    bullets.pop(i)

                if ghost_list_in_game:
                    for (index, ghost_el) in enumerate(ghost_list_in_game):
                        if el.colliderect(ghost_el):
                            
                            ghost_list_in_game.pop(index)
                            bullets.pop(i)
                            hit_counter += 1

    else:
        screen.fill((85, 255, 0))
        screen.blit(lose_label, (180, 100))
        screen.blit(restart_label, restart_label_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            bg_sound.play(loops=-1)
            player_x = 150
            ghost_list_in_game.clear()
            bullets.clear()
            bullets_left = 10
            hit_counter = 0
        
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(620, random.randint(150, 250))))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_SPACE and bullets_left > 0:
            shooting_sound.play()
            bullets.append(bullet.get_rect(topleft=(player_x + 30, player_y + 10)))
            bullets_left -= 1

    clock.tick(20)
