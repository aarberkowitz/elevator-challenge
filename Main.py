from config import *
from Building import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Elevator Challenge')

canvas_height = max(MARGIN * 2 + TOTAL_FLOORS * FLOOR_HEIGHT, SCREEN_HEIGHT)
canvas = pygame.Surface((SCREEN_WIDTH, canvas_height))
pygame.mixer.music.load(ELEVATOR_DING_PATH)

scroll_speed = 20
scroll_y = canvas_height - SCREEN_HEIGHT

building = Building(TOTAL_FLOORS, NUMBER_OF_ELEVATORS, canvas)

running = True

# game loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False
        # Check for mouse clicking on floor buttons
        if event.type == pygame.MOUSEBUTTONDOWN:
            ## if mouse is pressed get position of cursor ##
            if event.button == LEFT_MOUSE_BUTTON:
                pos = pygame.mouse.get_pos()
                print(f"mouse pressed {pos}")
                x, y = pos
                pos = x, y + scroll_y
                building.check_calls(pos)
            elif event.button == WHEEL_UP:
                scroll_y -= scroll_speed
            elif event.button == WHEEL_DOWN:
                scroll_y += scroll_speed

            # bound scroll y
            scroll_y = max(0, min(canvas_height - SCREEN_HEIGHT, scroll_y))

    clock.tick(FPS)
    canvas.fill(WHITE)
    building.draw(canvas)
    building.update(canvas)
    screen.blit(canvas, (0, -scroll_y))
    pygame.display.flip()
