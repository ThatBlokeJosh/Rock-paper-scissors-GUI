import pygame
from sys import exit
pygame.font.init()
from game import game, returncomputer
from image import *
list = []
with open("./conf.txt", "r") as f:
    content = f.read()
    for i in content.splitlines():
        list.append(i)
if list:
    width, height = int(list[0]), int(list[1])
else:
    width, height = 1920, 1080

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("")
image_width, image_height = 200, 200
gap = 500
paper_image = paper(image_width, image_height)
paperx = width//2
paper = paper_image.get_rect(center=(paperx, height//2 - image_height//2))

rock_image = rock(image_width, image_height)
rock = rock_image.get_rect(center=(0 + gap, height//2 - image_height//2))

scissors_image = scissors(image_width, image_height)
scissors = scissors_image.get_rect(center=(width - gap, height//2 - image_height//2))

versus_image = versus(image_width, image_height)
versus_image_light = versus_light(image_width, image_height)

win_i = win_i(image_width, image_height)
win_light = win_light(image_width, image_height)

lose = lose(image_width, image_height)
lose_light = lose_light(image_width, image_height)

mode_width, mode_height = 100, 100
dark_mode_image = dark_mode_f(mode_width, mode_height)
light_mode_image = light_mode_f(mode_width, mode_height)
dark_mode = dark_mode_image.get_rect(center=(width - mode_width//1.5, height - mode_height))
light_mode = light_mode_image.get_rect(center=(width - mode_width//1.5, height - mode_height))

play_image = play(image_width, image_height)
quit_image = quit(image_width, image_height)
options_image = options(image_width, image_height)

back_image = back(image_width, image_height)
back_light_image = back_light(image_width, image_height)
back_rect = back_image.get_rect(center=(0 + mode_width//2, height - mode_height))

image1080 = p1080(image_width, image_height)
image720 = p720(image_width, image_height)
image1440 = p1440(image_width, image_height)

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
        if screen != "menu":
            win.blit(back_image, back_rect)
    elif modestr == "light":
        win.fill(white)
        win.blit(light_mode_image, light_mode)
        if screen != "menu":
            win.blit(back_light_image, back_rect)

def choice_screen():
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

def result_screen():
    mode(modestr)
    if result == "win":
        if modestr == "dark":
            win.blit(win_i, rock)
            win.blit(lose, scissors)
        else:    
            win.blit(win_light, rock)
            win.blit(lose_light, scissors)
    elif result == "lose":
        if modestr == "dark":
            win.blit(lose, rock)
            win.blit(win_i, scissors)
        else:    
            win.blit(lose_light, rock)
            win.blit(win_light, scissors)
    else:
        if choice_ == "rock":
            win.blit(rock_image, rock)
        elif choice_ == "paper":
            win.blit(paper_image, rock)
        elif choice_ == "scissors":
            win.blit(scissors_image, rock)
        computer = returncomputer()
        if computer == "rock":
            win.blit(rock_image, scissors)
        elif computer == "paper":
            win.blit(paper_image, scissors)
        elif computer == "scissors":
            win.blit(scissors_image, scissors)

def menu_screen():
    mode(modestr)
    win.blit(play_image, paper)
    win.blit(quit_image,rock)
    win.blit(options_image, scissors)

def options_screen():
    mode(modestr)
    win.blit(image1080, paper)
    win.blit(image1440,rock)
    win.blit(image720, scissors)

clock = pygame.time.Clock()
modestr = "dark"
result = ""
choice_ = ""
screen = "menu"
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
        if screen != "choice" and screen != "result":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if screen == "main":
                    if paper.collidepoint(event.pos):
                        result = game("paper")
                        choice_ = "paper"
                        screen = "choice"
                    elif rock.collidepoint(event.pos):
                        result = game("rock")
                        choice_ = "rock"
                        screen = "choice"
                    elif scissors.collidepoint(event.pos):
                        result = game("scissors")
                        choice_ = "scissors"
                        screen = "choice"

                elif screen == "menu":
                    if paper.collidepoint(event.pos):
                        screen = "main"
                    elif rock.collidepoint(event.pos):
                        run = False
                        pygame.quit()              
                        exit()
                    elif scissors.collidepoint(event.pos):
                        screen = "options"

                elif screen == "options":
                        with open("conf.txt", "w") as f:
                            if rock.collidepoint(event.pos):
                                f.write("2560\n1440")
                            elif paper.collidepoint(event.pos):
                                f.write("1920\n1080")
                            elif scissors.collidepoint(event.pos):
                                f.write("1280\n720")
                if light_mode.collidepoint(event.pos) and modestr == "light":
                        modestr = "dark"
                elif dark_mode.collidepoint(event.pos):
                        modestr = "light"
                if back_rect.collidepoint(event.pos):
                    screen = "menu"

        if event.type == timer_event and screen == "choice":
            if result == "win":
                wins += 1
            elif result == "lose":
                losses += 1
            screen = "result"
            pygame.time.set_timer(timer_event, 0)
        elif event.type == timer_event and screen == "result":
            if result == "win":
                wins += 1
            elif result == "lose":
                losses += 1
            screen = "main"
            pygame.time.set_timer(timer_event, 0)

        if screen == "menu":
            menu_screen()
        elif screen == "main":            
                mode(modestr)
                draw()
        elif screen == "choice":
            choice_screen()
            pygame.time.set_timer(timer_event, 1000)
        elif screen == "result":
            result_screen()
            pygame.time.set_timer(timer_event, 1000)  
        elif screen == "options":
            options_screen()

    clock.tick(60)
    pygame.display.update()
