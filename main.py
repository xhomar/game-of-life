import sys
from gameoflife import *
from display import *
import file

pygame.init()

file.check_files()
width, height, array_width, array_height, framerate, array_swap = file.read_config()

pygame.display.set_caption("Game Of Life")
pygame.display.set_icon(pygame.image.load('assets/alive.jpg'))
SCREEN = pygame.display.set_mode((width, height), pygame.RESIZABLE)
CLOCK = pygame.Clock()
pause = True

gameoflife = GameOfLife()
gameoflife.create_array(array_width, array_height)
gameoflife.array_swap = array_swap

display = Display(SCREEN, gameoflife.array)
display.screen_fill = (10, 10, 10)


while True:
    for event in pygame.event.get():
        # exit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # place/remove cell
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 or event.button == 3:
                gameoflife.swap_array(display.event_array(pygame.mouse.get_pos()), event.button)
                display.render_array()
        if event.type == pygame.KEYDOWN:
            # pause
            if event.key == pygame.K_SPACE:
                if pause:
                    pause = False
                else:
                    pause = True
            # copy/paste
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RCTRL] or keys[pygame.K_LCTRL]:
                if keys[pygame.K_c] or keys[pygame.K_s]:
                    gameoflife.copy_array()
                if keys[pygame.K_v]:
                    gameoflife.paste_array()
                    display.render_array()
                if keys[pygame.K_e]:
                    gameoflife.empty_array()
                    display.render_array()
                if keys[pygame.K_r]:
                    gameoflife.random_array()
                    display.render_array()
    if pygame.display.get_window_size() != (display.window_width, display.window_height):
        display.calculate_array()
        display.render_array()
    if not pause:
        gameoflife.calculate_array()
        display.render_array()
    CLOCK.tick(framerate)
