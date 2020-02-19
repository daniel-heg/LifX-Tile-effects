from utils.tilechain_operations import *
from utils.colors import *
from lifxlan import *
from random import randint
from time import sleep

logoArr = [[2, 1, 1], [2, 2, 2], [3, 1, 3], [3, 2, 4]]  # (x, y, Val)
screen = [[0] * 16] * 16
direction = 4


def touchesBorder(logoArr):
    global direction
    for i in logoArr:
        if i[0] == 15:
            direction = randint(6, 12)
            return direction
        elif i[0] == 0:
            direction = randint(0, 6)
            return direction
        elif i[1] == 15:
            rand = randint(1, 12)

            while rand < 10 and rand > 3:
                rand = randint(1, 12)

            direction = rand
            return direction
        elif i[1] == 0:
            direction = randint(3, 9)
            return direction


def touchesCorner(screen):
    global direction
    if screen[0][0] != 0:
        direction = randint(3, 6)
        return direction
    elif screen[0][15] != 0:
        direction = randint(6, 9)
        return direction
    elif screen[15][15] != 0:
        direction = randint(9, 12)
        return direction
    elif screen[15][0] != 0:
        direction = randint(0, 3)
        return direction


def updateLogo(direction):
    if direction == 3:
        for i in logoArr:
            i[0] += 1  # right
    elif direction == 6:
        for i in logoArr:
            i[1] += 1  # down
    elif direction == 9:
        for i in logoArr:
            i[0] -= 1  # left
    elif direction == 12 or direction == 0:
        for i in logoArr:
            i[1] -= 1  # up
    elif direction == 1 or direction == 2:
        for i in logoArr:
            i[0] += 1  # right
            i[1] -= 1  # up
    elif direction == 4 or direction == 5:
        for i in logoArr:
            i[0] += 1  # right
            i[1] += 1  # down
    elif direction == 7 or direction == 8:
        for i in logoArr:
            i[0] -= 1  # left
            i[1] += 1  # down
    elif direction == 10 or direction == 11:
        for i in logoArr:
            i[0] -= 1  # left
            i[1] -= 1  # up


def main():
    global logoArr
    global screen
    global direction
    lan = LifxLAN(1)
    tilechain_lights = lan.get_tilechain_lights()
    if len(tilechain_lights) != 0:
        t = lan.get_tilechain_lights()[0]  # grab the first tilechain
        print("Selected TileChain light: {}".format(t.get_label()))
        original_colors = t.get_tilechain_colors()
        num_tiles = t.get_tile_count()
        duration_ms = 5

        palette = {0: OFF,
                   1: RED,
                   2: CYAN,
                   3: GREEN,
                   4: YELLOW
                   }

        try:
            while True:

                screen = screen = [[0] * 16] * 16
                placeListInMatrix(screen, logoArr)

                matrix = [getTileFromBoard(screen, 0, 0), getTileFromBoard(
                    screen, 0, 1), getTileFromBoard(screen, 1, 1), getTileFromBoard(screen, 1, 0)]

                for index in range(num_tiles):
                    sprite = []
                    for x in range(8):
                        for y in range(8):
                            sprite.append(palette[matrix[index][x][y]])

                    t.set_tile_colors(index, sprite, duration_ms, rapid=True)

                sleep(0.2)

                if touchesCorner(screen) == None:
                    touchesBorder(logoArr)

                updateLogo(direction)

        except KeyboardInterrupt:
            t.set_tilechain_colors(original_colors)
            print("Done.")
    else:
        print("No TileChain lights found.")


if __name__ == "__main__":
    main()
