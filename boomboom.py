import pygame
import random
import sys
import time

pygame.init()

done = False
clock = pygame.time.Clock()
size = length, width = 800, 600
screen = pygame.display.set_mode( (size) )
pygame.display.set_caption( "Bomb Shell Game" )

background = pygame.image.load( "pythonbackground1.jpg" )

red = (255, 0, 0)
darkRed = (255, 40, 10)
green = (0, 255, 0)
blue = (0, 0, 255)
darkBlue = (100, 100, 255)
black = (0, 0, 0,)
white = (255, 255, 255)
yellow = (169, 169, 0)
score = 0
lives = 3

speedx = 0
speedy = 0

crashSound = pygame.mixer.Sound( "pygame_Explosion.wav" )

font = pygame.font.Font( "freesansbold.ttf", 16 )
font1 = pygame.font.Font( "freesansbold.ttf", 40 )
font2 = pygame.font.Font( "freesansbold.ttf", 28 )

text = font.render( f"Score:{score}", True, black )
textRect = text.get_rect()
text1 = font.render( f"Lives:{lives}", True, black )
text1Rect = text.get_rect()

loserText = font1.render( "GAME OVER", True, black )
loserTextRect = loserText.get_rect()
scoreText = font2.render( f"Your Score was:{score}", True, black )
scoreTextRect = scoreText.get_rect()

bombX = int( random.randint( 60, width ) )
bombY = 40

shieldX = 370
shieldY = 570

shield = pygame.rect
circle = pygame.rect


def collideShield():
    global bombX, bombY, score, speedy, text
    bombX = random.randint( 60, width )
    bombY = 40
    score = score + 10
    speedy = 0
    text = font.render( f"Score:{score}", True, black )
    screen.blit( text, (710, 20) )


def collideBottom():
    global lives, bombX, bombY, speedy, text1
    lives -= 1
    bombX = random.randint( 60, width )
    bombY = 40
    speedy = 0
    text1 = font.render( f"Lives:{lives}", True, black )
    screen.blit( text1, (60, 20) )
    pygame.mixer.music.load( "pygame_Explosion.wav" )
    pygame.mixer.music.play( 1 )



def live():
    global speedy, scoreText
    speedy = 0
    screen.fill( (139, 0, 0) )
    scoreText = font2.render( f"Your Score was:{score}", True, black )
    screen.blit( loserText, (270, 220) )
    screen.blit( scoreText, (270, 300) )


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill( darkBlue )
    screen.blit( background, (0, 0) )
    screen.blit( text, (710, 20) )
    screen.blit( text1, (60, 20) )
    shield = pygame.draw.rect( screen, darkRed, (shieldX, shieldY, 100, 10) )
    circle = pygame.draw.circle( screen, yellow, (bombX, bombY), 30 )
    speedy += 0.09
    bombY += int(speedy)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            shieldX -= 8
        if event.key == pygame.K_RIGHT:
            shieldX += 8
    if shieldX <= 0:
        shieldX = 0
    elif shieldX >= 700:
        shieldX = 700
    if circle.colliderect( shield ):
        collideShield()
    if circle.bottom == 600:
        collideBottom()
    if lives == 0:
        live()

    pygame.display.flip()

    clock.tick( 60 )
pygame.quit()
