import pygame, os

# ICON
def icon():
    icon = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'icon.png')), (2000, 2000)).convert_alpha()
    pygame.display.set_icon(icon)

# PAPER
def paper(image_width, image_height):
    paper_image = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'paper_image.png')), (image_width, image_height)).convert_alpha()
    return paper_image

# ROCK
def rock(image_width, image_height):
    rock_image = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'rock_image.png')), (image_width, image_height)).convert_alpha()
    return rock_image

# SCISSORS
def scissors(image_width, image_height):
    scissors_image = image = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'scissors_image.png')), (image_width, image_height)).convert_alpha()
    return scissors_image

# DARK MODE
def dark_mode_f(mode_width, mode_height):
    dark_mode_image = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'moon.png')), (mode_width, mode_height)).convert_alpha()
    return dark_mode_image

# LIGHT MODE
def light_mode_f(mode_width, mode_height):
    light_mode_image = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'sun.png')), (mode_width, mode_height)).convert_alpha()
    return light_mode_image

# VERSUS
def versus(image_width, image_height):
    versus_image = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'vs.png')), (image_width, image_height)).convert_alpha()
    return versus_image
# VERSUS LIGHT
def versus_light(image_width, image_height):
    versus_image = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'vslight.png')), (image_width, image_height)).convert_alpha()
    return versus_image
# WIN
def win_i(image_width, image_height):
    win_image = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'win.png')), (image_width, image_height)).convert_alpha()
    return win_image
# WIN LIGHT
def win_light(image_width, image_height):
    win_image = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'winlight.png')), (image_width, image_height)).convert_alpha()
    return win_image
# LOSE
def lose(image_width, image_height):
    lose_image = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'lose.png')), (image_width, image_height)).convert_alpha()
    return lose_image
# LOSE LIGHT
def lose_light(image_width, image_height):
    lose_image = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'loselight.png')), (image_width, image_height)).convert_alpha()
    return lose_image