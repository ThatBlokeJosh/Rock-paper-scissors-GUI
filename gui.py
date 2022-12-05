import pygame, os
from sys import exit
pygame.font.init()

width, height = 1920, 1080

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("")

icon = pygame.transform.scale(pygame.image.load(
    os.path.join('gui/Assets', 'icon.png')), (2000, 2000)).convert_alpha()
background = pygame.transform.scale(pygame.image.load(
    os.path.join('gui/Assets', 'background.png')), (width, height)).convert_alpha()
image_width, image_height = 200, 200
gap = 500
paper_image = pygame.transform.scale(pygame.image.load(
    os.path.join('gui/Assets', 'paper_image.png')), (image_width, image_height)).convert_alpha()
paper = paper_image.get_rect(center=(width//2, height//2 - image_height//2))
rock_image = pygame.transform.scale(pygame.image.load(
    os.path.join('gui/Assets', 'rock_image.png')), (image_width, image_height)).convert_alpha()
rock = rock_image.get_rect(center=(0 + gap, height//2 - image_height//2))
scissors_image = image = pygame.transform.scale(pygame.image.load(
    os.path.join('gui/Assets', 'scissors_image.png')), (image_width, image_height)).convert_alpha()
scissors = scissors_image.get_rect(center=(width - gap, height//2 - image_height//2))
dark_mode_image = pygame.transform.scale(pygame.image.load(
    os.path.join('gui/Assets', 'moon.png')), (image_width, image_height)).convert_alpha()
light_mode_image = pygame.transform.scale(pygame.image.load(
    os.path.join('gui/Assets', 'sun.png')), (image_width, image_height)).convert_alpha()
dark_mode = dark_mode_image.get_rect(center=(width - image_width, height - image_height))
light_mode = light_mode_image.get_rect(center=(width - image_width, height - image_height))

white = (255,255,255)
dark = (33,33,33)
black = (0,0,0)

pygame.display.set_icon(icon)

run = True

class Font:
    def __init__(self, name, color, size, message, location) -> None:
        self.name = name
        self.color = color
        self.size = size
        self.message = message
        self.location = location
    def render(self):
        self.font = pygame.font.SysFont(self.name, self.size)
        self.render_name = self.font.render(self.message, True, self.color)
        win.blit(self.render_name, self.location)

def draw():
    win.blit(paper_image, paper)
    win.blit(rock_image,rock)
    win.blit(scissors_image, scissors)
    f1_size = 150
    f1 = Font(None, black, f1_size, "GAME",(width//2 - f1_size, 0))
    f1.render()
    pygame.display.update()

def mode(modestr):
    if modestr == "dark":
        win.fill(dark)
        win.blit(dark_mode_image, dark_mode)
    elif modestr == "light":
        win.fill(white)
        win.blit(light_mode_image, light_mode)
    draw()

clock = pygame.time.Clock()
modestr = "light"
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                pygame.quit()
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if paper.collidepoint(event.pos):
                    print("paper")
                elif rock.collidepoint(event.pos):
                    print("rock")
                elif scissors.collidepoint(event.pos):
                    print("scissors")
                elif light_mode.collidepoint(event.pos):
                    modestr = "dark"
                elif dark_mode.collidepoint(event.pos):
                    modestr = "light"
    mode(modestr)
    clock.tick(60)