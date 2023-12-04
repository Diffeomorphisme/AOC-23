import re

def read_file():
    with open("day4/source.txt", "r") as file:
        return file.read()


def problem_1():
    file_contents = read_file()
    total = 0
    for line in file_contents.splitlines():
        match = False
        points = 0
        card = line.split(":")[-1]
        winning_numbers = re.findall(r"[0-9]+", card.split("|")[0])
        available_numbers = re.findall(r"[0-9]+", card.split("|")[-1])

        for number in available_numbers:
            if number in winning_numbers:
                if not match:
                    points = 1
                    match = True
                else:
                    points *= 2
        total += points

    print(f"Problem 1 result: {total}")


def problem_2():
    file_contents = read_file()
    card_map = [1 for _ in range(len(file_contents.splitlines()))]
    for index, line in enumerate(file_contents.splitlines()):
        card = line.split(":")[-1]
        winning_numbers = re.findall(r"[0-9]+", card.split("|")[0])
        available_numbers = re.findall(r"[0-9]+", card.split("|")[-1])

        count = 0
        for number in available_numbers:
            if number in winning_numbers:
                count += 1
        for i in range(count):
            card_map[index + i + 1] += 1 * card_map[index]
    total = sum(card_map)
    print(f"Problem 2 result: {total}")


def run():
    print("Day 4")
    problem_1()
    problem_2()
