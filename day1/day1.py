def read_file():
    with open("day1/source.txt", "r") as file:
        return file.read()


valid_numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def problem_1():
    file_contents = read_file()
    total = 0
    for line in file_contents.splitlines():
        number = []
        for letter in line.strip():
            if letter.isdigit():
                number.append(letter)
        if number:
            total += int(number[0] + number[-1])
    print(f"Problem 1 result: {total}")


def problem_2():
    file_contents = read_file()
    total = 0
    for line in file_contents.splitlines():
        number = []
        for index, letter in enumerate(line):
            if letter.isdigit():
                number.append(
                    {
                        "index": index,
                        "value": letter
                    }
                )
            else:

                for key, value in valid_numbers.items():
                    if key in line[index:]:
                        if line[index:].index(key) + index == index:
                            number.append(
                                {
                                    "index": index,
                                    "value": value
                                }
                            )
        if number:
            number = sorted(number, key=lambda x: x.get("index"))
            total += int(number[0].get("value") + number[-1].get("value"))
    print(f"Problem 2 result: {total}")


def run():
    print("Day 1")
    problem_1()
    problem_2()