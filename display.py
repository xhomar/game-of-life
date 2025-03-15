import pygame


class Display:
    def __init__(self, screen, array):
        # general
        self.SCREEN = screen
        self.array = array
        self.screen_fill = (0, 0, 0)

        # measurements
        self.array_width, self.array_height = (0, 0)
        self. window_width, self.window_height = (0, 0)
        self.margin_width, self.margin_height = (0, 0)
        self.scale = 100

        # renders
        self.ALIVE_CELL = pygame.image.load('assets/alive.jpg').convert()
        self.DEAD_CELL = pygame.image.load('assets/dead.jpg').convert()
        self.alive_cell_resized = self.ALIVE_CELL
        self.dead_cell_resized = self.DEAD_CELL

    def render_array(self):
        self.SCREEN.fill(self.screen_fill)
        height = self.margin_height
        for i in range(0, self.array_height):
            width = self.margin_width
            for j in range(0, self.array_width):
                if self.array[i][j]:
                    self.SCREEN.blit(self.alive_cell_resized, (width, height))
                else:
                    self.SCREEN.blit(self.dead_cell_resized, (width, height))
                width += self.scale
            height += self.scale

        pygame.display.update()

    def calculate_array(self):
        # get window's and array's sizes
        self.window_width, self.window_height = pygame.display.get_window_size()
        self.array_width, self.array_height = len(self.array[0]), len(self.array)

        # getting scale (the same values)
        if self.window_width == self.array_width and self.window_height == self.array_width:
            self.scale = 1
            self.margin_width = 0
            self.margin_height = 0
            self.alive_cell_resized = self.ALIVE_CELL
            self.dead_cell_resized = self.DEAD_CELL
            return None

        # getting scale (width)
        scale = self.window_width / self.array_width
        new_array_width, new_array_height = self.array_width * scale, self.array_height * scale

        if new_array_width <= self.window_width and new_array_height <= self.window_height:
            self.scale = int(scale)
            self.margin_width = (self.window_width - (self.array_width * self.scale)) / 2
            self.margin_height = (self.window_height - (self.array_height * self.scale)) / 2
            self.alive_cell_resized = pygame.transform.scale(self.ALIVE_CELL, (self.scale, self.scale))
            self.dead_cell_resized = pygame.transform.scale(self.DEAD_CELL, (self.scale, self.scale))
            return None

        # getting scale (height)
        scale = self.window_height / self.array_height
        new_array_width, new_array_height = self.array_width * scale, self.array_height * scale

        if new_array_width <= self.window_width and new_array_height <= self.window_height:
            self.scale = int(scale)
            self.margin_width = (self.window_width - (self.array_width * self.scale)) / 2
            self.margin_height = (self.window_height - (self.array_height * self.scale)) / 2
            self.alive_cell_resized = pygame.transform.scale(self.ALIVE_CELL, (self.scale, self.scale))
            self.dead_cell_resized = pygame.transform.scale(self.DEAD_CELL, (self.scale, self.scale))
            return None

    def event_array(self, position):
        self.array_width, self.array_height = len(self.array[0]), len(self.array)
        width, height = position
        width, height = (width - self.margin_width) / self.scale, (height - self.margin_height) / self.scale

        if 0 < width < self.array_width and 0 < height < self.array_height:
            return int(width), int(height)
        else:
            return None
