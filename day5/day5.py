import re


def read_file():
    with open("day4/source.txt", "r") as file:
        return file.read()


headings = [
    "seed-to-soil map:",
    "soil-to-fertilizer map:",
    "fertilizer-to-water map:",
    "water-to-light map:",
    "light-to-temperature map:",
    "temperature-to-humidity map:",
    "humidity-to-location map:",
]


maps = {
    headings[0]: [],
    headings[1]: [],
    headings[2]: [],
    headings[3]: [],
    headings[4]: [],
    headings[5]: [],
    headings[6]: [],
}


def problem_1():
    file_contents = read_file()
    total = 0
    seeds = []
    current_map_key = headings[0]
    for line in file_contents.splitlines():
        if "seeds" in line:
            seeds = [int(seed) for seed in re.findall(r"[0-9]+", line.split("seeds")[-1])]
            continue
        for key, value in maps.items():
            if key in line:
                current_map_key = key
                break
        numbers = [int(seed) for seed in re.findall(r"[0-9]+", line)]
        if numbers:
            maps[current_map_key].append(numbers)
    for seed in seeds:
        for heading in headings:
            for _range in maps[heading]:
                if _range[1] <= seed < _range[1] + _range[2]:
                    seed = seed - _range[1] + _range[0]
                    break
        total = min(total, seed) if total != 0 else seed
    print(f"Problem 1 result: {total}")


def problem_2():
    file_contents = read_file()
    seeds = []
    current_map_key = headings[0]
    for line in file_contents.splitlines():
        if "seeds" in line:
            seeds = [int(seed) for seed in
                     re.findall(r"[0-9]+", line.split("seeds")[-1])]
            continue
        for key, value in maps.items():
            if key in line:
                current_map_key = key
                break
        numbers = [int(seed) for seed in re.findall(r"[0-9]+", line)]
        if numbers:
            maps[current_map_key].append(numbers)

    i = 130000000
    min_found = False
    while True:

        seed = i
        for heading in headings[::-1]:
            for _range in maps[heading]:
                if _range[0] <= seed < _range[0] + _range[2]:
                    seed = seed - _range[0] + _range[1]
                    break
        for index, start_seed in enumerate(seeds):
            if index % 2 == 0:
                if start_seed <= seed <= start_seed + seeds[index + 1]:
                    min_found = True
                    break
        if min_found:
            break
        i += 1
    total = i
    print(f"Problem 2 result: {total}")


def run():
    print("Day 5")
    problem_1()
    problem_2()
