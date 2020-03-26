from utils.tilechain_operations import getTileFromBoard
from utils.asciiFont import *
from utils.colors import *
from lifxlan import LifxLAN
from time import sleep
import datetime
import numpy as np


def main():
    lan = LifxLAN(1)
    tilechain_lights = lan.get_tilechain_lights()
    if len(tilechain_lights) != 0:
        t = lan.get_tilechain_lights()[0]  # grab the first tilechain
        print("Selected TileChain light: {}".format(t.get_label()))
        original_colors = t.get_tilechain_colors()
        num_tiles = t.get_tile_count()
        duration_ms = 5

        palette = {0: OFF,
                   1: CYAN
                   }

        text = input("Please insert Text (only ASCII chars are supported): ")

        textBMap = toTileSize(concatChars(stringToBitMatrix(text)))
        toDraw = concatChars([[[0] * 32] * 8, textBMap])

        try:
            while True:

                toDraw = np.roll(toDraw, -2, axis=1)  # scroll direction

                matrix = [getTileFromBoard(toDraw, 0, 0),
                          getTileFromBoard(toDraw, 0, 1),
                          getTileFromBoard(toDraw, 0, 3),
                          getTileFromBoard(toDraw, 0, 2)]

                for index in range(num_tiles):
                    sprite = []
                    for x in range(8):
                        for y in range(8):
                            sprite.append(palette[matrix[index][x][y]])

                    t.set_tile_colors(index, sprite, duration_ms, rapid=True)

                # printBitmap(toDraw)
                sleep(0.4)

        except KeyboardInterrupt:
            t.set_tilechain_colors(original_colors)
            print("Done.")
    else:
        print("No TileChain lights found.")


if __name__ == "__main__":
    main()
