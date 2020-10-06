import pygame
from network import Network
from player import Player

width = 800
height = 600

win = pygame.display.set_mode((width, height))
pygame.display.set_caption('PowWow Client')

clientNumber = 0


# def read_pos(str):
#     str = str.split(",")
#     return int(str[0]), int(str[1])
#
# def make_pos(tup):
#     return str(tup[0]) + "," + str(tup[1])


def redrawWindow(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    # startpos = read_pos(n.getPos())
    # p = Player(startpos[0], startpos[1], 50, 100, 100, (0, 0, 255))
    # p2 = Player(0, 0, 50, 100, 100, (255, 0, 0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        # p2pos = read_pos(n.send(make_pos((p.x, p.y))))
        # p2.x = p2pos[0]
        # p2.y = p2pos[1]
        # p2.update()

        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False
                pygame.quit()

        # p.move()
        # redrawWindow(win, p, p2)

main()