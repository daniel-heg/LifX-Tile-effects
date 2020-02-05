from lifxlan import *
from utils.colors import *
from utils.tilechain_operations import *
from random import randint
from time import sleep

logoArray = [(0, 0, 1), (0, 1, 2), (1, 0, 3), (1, 1, 4)]
screen = [[0] * 16] * 16


def main():
    lan = LifxLAN(1)
    tilechain_lights = lan.get_tilechain_lights()
    if len(tilechain_lights) != 0:
        t = lan.get_tilechain_lights()[0]  # grab the first tilechain
        print("Selected TileChain light: {}".format(t.get_label()))
        original_colors = t.get_tilechain_colors()
        num_tiles = t.get_tile_count()

        num_tiles = t.get_tile_count()
        duration_ms = 5
        palette = {0: OFF,
                   1: RED,
                   2: GREEN,
                   3: CYAN,
                   4: YELLOW
                   }

        placeListInMatrix(screen, logoArray)

        matrix = [getTileFromBoard(screen, 0, 0), getTileFromBoard(
            screen, 0, 1), getTileFromBoard(screen, 1, 1), getTileFromBoard(screen, 1, 0)]

        try:

            for index in range(num_tiles):
                sprite = []
                for x in range(8):
                    for y in range(8):
                        sprite.append(palette[matrix[index][x][y]])

                t.set_tile_colors(index, sprite, duration_ms, rapid=False)

            sleep(300)

        except KeyboardInterrupt:
            t.set_tilechain_colors(original_colors)
            print("Done.")
    else:
        print("No TileChain lights found.")


if __name__ == "__main__":
    main()
