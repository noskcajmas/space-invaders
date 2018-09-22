# # Space invaders game
import pygame
pygame.init()

pygame.display.set_caption('Space Invaders')
screen = pygame.display.set_mode((1024, 768))
beam = pygame.image.load("Sprites/beam.png")

# Creates a controllable player object
class Player():
    def __init__(self, position_x, position_y, speed):
        self.position_x = position_x
        self.position_y = position_y
        self.speed = speed
        self.sprite = pygame.image.load("Sprites/player.png")
        self.shoot = False
    
    def move_left(self):
        self.position_x -= self.speed 
    
    def move_right(self):
        self.position_x += self.speed 

    def fire(self):
        return Beam(self.position_x, self.position_y)

class Beam():
    def __init__(self, position_x, position_y):
        self.position_x = position_x + 48
        self.position_y = position_y
        self.sprite = pygame.image.load("Sprites/beam.png")
    
    def move(self):
        self.position_y -= 2

class Invader():
    def _init_(self, position, speed, rank):
        self.position = position
        self.speed = speed

    def rank():
        if self.rank ==  1:
            self.sprite =  pygame.image.load("Sprites/invader-1.png")
            self.score = 10

        elif self.rank == 2:
            self.sprite =  pygame.image.load("Sprites/invader-1.png")
            self.score = 20

        elif self.rank == 3:
            self.sprite =  pygame.image.load("Sprites/invader-1.png")
            self.score = 30

player = Player(496, 672, 0.32)
beam = Beam(player.position_x, player.position_y)

running = True
shoot = False

while running:

    print(player.shoot)

    for event in pygame.event.get():
            if pygame.event == pygame.QUIT:
                running = False

    # Define list of possible keys if pressed
    keys = pygame.key.get_pressed()

    # If the left or right arrow key is pressed, move player respectively. 
    if keys[pygame.K_LEFT] and player.position_x > player.speed:
        player.move_left()
    if keys[pygame.K_RIGHT] and player.position_x <= 920:
        player.move_right()
    if keys[pygame.K_SPACE]:
        if player.shoot == False:
            beam = player.fire()
            player.shoot = True

    if player.shoot and beam.position_y >= 16:
        beam.move()    
    
    # On each cycle of the loop, need to reset background and render the player
    screen.fill((0,0,0))
    screen.blit(player.sprite,(player.position_x, player.position_y))
    screen.blit(beam.sprite,(beam.position_x, beam.position_y))
    pygame.display.update()

pygame.quit()
