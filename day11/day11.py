def read_file():
    with open("day11/source.txt", "r") as file:
        return file.read()


def problem_1():
    file_contents = read_file()
    total = 0
    galaxies = []
    matrix = []
    empty_lines = []
    empty_columns = []
    for x, line in enumerate(file_contents.splitlines()):
        matrix.append([char for char in line.strip()])
        if "#" in line:
            for y, char in enumerate(line):
                if char == "#":
                    galaxies.append([x, y])
        else:
            empty_lines.append(x)

    for index in range(len(matrix[0])):
        if all(x == "." for x in [matrix[i][index] for i in range(len(matrix))]):
            empty_columns.append(index)

    for galaxy_1_nr, galaxy_1 in enumerate(galaxies):
        for galaxy_2_nr, galaxy_2 in enumerate(galaxies):
            if galaxy_2_nr <= galaxy_1_nr:
                continue
            distance = abs(galaxy_2[1] - galaxy_1[1]) + abs(galaxy_2[0] - galaxy_1[0])
            for column in empty_columns:
                if min(galaxy_2[1], galaxy_1[1]) < column < max(galaxy_2[1], galaxy_1[1]):
                    distance += 1
            for line in empty_lines:
                if min(galaxy_2[0], galaxy_1[0]) < line < max(galaxy_2[0], galaxy_1[0]):
                    distance += 1
            total += distance
    print(f"Problem 1 result: {total}")


def problem_2():
    file_contents = read_file()
    total = 0
    galaxies = []
    matrix = []
    empty_lines = []
    empty_columns = []
    for x, line in enumerate(file_contents.splitlines()):
        matrix.append([char for char in line.strip()])
        if "#" in line:
            for y, char in enumerate(line):
                if char == "#":
                    galaxies.append([x, y])
        else:
            empty_lines.append(x)

    for index in range(len(matrix[0])):
        if all(x == "." for x in [matrix[i][index] for i in range(len(matrix))]):
            empty_columns.append(index)

    for galaxy_1_nr, galaxy_1 in enumerate(galaxies):
        for galaxy_2_nr, galaxy_2 in enumerate(galaxies):
            if galaxy_2_nr <= galaxy_1_nr:
                continue
            distance = abs(galaxy_2[1] - galaxy_1[1]) + abs(galaxy_2[0] - galaxy_1[0])
            for column in empty_columns:
                if min(galaxy_2[1], galaxy_1[1]) < column < max(galaxy_2[1], galaxy_1[1]):
                    distance += 999999
            for line in empty_lines:
                if min(galaxy_2[0], galaxy_1[0]) < line < max(galaxy_2[0], galaxy_1[0]):
                    distance += 999999
            total += distance
    print(f"Problem 2 result: {total}")


def run():
    print("Day 11")
    problem_1()
    problem_2()
