from utils.tilechain_operations import *
from utils.colors import *
from lifxlan import *
from random import randint, randrange
from time import sleep
import threading
import keyboard
import sys

matrixSize = 16
shouldRun = True
gameBoard = [[0] * matrixSize] * matrixSize

palette = {0: OFF,
           1: CYAN,
           2: YELLOW,
           3: PURPLE,
           4: BLUE,
           5: ORANGE,
           6: GREEN,
           7: RED
           }


block_I = [(0, 7, 1), (1, 7, 1), (2, 7, 1), (3, 7, 1)]  # cyan
block_O = [(0, 7, 2), (1, 7, 2), (0, 8, 2), (1, 8, 2)]  # yellow
block_T = [(0, 7, 3), (0, 8, 3), (0, 9, 3), (1, 8, 3)]  # pink
block_J = [(0, 7, 4), (0, 8, 4), (0, 9, 4), (1, 9, 4)]  # blue
block_L = [(0, 7, 5), (0, 8, 5), (0, 9, 5), (1, 7, 5)]  # orange
block_S = [(1, 7, 6), (1, 8, 6), (0, 8, 6), (0, 9, 6)]  # green
block_Z = [(0, 7, 7), (0, 8, 7), (1, 8, 7), (1, 9, 7)]  # red


def constantPrint():
    global gameBoard

    while (shouldRun):
        buff = ""

        for i in gameBoard:
            for j in i:
                buff += str(j) + " "
            buff += "\n"

        sleep(0.15)
        print(buff)


def steering():
    global shouldRun
    
    while (shouldRun):
        if keyboard.is_pressed('w'):
            if (direction != 's'):
                direction = 'w'
        elif keyboard.is_pressed('a'):
            if (direction != 'd'):
                direction = 'a'
        elif keyboard.is_pressed('s'):
            if (direction != 'w'):
                direction = 's'
        elif keyboard.is_pressed('d'):
            if (direction != 'a'):
                direction = 'd'


def main():
    global shouldRun
    global gameBoard
    lan = LifxLAN(1)
    tilechain_lights = lan.get_tilechain_lights()
    if len(tilechain_lights) != 0:
        t = lan.get_tilechain_lights()[0]  # grab the first tilechain
        print("Selected TileChain light: {}".format(t.get_label()))
        original_colors = t.get_tilechain_colors()
        num_tiles = t.get_tile_count()

        foodPos = foodTupel(gameBoard, snakeList)

        placeFood(gameBoard, foodPos)
        placeListInMatrix(gameBoard, snakeList)

        #printT = threading.Thread(target=constantPrint, args=())
        # printT.start()
        steerT = threading.Thread(target=steering, args=())
        steerT.start()

        try:
            while shouldRun:

                sleep(0.1)

                if (moveSnake(snakeList, direction, foodPos)):
                    foodPos = foodTupel(gameBoard, snakeList)
                    placeFood(gameBoard, foodPos)

                matrix = [getTileFromBoard(gameBoard, 0, 0),
                          getTileFromBoard(gameBoard, 0, 1),
                          getTileFromBoard(gameBoard, 1, 1),
                          getTileFromBoard(gameBoard, 1, 0)]

                for index in range(num_tiles):
                    sprite = []
                    for x in range(8):
                        for y in range(8):
                            sprite.append(palette[matrix[index][x][y]])

                    t.set_tile_colors(index, sprite, rapid=True)

            t.set_tilechain_colors(original_colors)

        except KeyboardInterrupt:
            t.set_tilechain_colors(original_colors)
            shouldRun = 0
            sleep(0.2)
            print("Done.")
    else:
        print("No TileChain lights found.")


if __name__ == "__main__":
    main()
