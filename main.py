import pygame


def draw(screen, color, inp):
    black = pygame.Color('black')
    white = pygame.Color('white')
    rect_size = int(inp[0]) //  int(inp[1])
    for i in range(0, int(inp[0]), rect_size):
        for j in range(0, int(inp[0]), rect_size):
            if color:
                pygame.draw.rect(screen, white,(i, j, rect_size, rect_size), 0)
                color = False
            elif not color:
                pygame.draw.rect(screen, black,(i, j, rect_size, rect_size), 0)
                color = True


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Крест')
    inp = input().split()
    size = width, height = int(inp[0]), int(inp[0])
    screen = pygame.display.set_mode(size)
    color = None
    if int(inp[1]) % 2 == 0:
        color = True
    else:
        color = False
    draw(screen, color, inp)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()