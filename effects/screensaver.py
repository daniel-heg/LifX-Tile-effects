from utils.tilechain_operations import getTileFromBoard, placeListInMatrix
from utils.colors import OFF, RED, CYAN, GREEN, YELLOW
from lifxlan import LifxLAN
from random import randint
from time import sleep

logoArr = [[2, 1, RED],  # (x, y, Val)
           [2, 2, CYAN],
           [3, 1, GREEN],
           [3, 2, YELLOW]]
screen = [[OFF] * 16] * 16
direction = 4


def touchesBorder(logoArr):
    global direction
    for i in logoArr:

        if i[0] == 15:  # hits right

            if 3 < direction < 6:
                direction = randint(6, 9)
            elif 0 < direction < 3:
                direction = randint(9, 12)
            else:
                direction = randint(6, 12)

            return

        elif i[0] == 0:  # hits left

            if 9 < direction < 12:
                direction = randint(0, 3)
            elif 6 < direction < 9:
                direction = randint(3, 6)
            else:
                direction = randint(0, 6)

            return

        elif i[1] == 15:  # hits bottom

            if 3 < direction < 6:
                direction = randint(0, 3)
            elif 6 < direction < 9:
                direction = randint(9, 12)
            else:
                direction = randint(0, 11)

                while 3 < direction < 9:
                    direction = randint(0, 11)

            return

        elif i[1] == 0:  # hits top

            if 0 < direction < 3:
                direction = randint(3, 6)
            elif 9 < direction < 12:
                direction = randint(6, 9)
            else:
                direction = randint(3, 9)

            return


def touchesCorner():
    global direction
    global screen
    if screen[0][0] != OFF:
        direction = randint(3, 6)
        return True
    elif screen[0][15] != OFF:
        direction = randint(6, 9)
        return True
    elif screen[15][15] != OFF:
        direction = randint(9, 12)
        return True
    elif screen[15][0] != OFF:
        direction = randint(0, 3)
        return True

    return False


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

        try:
            while True:

                screen = [[OFF] * 16] * 16
                placeListInMatrix(screen, logoArr)

                matrix = [getTileFromBoard(screen, 0, 0),
                          getTileFromBoard(screen, 0, 1),
                          getTileFromBoard(screen, 1, 1),
                          getTileFromBoard(screen, 1, 0)]

                for index in range(num_tiles):
                    sprite = []
                    for x in range(8):
                        for y in range(8):
                            sprite.append(matrix[index][x][y])

                    t.set_tile_colors(index, sprite, duration_ms, rapid=True)

                sleep(0.2)

                if touchesCorner() == False:
                    touchesBorder(logoArr)

                updateLogo(direction)

        except KeyboardInterrupt:
            t.set_tilechain_colors(original_colors)
            print("Done.")
    else:
        print("No TileChain lights found.")


if __name__ == "__main__":
    main()
