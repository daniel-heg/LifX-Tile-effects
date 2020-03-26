from utils.tilechain_operations import getTileFromBoard
from utils.asciiFont import *
from utils.colors import *
from lifxlan import LifxLAN
from time import sleep
import datetime


def main():
    lan = LifxLAN(1)
    tilechain_lights = lan.get_tilechain_lights()
    if len(tilechain_lights) != 0:
        t = lan.get_tilechain_lights()[0]  # grab the first tilechain
        print("Selected TileChain light: {}".format(t.get_label()))
        original_colors = t.get_tilechain_colors()
        num_tiles = t.get_tile_count()

        DIM_BLUE = BLUE
        DIM_BLUE[2] = DIM_BLUE[2] / 3

        palette = {0: OFF,
                   1: CYAN
                   }

        try:
            while True:

                timeBitMatrix = concatChars(stringToTileMatrix(str(datetime.datetime.now().time().hour).zfill(2) +
                                                               str(datetime.datetime.now().time().minute).zfill(2)))

                matrix = [getTileFromBoard(timeBitMatrix, 0, 0),
                          getTileFromBoard(timeBitMatrix, 0, 1),
                          getTileFromBoard(timeBitMatrix, 0, 3),
                          getTileFromBoard(timeBitMatrix, 0, 2)]

                for index in range(num_tiles):
                    sprite = []
                    for x in range(8):
                        for y in range(8):
                            sprite.append(palette[matrix[index][x][y]])

                    t.set_tile_colors(index, sprite, rapid=True)

                sleep(5)

        except KeyboardInterrupt:
            t.set_tilechain_colors(original_colors)
            print("Done.")
    else:
        print("No TileChain lights found.")


if __name__ == "__main__":
    main()
