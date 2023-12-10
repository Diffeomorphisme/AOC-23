import re


def read_file():
    with open("day9/source.txt", "r") as file:
        return file.read()


def generate_next_number(sequence: list[int]):
    if sequence == [0 for i in range(len(sequence))]:
        return 0
    else:
        next_sequence = []
        for i in range(len(sequence) - 1):
            next_sequence.append((sequence[i + 1] - sequence[i]))
        output = sequence[-1] + generate_next_number(next_sequence)
        return output


def generate_previous_number(sequence: list[int]):
    if sequence == [0 for i in range(len(sequence))]:
        return 0
    else:
        next_sequence = []
        for i in range(len(sequence) - 1):
            next_sequence.append((sequence[i] - sequence[i + 1]))
        output = sequence[-1] + generate_next_number(next_sequence)
        return output


def problem_1():
    file_contents = read_file()
    total = 0
    for line in file_contents.splitlines():
        sequence = [int(number) for number in re.findall(r"\-*[0-9]+", line)]
        total += generate_next_number(sequence)
    print(f"Problem 1 result: {total}")


def problem_2():
    file_contents = read_file()
    total = 0
    for line in file_contents.splitlines():
        sequence = [int(number) for number in re.findall(r"\-*[0-9]+", line)][::-1]
        total += generate_next_number(sequence)
    print(f"Problem 2 result: {total}")


def run():
    print("Day 9")
    problem_1()
    problem_2()