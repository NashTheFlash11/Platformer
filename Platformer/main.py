import pygame
import os
from sys import exit

# This initiates all sub parts of pygame
pygame.init()

# Width and height of the window, title
# The window is a display surface
WIDTH, HEIGHT = 800, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Runner')

# Max FPS
FPS = 60

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Images and characters
# Convert the images to something pygame can work with easier. This helps make the game smoother
# convert_alpha() and convert() make the surfacces change to the same pixel format as that is being used by the screen
SKY = pygame.image.load(os.path.join('graphics', 'Sky.png')).convert()
GROUND = pygame.image.load(os.path.join('graphics', 'ground.png')).convert()
SNAIL = pygame.image.load(os.path.join('graphics', 'snail', 'snail1.png')).convert_alpha()
PLAYER = pygame.image.load(os.path.join('graphics', 'player', 'player_walk_1.png')).convert_alpha()

# FONT
# Use SysFont if you don't have a external font file
test_font = pygame.font.Font(os.path.join('font', 'Pixeltype.ttf'), 50)

# Function to draw all images and characters onto the window
def draw_window(snail, player):
    # The render function's arguments are: Text you want to display, Anti-aliasing, and color
    test_surface = test_font.render('My Game', False, BLACK)
    # Make sure to draw backgrounds at the back, and character and everything else in front
    # The WIN.blit function that draws the sky must be the first .blit() function when drawing characters, etc.
    WIN.blit(SKY, (0, 0))
    WIN.blit(GROUND, (0, 300))
    WIN.blit(test_surface, (300, 50))
    WIN.blit(SNAIL, (snail.x, snail.y))
    WIN.blit(PLAYER, (player.x, player.y))
    snail.x -= 4
    if snail.x < -100:
        snail.x = 800

   
    pygame.display.update()

def main():
    snail = pygame.Rect(600, 250, 50, 50)
    player = pygame.Rect(80, 200, 50, 50)
    # Declare clock
    clock = pygame.time.Clock()
    run = True
    while run == True:
        # Declare that the fps should max out at the value for FPS(60)
        clock.tick(FPS)
        # This for loop will try and get all events within the code, and do what it needs to do for each event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                # Exit the code so that it stops the loop immediatly
                exit()
 
        draw_window(snail, player)

# This if statements is to say that if there a file named main, it is the main file of the game
if __name__ == "__main__":
    main()