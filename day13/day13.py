import copy


def read_file():
    with open("day13/source.txt", "r") as file:
        return file.read()


def problem_1():
    file_contents = read_file()
    total = 0
    maps = []
    ongoing_map = []

    for line in file_contents.splitlines():
        if line.strip() == "":
            maps.append(ongoing_map)
            ongoing_map = []
            continue
        ongoing_map.append([char for char in line.strip()])
    maps.append(ongoing_map)

    for map in maps:
        map_line_scores = []
        map_column_scores = []
        map_columns = len(map[0])
        for row in map:
            score = 0
            for index, char in enumerate(row):
                if char == "#":
                    score += 2 ** (index + 1)
            map_line_scores.append(score)

        for column_index in range(map_columns):
            score = 0
            for row_index in range(len(map)):
                if map[row_index][column_index] == "#":
                    score += 2 ** (row_index + 1)
            map_column_scores.append(score)

        for index, line_score in enumerate(map_line_scores):
            working = True
            if index == len(map) - 1:
                continue
            if map_line_scores[index + 1] == line_score:
                for i in range(1, min(index, len(map) - 1 - (index + 1)) + 1):
                    if map_line_scores[index - i] != map_line_scores[index + 1 + i]:
                        working = False
                        break
                if working:
                    total += (index + 1) * 100
                    print((index + 1) * 100)
                    break

        for index, column_score in enumerate(map_column_scores):
            working = True
            if index == map_columns - 1:
                continue
            if map_column_scores[index + 1] == column_score:
                for i in range(1, min(index, map_columns - 1 - (index + 1)) + 1):
                    if map_column_scores[index - i] != map_column_scores[index + 1 + i]:
                        working = False
                        break
                if working:
                    total += (index + 1)
                    print(index + 1)
                    break
    print(f"Problem 1 result: {total}")


def problem_2():
    file_contents = read_file()
    total = 0
    maps = []
    ongoing_map = []

    for line in file_contents.splitlines():
        if line.strip() == "":
            maps.append(ongoing_map)
            ongoing_map = []
            continue
        ongoing_map.append([char for char in line.strip()])
    maps.append(ongoing_map)

    for map in maps:
        score = 0
        map_line_scores = []
        map_column_scores = []
        map_columns = len(map[0])
        for row in map:
            score = 0
            for index, char in enumerate(row):
                if char == "#":
                    score += 2 ** (index + 1)
            map_line_scores.append(score)

        for column_index in range(map_columns):
            score = 0
            for row_index in range(len(map)):
                if map[row_index][column_index] == "#":
                    score += 2 ** (row_index + 1)
            map_column_scores.append(score)

        regular_total = 0
        for index, line_score in enumerate(map_line_scores):
            working = True
            if index == len(map) - 1:
                continue
            if map_line_scores[index + 1] == line_score:
                for i in range(1, min(index, len(map) - 1 - (index + 1)) + 1):
                    if map_line_scores[index - i] != map_line_scores[index + 1 + i]:
                        working = False
                        break
                if working:
                    regular_total = (index + 1) * 100
                    break

        for index, column_score in enumerate(map_column_scores):
            working = True
            if index == map_columns - 1:
                continue
            if map_column_scores[index + 1] == column_score:
                for i in range(1, min(index, map_columns - 1 - (index + 1)) + 1):
                    if map_column_scores[index - i] != map_column_scores[index + 1 + i]:
                        working = False
                        break
                if working:
                    regular_total = index + 1
                    print(index + 1)
                    break

        map_columns = len(map[0])
        working = False
        for i in range(len(map)):
            for j in range(map_columns):
                map_copy = copy.deepcopy(map)
                map_line_scores = []
                map_column_scores = []
                map_copy[i][j] = "." if map_copy[i][j] == "#" else "#"
                for row in map_copy:
                    score = 0
                    for index, char in enumerate(row):
                        if char == "#":
                            score += 2 ** (index + 1)
                    map_line_scores.append(score)

                for column_index in range(map_columns):
                    score = 0
                    for row_index in range(len(map)):
                        if map_copy[row_index][column_index] == "#":
                            score += 2 ** (row_index + 1)
                    map_column_scores.append(score)

                working = False
                for index, line_score in enumerate(map_line_scores):
                    working = True
                    if index == len(map) - 1:
                        continue
                    if map_line_scores[index + 1] == line_score:
                        for i in range(1, min(index,
                                              len(map) - 1 - (index + 1)) + 1):
                            if map_line_scores[index - i] != map_line_scores[index + 1 + i]:
                                working = False
                                break
                        if working:
                            if (index + 1) * 100 == regular_total:
                                working = False
                                break
                            total += (index + 1) * 100
                            print((index + 1) * 100)
                            for line in map_copy:
                                print(line)
                            print(map_line_scores)
                            print(regular_total)
                            break
                for index, column_score in enumerate(map_column_scores):
                    working = True
                    if index == map_columns - 1:
                        continue
                    if map_column_scores[index + 1] == column_score:
                        for i in range(1, min(index, map_columns - 1 - (index + 1)) + 1):
                            if map_column_scores[index - i] != map_column_scores[index + 1 + i]:
                                working = False
                                break
                        if working:
                            if index + 1 == regular_total:
                                working = False
                                break
                            total += (index + 1)
                            print(index + 1)
                            for line in map_copy:
                                print(line)
                            print(map_column_scores)
                            print(regular_total)
                            break
            if working:
                break

    print(f"Problem 2 result: {total}")


def run():
    print("Day 13")
    problem_1()
    problem_2()
