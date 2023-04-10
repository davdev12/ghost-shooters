import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300)) # , flags=pygame.NOFRAME
pygame.display.set_caption("Pygame davbot12 Game")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

player = pygame.image.load('images/icon.png')

running = True
while running:
    screen.blit(player, (100, 50))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


