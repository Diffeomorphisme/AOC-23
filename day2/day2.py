import re


def read_file():
    with open("day2/source.txt", "r") as file:
        return file.read()


max_colors = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def problem_1():
    file_contents = read_file()
    total = 0
    for line in file_contents.splitlines():
        game_possible = True
        game_number = int(re.findall(r"[0-9]+", line.split(":")[0])[0])
        games = line.split(":")[-1].split(";")
        for game in games:
            for color_drawn in game.split(","):
                for color, value in max_colors.items():
                    if color in color_drawn and int(re.findall(r"[0-9]+", color_drawn)[0]) > value:
                        game_possible = False
                        break
                if not game_possible:
                    break
            if not game_possible:
                break
        if not game_possible:
            continue
        total += game_number
    print(f"Problem 1 result: {total}")


def problem_2():
    file_contents = read_file()
    total = 0
    for line in file_contents.splitlines():
        colors = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        games = line.split(":")[-1].split(";")
        for game in games:
            for color_drawn in game.split(","):
                for color, value in colors.items():
                    if color in color_drawn:
                        colors[color] = max(value, int(re.findall(r"[0-9]+", color_drawn)[0]))
        min_values = [x for x in colors.values()]
        power = 1
        for value in min_values:
            power *= value
        total += power
    print(f"Problem 2 result: {total}")


def run():
    print("Day 1")
    problem_1()
    problem_2()
