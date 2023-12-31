from copy import deepcopy


def read_file():
    with open("day10/source.txt", "r") as file:
        return file.read()


def get_surroundings(point, len_matrix, row_length):
    above = [max(point[0] - 1, 0), point[1]]
    under = [min(point[0] + 1, len_matrix), point[1]]
    left = [point[0], max(point[1] - 1, 0)]
    right = [point[0], min(point[1] + 1, row_length)]
    return above, under, left, right


def problem_1():
    file_contents = read_file()
    matrix = []
    row_length = 0
    start = []
    starting_branches = []
    to_the_right = {"-", "7", "J"}
    to_the_left = {"-", "L", "F"}
    up = {"|", "7", "F"}
    down = {"|", "J", "L"}
    for line in file_contents.splitlines():
        matrix.append([char for char in line.strip()])

    for index, row in enumerate(matrix):
        if "S" in row:
            start = [index, row.index("S")]
            row_length = len(row)
    len_matrix = len(matrix)

    above_start, under_start, left_of_start, right_of_start = get_surroundings(start, len_matrix, row_length)
    if matrix[left_of_start[0]][left_of_start[1]] in to_the_left:
        starting_branches.append(left_of_start)
    if matrix[right_of_start[0]][right_of_start[1]] in to_the_right:
        starting_branches.append(right_of_start)
    if matrix[above_start[0]][above_start[1]] in up:
        starting_branches.append(above_start)
    if matrix[under_start[0]][under_start[1]] in down:
        starting_branches.append(under_start)

    starting_branch = starting_branches[0]
    next_point = starting_branch
    history = [start]
    i = 1
    while True:
        current_point = next_point
        (above, under, left, right) = get_surroundings(current_point, len_matrix, row_length)
        point = matrix[current_point[0]][current_point[1]]
        if point == "-":
            if left not in history:
                next_point = left
            if right not in history:
                next_point = right
            history.append(current_point)
        elif point == "|":
            if above not in history:
                next_point = above
            if under not in history:
                next_point = under
            history.append(current_point)
        elif point == "7":
            if left not in history:
                next_point = left
            if under not in history:
                next_point = under
            history.append(current_point)
        elif point == "J":
            if above not in history:
                next_point = above
            if left not in history:
                next_point = left
            history.append(current_point)
        elif point == "L":
            if above not in history:
                next_point = above
            if right not in history:
                next_point = right
            history.append(current_point)
        elif point == "F":
            if under not in history:
                next_point = under
            if right not in history:
                next_point = right
            history.append(current_point)
        i += 1
        if next_point == starting_branches[1]:
            i += 1
            break
    total = i // 2
    print(f"Problem 1 result: {total}")


def problem_2():
    file_contents = read_file()
    matrix = []
    row_length = 0
    start = []
    starting_branches = []
    to_the_right = {"-", "7", "J"}
    to_the_left = {"-", "L", "F"}
    up = {"|", "7", "F"}
    down = {"|", "J", "L"}
    for line in file_contents.splitlines():
        matrix.append([char for char in line.strip()])

    for index, row in enumerate(matrix):
        if "S" in row:
            start = [index, row.index("S")]
            row_length = len(row)
    len_matrix = len(matrix)

    _up = False
    _down = False
    _left = False
    _right = False
    above_start, under_start, left_of_start, right_of_start = get_surroundings(start, len_matrix, row_length)
    if matrix[left_of_start[0]][left_of_start[1]] in to_the_left:
        starting_branches.append(left_of_start)
        _left = True
    if matrix[right_of_start[0]][right_of_start[1]] in to_the_right:
        starting_branches.append(right_of_start)
        _right = True
    if matrix[above_start[0]][above_start[1]] in up:
        starting_branches.append(above_start)
        _up = True
    if matrix[under_start[0]][under_start[1]] in down:
        starting_branches.append(under_start)
        _down = True

    if _left and _right:
        matrix[start[0]][start[1]] = "-"
    if _left and _up:
        matrix[start[0]][start[1]] = "J"
    if _left and _down:
        matrix[start[0]][start[1]] = "7"
    if _up and _down:
        matrix[start[0]][start[1]] = "|"
    if _up and _right:
        matrix[start[0]][start[1]] = "L"
    if _down and _right:
        matrix[start[0]][start[1]] = "F"

    starting_branch = starting_branches[0]
    next_point = starting_branch
    history = [start]
    i = 1
    while True:
        current_point = next_point
        (above, under, left, right) = get_surroundings(current_point, len_matrix, row_length)
        point = matrix[current_point[0]][current_point[1]]
        if point == "-":
            if left not in history:
                next_point = left
            if right not in history:
                next_point = right
            history.append(current_point)
        elif point == "|":
            if above not in history:
                next_point = above
            if under not in history:
                next_point = under
            history.append(current_point)
        elif point == "7":
            if left not in history:
                next_point = left
            if under not in history:
                next_point = under
            history.append(current_point)
        elif point == "J":
            if above not in history:
                next_point = above
            if left not in history:
                next_point = left
            history.append(current_point)
        elif point == "L":
            if above not in history:
                next_point = above
            if right not in history:
                next_point = right
            history.append(current_point)
        elif point == "F":
            if under not in history:
                next_point = under
            if right not in history:
                next_point = right
            history.append(current_point)
        i += 1
        if next_point == starting_branches[1]:
            i += 1
            history.append(next_point)
            break

    network = history

    pairs = [["L", "J"], ["F", "7"]]
    total = 0
    for row_index, row in enumerate(matrix):
        outside = True
        ongoing_pair = []
        for column_index, column in enumerate(row):
            if [row_index, column_index] in network:
                on_network = True
            else:
                on_network = False

            if matrix[row_index][column_index] == "|" and on_network:
                outside = False if outside else True

            if ongoing_pair:
                if matrix[row_index][column_index] in ongoing_pair and on_network:
                    outside = False if outside else True
            else:
                for pair in pairs:
                    if matrix[row_index][column_index] in pair and on_network:
                        ongoing_pair = pair
                        outside = False if outside else True
                        break

            if not outside and not on_network:
                total += 1
    print(f"Problem 2 result: {total}")


def run():
    print("Day 10")
    problem_1()
    problem_2()
