# # Space invaders game
import pygame
pygame.init()

pygame.display.set_caption('Space Invaders')
screen = pygame.display.set_mode((1024, 768))
img = pygame.image.load("Sprites/invader-1.png")
x = 496
y = 672
speed = 8

running = True
while running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if pygame.event == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 1024 - 72:
        x += speed

    screen.fill((0,0,0))
    screen.blit(img,(x, y))
    pygame.display.update()

pygame.quit()
