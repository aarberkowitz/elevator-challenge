import pygame

from config import *
from Elevator import *
from Floor import *

"""
After running the code, the user will see the building that
includes the floors, elevators, and elevator controls.
"""


def set_up_images():
    elevator_image = pygame.transform.scale(pygame.image.load(ELEVATOR_IMG_PATH), ELEVATOR_SIZE)
    floor_image = pygame.image.load(FLOOR_IMG_PATH)
    floor_image = floor_image.subsurface(pygame.Rect(0, 0, FLOOR_LENGTH * 2, FLOOR_HEIGHT * 2))
    scaled_floor_image = pygame.transform.scale(floor_image, (FLOOR_LENGTH, FLOOR_HEIGHT))
    top_floor_image = scaled_floor_image.copy()
    pygame.draw.rect(scaled_floor_image, BLACK, pygame.Rect(0, 0, FLOOR_LENGTH, BORDER_PIXEL_WIDTH))
    pygame.draw.rect(top_floor_image, WHITE, pygame.Rect(0, 0, FLOOR_LENGTH, BORDER_PIXEL_WIDTH))
    return elevator_image, scaled_floor_image, top_floor_image


class Building:
    def __init__(self, floors, elevators, canvas):
        elevator_image, scaled_floor_image, top_floor_image = set_up_images()
        elevator_initial_y = canvas.get_height() - MARGIN - ELEVATOR_HEIGHT
        self.floors = [Floor(i, scaled_floor_image) for i in range(floors - 1)]
        self.floors.append(Floor(floors - 1, top_floor_image))
        self.elevators = [Elevator(i, elevator_image, elevator_initial_y, self.elevator_arrived_at) for i in
                          range(elevators)]  # how many elevators
        self.last_update_time = 0

    def elevator_arrived_at(self, level):
        self.floors[level].awaiting_elevator = False
        # self.floors[level]

    def draw(self, canvas):
        for floor in self.floors:
            floor.draw(canvas)
        for elevator in self.elevators:
            elevator.draw(canvas)

    def check_calls(self, pos):
        print("checking calls...")
        x, y = pos
        for floor in self.floors:
            level = floor.button_was_pressed(x, y)
            if level is not None:
                self.call_elevator(level)

    def update(self, canvas):
        for elevator in self.elevators:
            elevator.update()

            # when button will turn green we will need to draw the floor here too

    def call_elevator(self, floor_level):
        # when we click on the button in our app window our elevator is added to our queue.  The elevator that will
        # take the least time to get to our called floor is chosen and will go to this floor when done with its FIFO activity.
        # (needs to be done with pygame, perhaps this function will only be called in main.py?)
        called_floor = self.floors[floor_level]

        if called_floor.awaiting_elevator:
            return

        best_arrival_time = float("inf")
        best_elevator = self.elevators[0]

        for elevator in self.elevators:

            arrival_time = elevator.calculate_arrival_time(floor_level)

            if arrival_time < best_arrival_time:
                best_arrival_time = arrival_time
                best_elevator = elevator

        _, dest_y = called_floor.top_left
        called_floor.awaiting_elevator = True

        best_elevator.append_to_queue(floor_level, dest_y, best_arrival_time + ELEVATOR_DELAY_TIME)
