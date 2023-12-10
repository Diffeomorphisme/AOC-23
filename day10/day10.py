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
    print(start)
    print(starting_branches)

    next_point = starting_branches
    histories = [[start], [start]]
    i = 1
    while True:
        for index, branch in enumerate(starting_branches):
            current_point = next_point[index]
            (above, under, left, right) = get_surroundings(current_point, len_matrix, row_length)
            history = histories[index]
            point = matrix[current_point[0]][current_point[1]]
            if point == "-":
                if left not in history:
                    next_point[index] = left
                    histories[index].append(current_point)
                    continue
                if right not in history:
                    next_point[index] = right
                    histories[index].append(current_point)
                    continue
            elif point == "|":
                if above not in history:
                    next_point[index] = above
                    histories[index].append(current_point)
                    continue
                if under not in history:
                    next_point[index] = under
                    histories[index].append(current_point)
                    continue
            elif point == "7":
                if left not in history:
                    next_point[index] = left
                    histories[index].append(current_point)
                    continue
                if under not in history:
                    next_point[index] = under
                    histories[index].append(current_point)
                    continue
            elif point == "J":
                if above not in history:
                    next_point[index] = above
                    histories[index].append(current_point)
                    continue
                if left not in history:
                    next_point[index] = left
                    histories[index].append(current_point)
                    continue
            elif point == "L":
                if above not in history:
                    next_point[index] = above
                    histories[index].append(current_point)
                    continue
                if right not in history:
                    next_point[index] = right
                    histories[index].append(current_point)
                    continue
            elif point == "F":
                if under not in history:
                    next_point[index] = under
                    histories[index].append(current_point)
                    continue
                if right not in history:
                    next_point[index] = right
                    histories[index].append(current_point)
                    continue
        i += 1
        if next_point[0] == next_point[1]:
            break
    total = i
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

    above_start, under_start, left_of_start, right_of_start = get_surroundings(start, len_matrix, row_length)
    if matrix[left_of_start[0]][left_of_start[1]] in to_the_left:
        starting_branches.append(left_of_start)
    if matrix[right_of_start[0]][right_of_start[1]] in to_the_right:
        starting_branches.append(right_of_start)
    if matrix[above_start[0]][above_start[1]] in up:
        starting_branches.append(above_start)
    if matrix[under_start[0]][under_start[1]] in down:
        starting_branches.append(under_start)
    print(start)
    print(starting_branches)

    next_point = starting_branches
    histories = [[start], [start]]
    i = 1
    while True:
        for index, branch in enumerate(starting_branches):
            current_point = next_point[index]
            (above, under, left, right) = get_surroundings(current_point, len_matrix, row_length)
            history = histories[index]
            point = matrix[current_point[0]][current_point[1]]
            if point == "-":
                if left not in history:
                    next_point[index] = left
                    histories[index].append(current_point)
                    continue
                if right not in history:
                    next_point[index] = right
                    histories[index].append(current_point)
                    continue
            elif point == "|":
                if above not in history:
                    next_point[index] = above
                    histories[index].append(current_point)
                    continue
                if under not in history:
                    next_point[index] = under
                    histories[index].append(current_point)
                    continue
            elif point == "7":
                if left not in history:
                    next_point[index] = left
                    histories[index].append(current_point)
                    continue
                if under not in history:
                    next_point[index] = under
                    histories[index].append(current_point)
                    continue
            elif point == "J":
                if above not in history:
                    next_point[index] = above
                    histories[index].append(current_point)
                    continue
                if left not in history:
                    next_point[index] = left
                    histories[index].append(current_point)
                    continue
            elif point == "L":
                if above not in history:
                    next_point[index] = above
                    histories[index].append(current_point)
                    continue
                if right not in history:
                    next_point[index] = right
                    histories[index].append(current_point)
                    continue
            elif point == "F":
                if under not in history:
                    next_point[index] = under
                    histories[index].append(current_point)
                    continue
                if right not in history:
                    next_point[index] = right
                    histories[index].append(current_point)
                    continue
        i += 1
        if next_point[0] == next_point[1]:
            break

    network = []
    for hist in histories:
        for i in range(len(hist)):
            network.append(hist[i])
    candidates = [[x, y] for y in range(row_length) for x in range(len_matrix) if [x, y] not in network]
    outside = []
    print(candidates)
    new_candidates = []
    

    total = 0
    print(f"Problem 2 result: {total}")


def run():
    print("Day 10")
    problem_1()
    problem_2()