from gameLib import *

import time
import random

def bot():
    while True:
        garden = fetchGarden()
        line = random.randint(0, len(garden) - 1)
        column = random.randint(0, len(garden) - 1)
        plant(line, column, "CARROT")
        time.sleep(0.5)

def __main__():
    bot()

if __name__ == "__main__":
    __main__()