import pygame.time

from config import *
from Building import *

"""

After running the code, the user will see the building that includes
the floors, elevators, and elevator controls.

The number of floors and the number of elevators in the building must
be easily defined/changed (by changing settings in the code or a configuration file).

Utilize pygame library to build our world, screen, and capture events within the world
to send to functions within our different classes.
"""

# Define the dimensions of screen object(width,height)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# details for our game window
pygame.display.set_caption('Elevator Challenge')
screen.fill(WHITE)

# setting framerate and game clock
clock = pygame.time.Clock()
pygame.time.Clock.tick(clock, 60)

# Update the display using flip
building = Building(TOTAL_FLOORS, NUMBER_OF_ELEVATORS)

building.draw(screen)

pygame.display.flip()

# at some point...


# # maybe some more stuff...
#
building.draw(screen)

# Variable to keep our game loop running
running = True

# game loop
while running:

    # for loop through the event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False
        # Check for mouse clicking on floor buttons
        if event.type == pygame.mouse.get_pressed():
            ## if mouse is pressed get position of cursor ##
            pos = pygame.mouse.get_pos()
            ## check if cursor is on button ##
            # if button.collidepoint(pos):
            #     here call elevator add to queue
            # return
