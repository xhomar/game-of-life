import pygame


class Display:
    def __init__(self, screen, array):
        # general
        self.SCREEN = screen
        self.array = array
        self.screen_fill = (0, 0, 0)

        # measurements
        self.array_width, self.array_height = len(self.array[0]), len(self.array)
        self.window_width, self.window_height = (0, 0)
        self.margin_width, self.margin_height = (0, 0)
        self.scale = 1

        # array display
        self.ARRAY_DISPLAY = pygame.Surface((self.array_width, self.array_height))
        self.array_display_resized = None

        # renders
        self.ALIVE_CELL = pygame.image.load('assets/alive.jpg').convert()

    def render_array(self):
        self.ARRAY_DISPLAY.fill((0, 0, 0))
        height = 0
        for i in range(0, self.array_height):
            width = 0
            for j in range(0, self.array_width):
                if self.array[i][j]:
                    self.ARRAY_DISPLAY.blit(self.ALIVE_CELL, (width, height))
                width += 1
            height += 1
        self.array_display_resized = pygame.transform.scale(self.ARRAY_DISPLAY, (self.array_width * self.scale, self.array_height * self.scale))
        self.SCREEN.fill(self.screen_fill)
        self.SCREEN.blit(self.array_display_resized, (self.margin_width, self.margin_height))
        pygame.display.update()

    def calculate_array(self):
        # get window's and array's sizes
        self.window_width, self.window_height = pygame.display.get_window_size()

        # getting scale (the same values)
        if self.window_width == self.array_width and self.window_height == self.array_width:
            self.scale = 1
            self.margin_width = 0
            self.margin_height = 0
            return None

        # getting scale (width)
        scale = self.window_width / self.array_width
        new_array_width, new_array_height = self.array_width * scale, self.array_height * scale

        if new_array_width <= self.window_width and new_array_height <= self.window_height:
            self.scale = scale
            self.margin_width = (self.window_width - (self.array_width * self.scale)) / 2
            self.margin_height = (self.window_height - (self.array_height * self.scale)) / 2
            return None

        # getting scale (height)
        scale = self.window_height / self.array_height
        new_array_width, new_array_height = self.array_width * scale, self.array_height * scale

        if new_array_width <= self.window_width and new_array_height <= self.window_height:
            self.scale = scale
            self.margin_width = (self.window_width - (self.array_width * self.scale)) / 2
            self.margin_height = (self.window_height - (self.array_height * self.scale)) / 2
            return None

    def event_array(self, position):
        self.array_width, self.array_height = len(self.array[0]), len(self.array)
        width, height = position
        width, height = (width - self.margin_width) / self.scale, (height - self.margin_height) / self.scale

        if 0 < width < self.array_width and 0 < height < self.array_height:
            return int(width), int(height)
        else:
            return None
