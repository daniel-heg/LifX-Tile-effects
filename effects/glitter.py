from utils.colors import *
from lifxlan import LifxLAN
from random import randint
from time import sleep


def main():
    lan = LifxLAN(1)
    tilechain_lights = lan.get_tilechain_lights()
    if len(tilechain_lights) != 0:
        t = lan.get_tilechain_lights()[0]  # grab the first tilechain
        print("Selected TileChain light: {}".format(t.get_label()))
        original_colors = t.get_tilechain_colors()
        num_tiles = t.get_tile_count()

        palette = [OFF, OFF, OFF, GOLD]

        try:

            while True:

                for index in range(num_tiles):
                    sprite = []
                    for x in range(8):
                        for y in range(8):
                            sprite.append(
                                palette[randint(0, len(palette) - 1)])

                    t.set_tile_colors(index, sprite, duration=150, rapid=True)

                sleep(0.05)

        except KeyboardInterrupt:
            t.set_tilechain_colors(original_colors)
            print("Done.")
    else:
        print("No TileChain lights found.")


if __name__ == "__main__":
    main()
