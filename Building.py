from config import *
from Elevator import *
from Floor import *
"""
After running the code, the user will see the building that
includes the floors, elevators, and elevator controls.
"""
#getting our object assets
elevator_image = pygame.image.load(ELEVATOR_IMG_PATH)
floor_image = pygame.image.load(FLOOR_IMG_PATH)


#PLACEHOLDER needs to be replaced with whatever should go in self for respective class


class Building:
    def __init__(self, floors=TOTAL_FLOORS, elevators=NUMBER_OF_ELEVATORS):
        self.floors = [Floor(i) for i in range(floors)] #how many floors
        self.elevators = [Elevator(i) for i in range(elevators)] #how many elevators
        self.elevatorTimes = [0] * elevators  #keeps track of elevator busy times

#maybe the call button should be initialized in a function here instead of in floor.py?

    def draw(self, screen):
        floor_img = pygame.image.load(FLOOR_IMG_PATH)
        floor_image_scaled = pygame.transform.scale(floor_img, (FLOOR_LENGTH, FLOOR_HEIGHT))
        elevator_img = pygame.image.load(ELEVATOR_IMG_PATH)
        elevator_image_scaled = pygame.transform.scale(elevator_img, (ELEVATOR_LENGTH, ELEVATOR_HEIGHT))
        #sets up the floors, stacking one on top of the other
        for floor in self.floors[:-1]:
            floor.draw(screen, floor_image_scaled)
        self.floors[-1].draw(screen, floor_image_scaled, WHITE)
        for elevator in self.elevators:
            elevator.draw(screen, elevator_image_scaled)


    def initializeCallButton(self, current_floor):
        #for every floor in our building, there will be a button to press to call the elevator to that floor.
        #This function initializes that button.  Maybe this should go in our building class?  Not sure
        # for floor in self.floors:
        pass

    def update_position(self):
        pass

    def addToElevatorQueue(self, elevator, min_time, floor_level):
        Elevator.update_time_when_free(elevator, min_time)
        Elevator.append_to_queue(elevator, floor_level)


    def callElevator(self, floor_level):
        # when we click on the button in our app window our elevator is added to our queue.  The elevator that will
        # take the least time to get to our called floor is chosen and will go to this floor when done with its FIFO activity.
        # (needs to be done with pygame, perhaps this function will only be called in main.py?)
        min_time = pygame.time.get_ticks() + 99999
        elevator_index = -1
        for elevator in self.elevators:
            if elevator.calculateArrivalTime(floor_level) < min_time:
                min_time = elevator.calculateArrivalTime(floor_level)
                elevator_index = elevator
        self.elevatorTimes[elevator_index] = min_time
        return self.addToElevatorQueue(elevator_index, min_time, floor_level)



    def elevatorOperates(self, elevator):
        #Removes the floor at the head of the queue and moves to it.
        #Once we have arrived, ding the elevator once, delay, and move to the next floor
        #if there is one in the queue.
        while Elevator.activeQueue:
            destination = elevator.activeQueue.pop()
            while destination != elevator.currentFloor:
                elevator.elevatorMovement()
                time.sleep(ELEVATOR_MOVEMENT_SPEED/2)
            elevator.arrivedAtFloor()