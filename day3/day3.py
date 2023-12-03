import re


def read_file():
    with open("day3/source.txt", "r") as file:
        return file.read()


def problem_1():
    file_contents = read_file()
    total = 0
    split_file = file_contents.splitlines()
    for index, line in enumerate(split_file):
        print(line)
        numbers = re.findall(r"[0-9]+", line)
        if numbers:
            for number in numbers:
                print(number)
                start = line.index(number)
                end = start + len(number)
                check_start = max(start - 1, 0)
                check_end = min(end + 1, len(line))
                print(start, check_start)
                print(end, check_end)
                if index > 0:
                    print(split_file[index - 1][check_start:check_end])
                    if not split_file[index - 1][check_start:check_end] == "."*(check_end - check_start):
                        total += int(number)
                        continue
                if index < len(split_file) - 1:
                    print(split_file[index + 1][check_start:check_end])
                    if not split_file[index + 1][check_start:check_end] == "."*(check_end - check_start):
                        total += int(number)
                        continue
                if start > 0:
                    if not split_file[index][start - 1] == ".":
                        total += int(number)
                        continue
                if end < len(line):
                    if not split_file[index][end] == ".":
                        total += int(number)
                        continue
                print("bad number")

    print(f"Problem 1 result: {total}")


def problem_2():
    file_contents = read_file()
    total = 0
    print(f"Problem 2 result: {total}")


def run():
    print("Day 1")
    problem_1()
    problem_2()
