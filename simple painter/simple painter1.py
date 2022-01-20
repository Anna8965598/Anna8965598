import pygame

pygame.init()

white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
black = 0, 0, 0
grey = 220, 220, 220
orange = 229, 160, 11
pink = 231, 62, 239
yellow = 242, 232, 67

brush = 25
line = 3

tinyfont = pygame.font.SysFont('', 15)
smallfont = pygame.font.SysFont('', 25)
medfont = pygame.font.SysFont('', 50)
largefont = pygame.font.SysFont('', 80)

screen_size = (1000, 800)
colours = [white, red, green, blue, black, grey, orange, pink, yellow]

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('simple painter')
screen.fill(white)

pygame.display.flip()

clock = pygame.time.Clock()
fps = 500

running = True
pen_colour = black


def button(text, x, y, width, height, inactivecol, activecol = 'black', action = 0):
    global pen_colour, line
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cursor[0] > x and y + height > cursor[1] > y:
        pygame.draw.rect(screen, activecol, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == 'quit':
                pygame.quit()
                quit()
            elif action == '-':
                if line > 2:
                    line -= 1
            elif action == '+':
                if line < 15:
                    line += 1
            elif action != None and action != 'quit':
                pen_colour = action

    else:
        pygame.draw.rect(screen, inactivecol, (x, y, width, height))
    text_to_button(text, black, x, y, width, height)

def text_obj(text, colour, size):
    if size == 'tiny':
        textsurface = tinyfont.render(text, True, colour)
    elif size == 'small':
        textsurface = smallfont.render(text, True, colour)
    elif size == 'med':
        textsurface = medfont.render(text, True, colour)
    elif size == 'large':
        textsurface = largefont.render(text, True, colour)
    return textsurface, textsurface.get_rect()

def message(msg, colour, x_displace=0, y_displace=0, size = 'small'):
    textSurf, textRect = text_obj(msg, colour, size)
    textRect = x_displace, y_displace
    screen.blit(textSurf, textRect)

def text_to_button(msg, colour, butx, buty, butwidth, butheight, size='small'):
    textSurf, textRect = text_obj(msg, colour, size)
    textRect.center = ((butx + (butwidth / 2)), buty + (butheight / 2))
    screen.blit(textSurf, textRect)

while running:
    pygame.draw.rect(screen, grey, (100, 0, 800, 900), 1)
    pygame.draw.rect(screen, white, (0, 0, 100, 800))
    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        col = 0
        for x in range(3):
            for i in range(3):
                button(None, 10 + (brush * x), 90 + (brush * i), brush, brush, colours[col], action = colours[col])
                col += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_COMMA:
                if line > 2:
                    line -= 1
            if event.key == pygame.K_PERIOD:
                if line < 15:
                    line += 1
        if 100 < pos[0] < 1000 and 1 < pos[1] < 900:
            if click[0] == 1:
                pygame.draw.circle(screen, pen_colour, pos, line)
        button('-', 10, 25, brush, brush, white, grey, action = '-')
        button('+', 60, 25, brush, brush, white, grey, action = '+')
        pygame.display.flip()
        clock.tick(fps)