import pygame, os

# ICON
def icon():
    icon = pygame.transform.scale(pygame.image.load(
    os.path.join('gui/Assets', 'icon.png')), (2000, 2000)).convert_alpha()
    pygame.display.set_icon(icon)

# PAPER
def paper(image_width, image_height):
    paper_image = pygame.transform.scale(pygame.image.load(
    os.path.join('gui/Assets', 'paper_image.png')), (image_width, image_height)).convert_alpha()
    return paper_image

# ROCK
def rock(image_width, image_height):
    rock_image = pygame.transform.scale(pygame.image.load(
    os.path.join('gui/Assets', 'rock_image.png')), (image_width, image_height)).convert_alpha()
    return rock_image

# SCISSORS
def scissors(image_width, image_height):
    scissors_image = image = pygame.transform.scale(pygame.image.load(
    os.path.join('gui/Assets', 'scissors_image.png')), (image_width, image_height)).convert_alpha()
    return scissors_image

# DARK MODE
def dark_mode_f(mode_width, mode_height):
    dark_mode_image = pygame.transform.scale(pygame.image.load(
    os.path.join('gui/Assets', 'moon.png')), (mode_width, mode_height)).convert_alpha()
    return dark_mode_image

# LIGHT MODE
def light_mode_f(mode_width, mode_height):
    light_mode_image = pygame.transform.scale(pygame.image.load(
    os.path.join('gui/Assets', 'sun.png')), (mode_width, mode_height)).convert_alpha()
    return light_mode_image

# VERSUS
def versus(image_width, image_height):
    versus_image = pygame.transform.scale(pygame.image.load(
    os.path.join('gui/Assets', 'vs.png')), (image_width, image_height)).convert_alpha()
    return versus_image
# VERSUS LIGHT
def versus_light(image_width, image_height):
    versus_image = pygame.transform.scale(pygame.image.load(
    os.path.join('gui/Assets', 'vslight.png')), (image_width, image_height)).convert_alpha()
    return versus_image