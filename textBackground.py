import pygame
black = (0, 0, 0)
pygame.init()
font = pygame.font.Font( "freesansbold.ttf", 40 )
done = False
size = length, width = 800, 600
screen = pygame.display.set_mode( (size) )
loserText = font.render( "GAME OVER", True, black )
loserTextRect = loserText.get_rect()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        screen.fill( (139, 0, 0) )
        screen.blit(loserText, (270, 220))

        pygame.display.flip()


pygame.quit()