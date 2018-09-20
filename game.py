# # Space invaders game
import pygame
pygame.init()

pygame.display.set_caption('Space Invaders')
screen = pygame.display.set_mode((900, 600))
img = pygame.image.load("Sprites/invader-1.png")
x = 425
y = 520
speed = 8
fire_shot_x = 0
fire_shot_y = -1
fire_shot_speed = 10
is_shootable = True

white = (255, 255, 255)

# Shoot ball
def fire_shot(shoot_x, shoot_y):
    thickness = 7
    pygame.draw.circle(screen, white, (shoot_x, shoot_y), thickness)

running = True
while running:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if pygame.event == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fire_shot_x = x + 10
                    fire_shot_y = y

    if is_shootable:
        fire_shot(fire_shot_x, fire_shot_y)
        fire_shot_y -= fire_shot_speed
        print(fire_shot_y)
        pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 900 - 72:
        x += speed

    screen.fill((0,0,0))
    screen.blit(img,(x, y))
    pygame.display.update()

pygame.quit()
