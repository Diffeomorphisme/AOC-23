import re


def read_file():
    with open("day3/source.txt", "r") as file:
        return file.read()


def problem_1():
    file_contents = read_file()
    total = 0
    split_file = file_contents.splitlines()
    for index, line in enumerate(split_file):
        numbers = re.findall(r"[0-9]+", line)
        end = 0
        for number in numbers:
            start = end + line[end:].index(number)
            end = start + len(number)
            check_start = max(start - 1, 0)
            check_end = min(end + 1, len(line))
            if index > 0:
                if not split_file[index - 1][check_start:check_end] == "." * (check_end - check_start):
                    total += int(number)
                    continue
            if index < len(split_file) - 1:
                if not split_file[index + 1][check_start:check_end] == "." * (check_end - check_start):
                    total += int(number)
                    continue
            if start > 0:
                if not split_file[index][start - 1] == ".":
                    total += int(number)
                    continue
            if end < len(line) - 1:
                if not split_file[index][end] == ".":
                    total += int(number)
                    continue
    print(f"Problem 1 result: {total}")


def add_star_position(position, number, stars):
    star_positions = [star.get("position") for star in stars]
    if position not in star_positions:
        stars.append(
            {
                "position": position,
                "number": int(number),
                "count": 1
            }
        )
    else:
        for star in stars:
            if star.get("position") == position:
                star["count"] += 1
                star["number"] *= int(number)
                break
    return stars


def problem_2():
    file_contents = read_file()
    stars = []
    star_positions = []
    star_adjacent_numbers = []
    total = 0
    split_file = file_contents.splitlines()
    for index, line in enumerate(split_file):
        numbers = re.findall(r"[0-9]+", line)
        end = 0
        for number in numbers:
            print(number)
            start = end + line[end:].index(number)
            end = start + len(number)
            check_start = max(start - 1, 0)
            check_end = min(end + 1, len(line))
            if index > 0:
                if not split_file[index - 1][check_start:check_end] == "." * (check_end - check_start):
                    if "*" in split_file[index - 1][check_start:check_end]:
                        position = (index - 1, split_file[index - 1][check_start:check_end].index("*") + check_start)
                        stars = add_star_position(position, number, stars)

            if index < len(split_file) - 1:
                if not split_file[index + 1][check_start:check_end] == "." * (check_end - check_start):
                    if "*" in split_file[index + 1][check_start:check_end]:
                        position = (index + 1, split_file[index + 1][check_start:check_end].index("*") + check_start)
                        stars = add_star_position(position, number, stars)

            if start > 0:
                if split_file[index][start - 1] == "*":
                    position = (index, start - 1)
                    stars = add_star_position(position, number, stars)

            if end < len(line) - 1:
                if split_file[index][end] == "*":
                    position = (index, end)
                    stars = add_star_position(position, number, stars)
    total += sum([star.get("number") for star in stars if star.get("count") == 2])
    print(f"Problem 2 result: {total}")


def run():
    print("Day 1")
    problem_1()
    problem_2()
