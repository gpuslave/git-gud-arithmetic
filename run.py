import time
import csv
import random
import re
from collections import namedtuple


# import sys
import os

OPERATIONS = ("+", "-", "*")
OPERATOR_MAP = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x // y,
}


def isoperation(string: str):
    return string in OPERATIONS


def start_session(start_time, game_config):
    log_list = []
    score, total = 0, 0
    answ = None
    op = game_config.operation
    while time.time() - start_time <= 35:
        x = random.randint(1, 10 ** int(game_config.first_num) - 1)
        y = random.randint(1, 10 ** int(game_config.second_num) - 1)
        think_time_start = time.time()
        print(f"{x} {op} {y}")

        answ = OPERATOR_MAP[op](x, y)

        res = int("".join(re.split(r"(?!-)\D*", input(), flags=re.IGNORECASE)))
        think_time_end = time.time()

        right = False
        if res == answ:
            score += 1
            right = True

        log_list.append(
            {
                "num_1": x,
                "operation": op,
                "num_2": y,
                "is_right": int(right),
                "think_time": round(think_time_end - think_time_start, 3),
            }
        )

        total += 1
    with open("results.csv", "a", newline="") as csvfile:
        fieldnames = ["num_1", "operation", "num_2", "is_right", "think_time"]
        logwriter = csv.DictWriter(csvfile, delimiter=",", fieldnames=fieldnames)

        if os.path.getsize("results.csv") <= 0:
            logwriter.writeheader()

        for log in log_list:
            logwriter.writerow(log)

    print("Your session has ran out! Well done")
    print(
        f"You scored: {score}/{total}, that's {int(score/total*100)}% accuracy",
    )

    if not all([bool(x["is_right"]) for x in log_list]):
        print("You've failed at: ")
        for log in log_list:
            if not log["is_right"]:
                print(log["num_1"], log["operation"], log["num_2"])


if __name__ == "__main__":
    start_time = time.time()

    print('Welcome to the ultimate "git-gud-arithmetic" game!')
    print(
        "Please input 3 values: (num size, num size, operation) separated by spaces\n",
        "e.g.: 1 2 + ",
    )
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
