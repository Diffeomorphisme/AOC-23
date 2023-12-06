import re
def read_file():
    with open("day6/source.txt", "r") as file:
        return file.read()


def problem_1():
    file_contents = read_file()
    distances = []
    times = []
    total = 1
    for line in file_contents.splitlines():
        if "Distance" in line:
            distances = [int(distance) for distance in re.findall(r"[0-9]+", line)]
        if "Time" in line:
            times = [int(time) for time in re.findall(r"[0-9]+", line)]

    wins = []
    for index, time, distance in zip([i for i in range(len(times))], times, distances):
        for tick in range(1, time + 1):
            score = (time - tick) * tick
            if score > distance:
                if len(wins) == index + 1:
                    wins[index] += 1
                else:
                    wins.append(1)
    for win in wins:
        total *= win

    print(f"Problem 1 result: {total}")


def problem_2():
    file_contents = read_file()
    distance_text = ""
    time_text = ""
    for line in file_contents.splitlines():
        if "Distance" in line:
            for number in re.findall(r"[0-9]+", line):
                distance_text += number
        if "Time" in line:
            for number in re.findall(r"[0-9]+", line):
                time_text += number
    distance = int(distance_text)
    time = int(time_text)

    wins = 0
    for tick in range(1, time + 1):
        score = (time - tick) * tick
        if score > distance:
            wins += 1

    total = wins
    print(f"Problem 2 result: {total}")


def run():
    print("Day 6")
    problem_1()
    problem_2()
