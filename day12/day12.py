import re


def read_file():
    with open("day12/source.txt", "r") as file:
        return file.read()


def get_all_possibilities(springs: list):
    if len(springs) == 1:
        return [["."], ["#"]]
    else:
        possibilities = get_all_possibilities(springs[1:])
        output = []
        for possibility in possibilities:
            possibility1 = ["."]
            possibility2 = ["#"]
            possibility1.extend(possibility)
            possibility2.extend(possibility)
            output.append(possibility1)
            output.append(possibility2)
        return output


def check_that_records_match(test_record, reference_record):
    count = 0
    groups = []
    for spring in test_record:
        if spring == "." and count > 0:
            groups.append(count)
            count = 0
            continue
        elif spring == "#":
            count += 1
    if count > 0:
        groups.append(count)
    return groups == reference_record


def problem_1():
    file_contents = read_file()
    total = 0
    for line in file_contents.splitlines():
        spring_record = [char for char in line.split(" ")[0]]
        extra_record = [int(number) for number in re.findall(r"[0-9]+", line.split(" ")[-1])]
        unknown_springs = [index for index, spring in enumerate(spring_record) if spring == "?"]
        all_possibilities = get_all_possibilities(unknown_springs)
        for possibility in all_possibilities:
            spring_record_copy = spring_record
            for index, unknown_spring in enumerate(unknown_springs):
                spring_record_copy[unknown_spring] = possibility[index]
            if check_that_records_match(spring_record_copy, extra_record):
                total += 1

    print(f"Problem 1 result: {total}")


def problem_2():
    file_contents = read_file()
    total = 0
    print(f"Problem 2 result: {total}")


def run():
    print("Day 12")
    problem_1()
    problem_2()
