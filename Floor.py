from config import *

class Floor:
    def __init__(self, level, image):
        self.image = image
        self.level = level
        self.top_left = None
        self.button_center = None
        self.awaiting_elevator = False  # are we in some elevator's queue?  Becomes True when button is clicked

    def draw_button(self, canvas, center):
        font_color = BLACK if not self.awaiting_elevator else GREEN
        pygame.draw.circle(canvas, GRAY, center, BUTTON_RADIUS)
        pygame.draw.circle(canvas, font_color, center, BUTTON_RADIUS, width=2)

        number = str(self.level) if self.level > 0 else "G"
        font = pygame.font.Font(None, FONT_SIZE)
        text_surface = font.render(number, True, font_color)
        text_surface_rect = text_surface.get_rect(center=center)
        canvas.blit(text_surface, text_surface_rect)

    def draw(self, canvas):
        x, base_y = MARGIN, canvas.get_height() - FLOOR_HEIGHT - MARGIN
        y = base_y - self.level * FLOOR_HEIGHT
        self.top_left = x, y
        canvas.blit(self.image, (x, y))
        button_draw_center = x + FLOOR_LENGTH // 2, y + (FLOOR_HEIGHT + BORDER_PIXEL_WIDTH) // 2
        self.button_center = x + FLOOR_LENGTH // 2, y + (FLOOR_HEIGHT + BORDER_PIXEL_WIDTH) // 2 #y - canvas.get_height() + SCREEN_HEIGHT
        self.draw_button(canvas, button_draw_center)


    def button_was_pressed(self, x, y):
        cx, cy = self.button_center
        if ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5 <= BUTTON_RADIUS:
            return self.level