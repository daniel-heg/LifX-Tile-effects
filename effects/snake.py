from utils.tilechain_operations import *
from utils.colors import *
from lifxlan import *
from random import randint, randrange
from time import sleep
import threading
import keyboard
import sys

matrixSize = 16 
snakeList = [(1, 1, 'm'), (2, 1, 'm'), (3, 1, 'm'),  # (x, y)
             (3, 2, 'm'), (4, 2, 'm'), (5, 2, 'h')]
direction = 'd'  # directions are "w" "a" "s" "d"
shouldRun = True
gameBoard = [['.'] * matrixSize] * matrixSize


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


def foodTupel(gameBoard, snakeList):
    x = randrange(matrixSize)
    y = randrange(matrixSize)

    while (gameBoard[y][x] != '.'):
        x = randrange(matrixSize)
        y = randrange(matrixSize)

    return (x, y)


def placeFood(gameBoard, foodTupel):
    gameBoard[foodTupel[1]] = placeTupleInMatrix(
        gameBoard[foodTupel[1]], foodTupel[0], 'f')


def moveSnake(snakeList, direction, placeFood):
    global shouldRun
    head = snakeList[len(snakeList) - 1]
    newHead = (0, 0)

    if direction == 'w':
        if (head[1] - 1) < 0:
            newHead = (head[0], matrixSize - 1)
        else:
            newHead = (head[0], head[1] - 1)
    elif direction == 'a':
        if (head[0] - 1) < 0:
            newHead = (matrixSize - 1, head[1])
        else:
            newHead = (head[0] - 1, head[1])
    elif direction == 's':
        if (head[1] + 1) >= matrixSize:
            newHead = (head[0], 0)
        else:
            newHead = (head[0], head[1] + 1)
    elif direction == 'd':
        if (head[0] + 1) >= matrixSize:
            newHead = (0, head[1])
        else:
            newHead = (head[0] + 1, head[1])

    if (newHead in snakeList):
        shouldRun = 0
        sleep(0.2)
        print("\n--------------------------------------------------------\n")
        print("Game Over! Your Snake had the size: " + str(len(snakeList)))
        print("\n--------------------------------------------------------")
        return

    gameBoard[head[1]] = placeTupleInMatrix(
        gameBoard[head[1]], head[0], 'm')
    gameBoard[newHead[1]] = placeTupleInMatrix(
        gameBoard[newHead[1]], newHead[0], 'h')
    snakeList.append(newHead)

    if (newHead == placeFood):
        return True

    last = snakeList.pop(0)
    gameBoard[last[1]] = placeTupleInMatrix(
        gameBoard[last[1]], last[0], '.')
    return False


def steering():
    global shouldRun
    global direction

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

        palette = {'.': OFF,
                   'm': CYAN,
                   'h': GREEN,
                   'f': PURPLE
                   }

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
