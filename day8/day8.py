import re


def read_file():
    with open("day8/source.txt", "r") as file:
        return file.read()


def problem_1():
    file_contents = read_file()
    total = 0
    print(f"Problem 1 result: {total}")


def problem_2():
    file_contents = read_file()
    pattern = ""
    directions = {}
    for index, line in enumerate(file_contents.splitlines()):
        if index == 0:
            pattern = line.strip()
            continue
        if not "=" in line:
            continue
        key = line.split("=")[0].strip()
        values = line.split("=")[-1].strip().replace("(", "").replace(")", "")
        left, right = values.split(",")
        directions.setdefault(
            key,
            {"L": left.strip(), "R": right.strip()}
        )
    i = 0
    total_counter = 1
    current_spot = "AAA"
    destination = "ZZZ"
    while True:
        if i == len(pattern):
            i = 0
        move = pattern[i]
        current_spot = directions.get(current_spot).get(move)
        if current_spot == destination:
            break
        i += 1
        total_counter += 1
    total = total_counter
    print(f"Problem 2 result: {total}")


def run():
    print("Day 8")
    problem_1()
    problem_2()
