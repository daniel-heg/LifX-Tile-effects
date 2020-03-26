from utils.tilechain_operations import *
from utils.audio import *
from lifxlan import LifxLAN
from time import sleep

import soundcard as sc
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

        try:

            loopback = micSelector()

            with loopback.recorder(samplerate=44100) as mic, sc.default_speaker().player(samplerate=44100) as sp:
                while True:

                    data = mic.record(numframes=1024)
                    peak = np.floor(np.max(np.abs(data))*512)
                    print(peak*500)

                    for index in range(num_tiles):
                        sprite = []
                        for x in range(8):
                            for y in range(8):
                                if peak*500 > 65535:
                                    sprite.append([65535, 65535, 65535, 3500])
                                else:
                                    sprite.append([58275, 0, peak * 500, 3500])

                        t.set_tile_colors(index, sprite, duration_ms, rapid=True)


        except KeyboardInterrupt:
            t.set_tilechain_colors(original_colors)
            print("Done.")
    else:
        print("No TileChain lights found.")


if __name__ == "__main__":
    main()
