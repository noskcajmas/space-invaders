# Space invaders game
#
import pygame

# Initialize the game
pygame.init()
pygame.display.set_caption('Space Invaders')
display_width=640
display_height=480
display_window=pygame.display.set_mode((display_width, display_height))

# Run the game
def run_game():
    exit_game = False;

    while not exit_game:
        # Handle events
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        exit_game = True
        # Update the screen
        pygame.display.flip()

# Run the game
run_game()
pygame.quit()
quit()
