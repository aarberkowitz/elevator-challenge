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
    def __init__(self, number=None):
        self.number = number
        self.currentFloor = 0 #what floor am I on?  updates on every floor
        self.destinedFloor = None #what floor am i travelling to?
        self.activeQueue = [] #array of floors I am set to travel to next
        self.direction = None #am i moving up or down?
        self.inUse = False
        self.y = None #Current Y coordinate for the elevator
        self.timeWhenFree = 0 #what game tick will elevator be free?  Pass along to call elevator function

    def draw(self, screen, image):
        topLeftPixel = (ELEVATOR_START_X + (FLOOR_HEIGHT * self.number), screen.get_height() - MARGIN - FLOOR_HEIGHT)
        screen.blit(image, topLeftPixel)

        # calc x and y...
        # use some pygame function and the screen to draw...
        #calls on the elevator png and places it according to building directions


    def calculateArrivalTime(self, called_floor):
        #Based on our queue, movement speed, and delay,
        #when will we arrive at any given floor?
        #should return a new total time for the entire queue
        if self.activeQueue and self.inUse:
            last_current_floor = self.activeQueue[-1]
            potential_arrival_time = self.timeWhenFree + (abs((called_floor - last_current_floor)) / ELEVATOR_MOVEMENT_SPEED)
        elif not self.activeQueue and self.inUse:
            potential_arrival_time = self.timeWhenFree + (abs((called_floor - self.destinedFloor)) / ELEVATOR_MOVEMENT_SPEED)
        else:
            potential_arrival_time = self.timeWhenFree + (abs((called_floor - self.currentFloor)) / ELEVATOR_MOVEMENT_SPEED)
        return potential_arrival_time

    def update_time_when_free(self, min_time):
        self.timeWhenFree = min_time

    def append_to_queue(self, floor):
        self.activeQueue.append(floor)

#move up and down
    def elevatorMovement(self):
    #     if self.currentFloor < self.destinedFloor:
    #         self.currentFloor += 1
    #     if self.currentFloor > self.destinedFloor:
    #         self.currentFloor -= 1
        pass

    def elevatorDelay(self):
        # When the elevator arrives at a floor, it will delay for 2 seconds before
        # proceeding to the next queued floor
        time.sleep(ELEVATOR_DELAY_TIME)


    def elevatorDing(self):
        #pygame has an audio mixer module, use that
        #
        pass


    def arrivedAtFloor(self):
            self.elevatorDing()
            self.elevatorDelay()

            # maybe this part should be done by a building function instead?

            # if self.activeQueue:
            #     self.destinedFloor = self.activeQueue.pop()
            #     self.elevatorMovement()

# ron = Elevator(1)
# ron.elevatorDing()


    def calculateArrivalTime(self):
        #Based on our queue, movement speed, and delay,
        #when will we arrive at any given floor?
        #should return a new total time for the entire queue
        total_busy_time = 0
        for i in range(len(self.activeQueue)):
            next_current_floor = self.activeQueue[i+1]
            next_time_to_arrival = abs(((self.activeQueue[i] - next_current_floor) * ELEVATOR_MOVEMENT_SPEED))
            total_busy_time += next_time_to_arrival + ELEVATOR_DELAY_TIME
        self.busyTime = total_busy_time
        return self.busyTime
