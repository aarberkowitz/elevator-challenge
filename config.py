import pygame
import time

#Pygame set up
#RGB Tuples
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
GRAY = (128, 128, 128)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

#Building Set up
TOTAL_FLOORS = 10
NUMBER_OF_ELEVATORS = 3
ELEVATOR_IMG_PATH = 'assets/elv.png'
FLOOR_IMG_PATH = 'assets/brick.png'
ELEVATOR_DING_PATH = 'assets/ding.mp3'

#Floor Constants
MARGIN = 5
FLOOR_LENGTH = 120 #120 pixels
FLOOR_HEIGHT = 60 #60 pixels
BORDER_PIXEL_WIDTH = 7 #border should be 7 pixels across

BUTTON_RADIUS = 15


#Elevator Constants/variables
ELEVATOR_LENGTH = 50
ELEVATOR_HEIGHT = 50
ELEVATOR_SPACE = 15
ELEVATOR_START_X = MARGIN + FLOOR_LENGTH + ELEVATOR_SPACE

ELEVATOR_MOVEMENT_SPEED = 100 #Elevator needs to move at 2 floors per second (minus borders), so 100 pixels
ELEVATOR_DELAY_TIME = 2
TOTAL_ARRIVAL_TIME = 0
CURRENT_TICK = pygame.time.get_ticks()
