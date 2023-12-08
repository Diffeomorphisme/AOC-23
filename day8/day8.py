import math


def read_file():
    with open("day8/source.txt", "r") as file:
        return file.read()


def problem_1():
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
    current_spots = [key for key in directions.keys() if key[-1] == "A"]
    cycles = []
    while True:
        if i == len(pattern):
            i = 0
        move = pattern[i]
        new_spots = []
        for current_spot in current_spots:
            new_spot = directions.get(current_spot).get(move)
            if new_spot[-1] == "Z":
                cycles.append(total_counter)
            else:
                new_spots.append(new_spot)
        if all([new_spot[-1] == "Z" for new_spot in new_spots]) or not new_spots:
            break
        i += 1
        total_counter += 1
        current_spots = new_spots
    total = math.lcm(*tuple(cycles))
    print(f"Problem 2 result: {total}")


def run():
    print("Day 8")
    # problem_1()
    problem_2()
