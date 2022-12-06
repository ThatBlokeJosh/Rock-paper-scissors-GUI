import pygame
from sys import exit
pygame.font.init()
from game import game, returncomputer
from image import icon, paper, rock, scissors, dark_mode_f, light_mode_f, versus, versus_light
list = []
with open("./conf.txt", "r") as f:
    content = f.read()
    for i in content.splitlines():
        list.append(i)

width, height = int(list[0]), int(list[1])

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("")
image_width, image_height = 200, 200
gap = 500
#paper_image = pygame.transform.rotate(paper_image, 90)
paper_image = paper(image_width, image_height)
paperx = width//2
paper = paper_image.get_rect(center=(paperx, height//2 - image_height//2))

rock_image = rock(image_width, image_height)
rock = rock_image.get_rect(center=(0 + gap, height//2 - image_height//2))

scissors_image = scissors(image_width, image_height)
scissors = scissors_image.get_rect(center=(width - gap, height//2 - image_height//2))

versus_image = versus(image_width, image_height)
versus_image_light = versus_light(image_width, image_height)

mode_width, mode_height = 100, 100
dark_mode_image = dark_mode_f(mode_width, mode_height)
light_mode_image = light_mode_f(mode_width, mode_height)
dark_mode = dark_mode_image.get_rect(center=(width - mode_width//1.5, height - mode_height))
light_mode = light_mode_image.get_rect(center=(width - mode_width//1.5, height - mode_height))

white = (228,229,241)
dark = (37,39,60)
black = (0,0,0)


timer_event = pygame.USEREVENT+1

icon()

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

def mode(modestr):
    if modestr == "dark":
        win.fill(dark)
        win.blit(dark_mode_image, dark_mode)
    elif modestr == "light":
        win.fill(white)
        win.blit(light_mode_image, light_mode)

def result_screen(choice):
    mode(modestr)
    if choice_ == "rock":
        win.blit(rock_image, rock)
    elif choice_ == "paper":
        win.blit(paper_image, rock)
    elif choice_ == "scissors":
        win.blit(scissors_image, rock)
    if modestr == "dark":
        win.blit(versus_image, paper)
    else:
        win.blit(versus_image_light, paper)
    computer = returncomputer()
    if computer == "rock":
        win.blit(rock_image, scissors)
    elif computer == "paper":
        win.blit(paper_image, scissors)
    elif computer == "scissors":
        win.blit(scissors_image, scissors)

    

clock = pygame.time.Clock()
modestr = "dark"
result = ""
choice_ = ""
screen = "main"
wins = 0
losses = 0

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
        if event.type == pygame.MOUSEBUTTONDOWN and screen == "main":
            if event.button == 1:
                if paper.collidepoint(event.pos):
                    result = game("paper")
                    choice_ = "paper"
                    screen = "result"
                elif rock.collidepoint(event.pos):
                    result = game("rock")
                    choice_ = "rock"
                    screen = "result"
                elif scissors.collidepoint(event.pos):
                    result = game("scissors")
                    choice_ = "scissors"
                    screen = "result"
                elif light_mode.collidepoint(event.pos) and modestr == "light":
                    modestr = "dark"
                elif dark_mode.collidepoint(event.pos):
                    modestr = "light"
        if event.type == timer_event and screen == "result":
            print(result)
            if result == "win":
                wins += 1
            elif result == "lose":
                losses += 1
            screen = "main"
            result = ""
            pygame.time.set_timer(timer_event, 0)

        if screen == "main":            
                mode(modestr)
                draw()
        elif screen == "result":
            result_screen(result)
            pygame.time.set_timer(timer_event, 1000)

    clock.tick(60)
    pygame.display.update()