import time
import csv

# import sys
# import os


def start_session(start_time):
    while time.time() - start_time <= 20:
        x = int(input())
        print(x)

    print("Your 5 min session has ran out! Well done")
    print(
        "You scored: ",
    )


if __name__ == "__main__":
    start_time = time.time()

    start_session(start_time)
