import time
import csv
import random
from collections import namedtuple

# import sys
# import os
OPERATIONS = ("+", "-", "*")


def isoperation(string: str):
    return string in OPERATIONS


def start_session(start_time, game_config):
    while time.time() - start_time <= 20:
        x = random.randint(0, 10**game_config.first_num)
        y = random.randint(0, 10**game_config.second_num)

        answ = x
        res = int(input())
        print(x)

    print("Your 5 min session has ran out! Well done")
    print(
        "You scored: ",
    )


if __name__ == "__main__":
    start_time = time.time()

    print('Welcome to the ultimate "git gud counting" game!')
    print("Please input 3 values: (num size, num size, operation)")
    config_tuple = namedtuple("Config", ["first_num", "second_num", "operation"])
    game_config = config_tuple._make(str(input()).split(sep=None))

    print(game_config.__repr__())
    # if all(
    #     game_config..isnumeric(),
    #     game_config[1].isnumeric(),
    #     isoperation(game_config[2]),
    # ):
    #     print("Wrong input, try again.")
    #     exit(1)

    start_session(start_time, game_config)
