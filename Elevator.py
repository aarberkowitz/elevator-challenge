"""
When an elevator is ordered to a floor, a descending timer
will initialize next to the elevator button, displaying
the number of seconds remaining until the elevator arrives.

The elevator algorithm must result in the minimal
waiting time for the elevator without extending the waiting
times of those who have already ordered an elevator.

The elevator will be represented using a given image (elv.png file).
When an elevator arrives at a floor, a given sound (ding.mp3 file) must be played.
"""

from config import *


class Elevator:
    def __init__(self, number, image, initial_y_pos, call_back_function):
        self.building_call_back_function = call_back_function
        self.image = image
        self.number = number
        self.destined_floor = 0  # what floor am i travelling to?
        self.active_q = []  # array of floors I am set to travel to next
        self.q_pop = False
        self.direction = None  # am i moving up or down?
        self.destination_y = initial_y_pos  # updates to Y coordinate of floor we are going to now
        self.y = initial_y_pos  # Current Y coordinate for the elevator
        self.time_when_free = 0.0  # what game tick will elevator be free?  Pass along to call elevator function
        self.position_when_free = 0
        self.delay_start_time = None
        self.delaying = False  # Flag for delay status
        self.busy = False
        self.at_delay = False

    def draw(self, canvas):
        top_left = (ELEVATOR_START_X + (ELEVATOR_LENGTH + MARGIN) * self.number, self.y)
        canvas.blit(self.image, top_left)

    def calculate_arrival_time(self, called_floor):
        trip_time = abs(called_floor - self.position_when_free) / SINGLE_FLOOR_TRAVEL_TIME
        return self.time_when_free + trip_time

    def append_to_queue(self, floor, y, arrival_time):
        self.active_q.append((floor, y))
        self.position_when_free = floor
        self.time_when_free = arrival_time

    def get_next_task(self):
        if self.active_q:
            self.destined_floor, self.destination_y = self.active_q.pop(0)
            self.destination_y += BORDER_PIXEL_WIDTH
            self.busy = True

    # move up and down
    def update(self):
        self.time_when_free = max(self.time_when_free, pygame.time.get_ticks())
        if self.busy:
            if self.y != self.destination_y:
                direction = 1 if self.y <= self.destination_y else -1
                # Prevent overshooting the destination floor
                movement_step = direction * min(ELEVATOR_MOVEMENT_SPEED, abs(self.destination_y - self.y))
                self.y += movement_step
            else:
                self.arrived_at_floor()
        elif self.at_delay:
            current_time = pygame.time.get_ticks()
            elapsed_time = (current_time - self.delay_start_time) / 1000
            if elapsed_time >= 2:
                self.at_delay = False
        else:
            self.get_next_task()

    def arrived_at_floor(self):
        pygame.mixer.music.play()  # Play the ding sound when the elevator arrives
        self.building_call_back_function(self.destined_floor)
        self.busy = False
        self.at_delay = True
        self.delay_start_time = pygame.time.get_ticks()
