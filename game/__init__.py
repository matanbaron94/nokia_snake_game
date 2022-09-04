import pygame
import time
import random




################ Setup surface & game #######################




pygame.init()

# Setup colors
white = (255, 255, 255)
black = (112, 96, 0)
red = (255, 0, 0)
blue = (66, 135, 245)
green = (149,159,0)


# Surface size
window_width = 600
window_height = 630

frame_width = 594
frame_height = 593







# Fonts setup
h3 = pygame.font.SysFont("ariel", 25)
h1 = pygame.font.SysFont("ariel", 80)
h4 = pygame.font.SysFont("ariel", 20)


# Setup window
display = pygame.display.set_mode((window_width, window_height))
display.fill(green)

# Window title
pygame.display.set_caption('Nokia Snake Game by Matan Baron')

# Stages
game_over = False
stop = False
exit = False
welcome_s = True

score = 0

# Setup snake
head_x = window_width / 2
head_y = (window_height / 2) -5
snake_block = 10
speed = 0.1
snake_size = 10

apple_x = (random.randint(1, 58) * 10)
apple_y = (random.randint(1, 58) * 10)

x_change = 0
y_change = 0

snake_list = []


# Ganerate game frame
def frame():
    #
    for i in range(5, 594):
        pygame.draw.rect(display, black, [5, i, 3, 3])
        pygame.draw.rect(display, black, [593, i, 3, 3])
        pygame.draw.rect(display, black, [i, 5, 3, 3])
        pygame.draw.rect(display, black, [i, 593, 3, 3])


# Display welcome view
def welcome():
    display.fill(green)
    score = 0
    # Print welcome messages
    display.blit(h1.render("NOKIA", True, black), [400 / 2, 250])
    display.blit(h4.render("Tap Space to start", True, black), [230, 320])
    display.blit(h4.render("Made by Matan Baron", True, black), [225, 570])

    frame()

    pygame.display.update()


# Pause Stage
def puse():


    display.fill(green)


    # Print Puse messages
    display.blit(h1.render("Pause", True, black), [212, 200])
    display.blit(h4.render("Tap Space to continue", True, black), [230, 260])
    display.blit(h4.render("Tap Esc to exit", True, black), [248, 280])
    value = h3.render(f"loction = ({head_x},{head_y}), score = {score}, apple = {apple_x, apple_y}", True, black)
    display.blit(value, [10, 600])

    frame()

    pygame.display.update()


def ggame_over():
    display.fill(green)

    # Print Game over messages
    display.blit(h1.render("GAME OVER", True, black), [135, 200])
    display.blit(h4.render("Tap Space to restart", True, black), [235, 260])
    display.blit(h4.render("Tap Esc to exit", True, black), [248, 280])
    # display.blit(h3.render(f"Your score: {score}", True, black), [250, 350])


    frame()

    pygame.display.update()


