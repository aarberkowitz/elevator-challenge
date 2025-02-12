from config import *
from Elevator import *

"""
An elevator call control will be displayed on each floor, 
with the floor number written on it. Pressing the button will
order an elevator to the floor (even if no elevator is currently available).
When an elevator is ordered to a floor, a descending number
will be displayed next to the elevator button, 
representing the number of seconds remaining until the elevator arrives.

Each floor will be displayed with a brick background. A black bar 7 pixels
thick will be displayed between every two floors, which will be calculated as part 
of the height of the floor below it.

When clicked, the elevator call control text must become green,
and returned to its normal color when the elevator arrives at the floor.
"""


def draw_border(screen, top_left_pixel, space_color):
    x, y = top_left_pixel
    pygame.draw.rect(screen, space_color, pygame.Rect(x, y, FLOOR_LENGTH, BORDER_PIXEL_WIDTH))


class Floor:
    def __init__(self, level=0):
        self.level = level
        self.awaitingElevator = False  # are we in some elevator's queue?  Becomes True when button is clicked

    def draw_button(self, screen, level, center):
        pygame.draw.circle(screen, GRAY, center, BUTTON_RADIUS)
        # in the middle of the circle put the number (self.level) of the floor

    def draw(self, screen, image, space_color=BLACK):
        # calc x and y...
        # use some pygame function and the screen to draw...
        bottomFloorHeight = screen.get_height() - FLOOR_HEIGHT - MARGIN
        topLeftPixel = (MARGIN, bottomFloorHeight - (self.level * FLOOR_HEIGHT))
        screen.blit(image, topLeftPixel)
        # draw the border between floors overlaid on the top of the floor
        draw_border(screen, topLeftPixel, space_color)
        # now do the button
        x, y = topLeftPixel
        buttonCenterPixel = ((x + FLOOR_LENGTH) // 2, y + (FLOOR_HEIGHT + BORDER_PIXEL_WIDTH) // 2)
        self.draw_button(screen, self.level, buttonCenterPixel)

    def callElevator(self, level):
        # When button is pressed, enter floor into the queue of the elevator which will arrive fastest
        pass

    # def displayTimer(self, parameters?):
    #     #after our elevator is called, a timer is initialized next to the call elevator
    #     #button displaying how much time until our elevator arrives on our chosen floor.
    #     #will need to call on Elevator.calculateArrivalTime()
    #     pass
