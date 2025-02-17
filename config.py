import pygame

# Pygame set up
# RGB Tuples
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
GRAY = (160, 160, 160)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# Building Set up
TOTAL_FLOORS = 50
NUMBER_OF_ELEVATORS = 3
ELEVATOR_IMG_PATH = 'assets/elv.png'
FLOOR_IMG_PATH = 'assets/brick.png'
ELEVATOR_DING_PATH = 'assets/ding.mp3'

# Floor Constants
MARGIN = 5
FLOOR_LENGTH = 120  # 120 pixels
FLOOR_HEIGHT = 60  # 60 pixels
BORDER_PIXEL_WIDTH = 7  # border should be 7 pixels across

BUTTON_RADIUS = 15

# Elevator Constants/variables
ELEVATOR_SIZE = ELEVATOR_LENGTH, ELEVATOR_HEIGHT = 50, 50
ELEVATOR_SPACE = 15
ELEVATOR_START_X = MARGIN + FLOOR_LENGTH + ELEVATOR_SPACE

SINGLE_FLOOR_TRAVEL_TIME = 0.5 # seconds per floor
FPS = 60
ELEVATOR_MOVEMENT_SPEED = FLOOR_HEIGHT * 2 // FPS #2 pixels per frame, 120 pixels, or 2 floors, per second
ELEVATOR_DELAY_TIME = 2000 # in MS

FONT_SIZE = 25

# mouse buttons:

LEFT_MOUSE_BUTTON = 1
WHEEL_UP = 4
WHEEL_DOWN = 5