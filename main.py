import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300)) # , flags=pygame.NOFRAME
pygame.display.set_caption("Pygame davbot12 Game")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

square = pygame.Surface((50, 170))
square.fill('Blue')

myfont = pygame.font.Font('fonts/Bungee-Regular.ttf', 40)
text_surface = myfont.render('hello!', True, 'Green')

player = pygame.image.load('images/icon.png')

running = True
while running:

    pygame.draw.circle(square, 'Red', (10, 7), 5)
    screen.blit(square, (10, 0))
    screen.blit(text_surface, (300, 100))
    screen.blit(player, (100, 50))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


