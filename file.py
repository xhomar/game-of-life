def check_files():
    try:
        open("config/config.txt", "x")
        file = open("config/config.txt", "w")
        # width, height, array width, array height, framerate, array swap
        file.write("1280\n720\n64\n32\n10\nTrue")
    except FileExistsError:
        pass

    try:
        open("config/save.txt", "x")
    except FileExistsError:
        pass


def read_config():
    try:
        file = open("config/config.txt", "r")
        width = int(file.readline())
        height = int(file.readline())
        array_width = int(file.readline())
        array_height = int(file.readline())
        framerate = int(file.readline())
        array_swap = bool(int(file.readline()))
    except ValueError:
        file = open("config/config.txt", "w")
        file.write("1280\n720\n64\n32\n10\nTrue")
        file = open("config/config.txt", "r")
        width = int(file.readline())
        height = int(file.readline())
        array_width = int(file.readline())
        array_height = int(file.readline())
        framerate = int(file.readline())
        array_swap = bool(int(file.readline()))
    return width, height, array_width, array_height, framerate, array_swap


def save_array(array):
    file = open("config/save.txt", "w")
    file.write("")
    file = open("config/save.txt", "a")
    file.write(f"{len(array[0])}\n{len(array)}\n")
    for i in range(0, len(array)):
        for j in range(0, len(array[0])):
            if array[i][j]:
                file.write("1")
            else:
                file.write("0")
        file.write("\n")


def load_array():
    array = []
    file = open("config/save.txt", "r")
    width = int(file.readline())
    height = int(file.readline())
    for i in range(0, height):
        row_read = file.readline()
        row_array = []
        for j in range(0, width):
            if int(row_read[j]) == 0:
                row_array.append(False)
            else:
                row_array.append(True)
        array.append(row_array)
    return array
