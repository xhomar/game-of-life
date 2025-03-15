import numpy as np
import file


class GameOfLife:
    def __init__(self):
        self.array = np.array([])
        self.array_copy = np.array([])
        self.array_check = np.array([])
        self.array_swap = True
        self.array_width, self.array_height = (0, 0)

    def create_array(self, width, height):
        self.array = np.array([[False for _ in range(0, width)] for _ in range(0, height)])
        self.array_copy = np.array([[False for _ in range(0, width)] for _ in range(0, height)])
        self.array_check = np.array([[0 for _ in range(0, width)] for _ in range(0, height)])
        self.array_width, self.array_height = (len(self.array[0]), len(self.array))

    def swap_array(self, position, button):
        if position is None:
            return None
        width, height = position

        if self.array_swap:
            if self.array[height][width]:
                self.array[height][width] = False
            else:
                self.array[height][width] = True
        else:
            if button == 3:
                self.array[height][width] = False
            elif button == 1:
                self.array[height][width] = True

    def copy_array(self):
        for i in range(0, self.array_height):
            for j in range(0, self.array_width):
                self.array_copy[i][j] = self.array[i][j]
        try:
            file.save_array(self.array_copy)
        except:
            pass

    def paste_array(self):
        try:
            self.array_copy = file.load_array()
        except:
            pass

        for i in range(0, self.array_height):
            for j in range(0, self.array_width):
                self.array[i][j] = self.array_copy[i][j]

    def empty_array(self):
        for i in range(0, self.array_height):
            for j in range(0, self.array_width):
                self.array[i][j] = False

    def calculate_array(self):
        self.array_check = np.array([[0 for _ in range(0, self.array_width)] for _ in range(0, self.array_height)])

        for i in range(0, self.array_height):
            for j in range(0, self.array_width):
                if not self.array[i][j]:
                    continue
                for i2 in range(-1, 2):
                    for j2 in range(-1, 2):
                        if i2 == 0 and j2 == 0:
                            continue
                        if i + i2 < 0 or i + i2 > self.array_height or j + j2 < 0 or j + j2 > self.array_width:
                            continue
                        try:
                            if self.array[i + i2][j + j2]:
                                self.array_check[i][j] += 1
                            else:
                                self.array_check[i + i2][j + j2] += 1
                        except IndexError:
                            continue

        for i in range(0, self.array_height):
            for j in range(0, self.array_width):
                if self.array[i][j]:
                    if self.array_check[i][j] < 2 or self.array_check[i][j] > 3:
                        self.array[i][j] = False
                elif self.array_check[i][j] == 3:
                    self.array[i][j] = True

    def print_array(self):
        print(self.array)
