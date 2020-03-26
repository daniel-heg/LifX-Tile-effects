import soundcard as sc
import numpy as np


def defaultOutAsMic():
    return sc.get_microphone(sc.default_speaker().name, include_loopback=True)


def micSelector():

    all_mics = sc.all_microphones(include_loopback=True)
    counter = 0

    print("Please select the audio device which you want to use for visualization:")

    for e in all_mics:
        print("\t" + str(counter) + ".\t" + str(e))
        counter += 1

    index = int(input("Device num: "))

    return all_mics[index]

# example:
# loopback = defaultOutAsMic()

# with loopback.recorder(samplerate=44100) as mic, sc.default_speaker().player(samplerate=44100) as sp:
#     for i in range(1000):
#         data = mic.record(numframes=1024)
#         peak = np.floor(np.max(np.abs(data))*512)
#         print("#" * int(peak))

