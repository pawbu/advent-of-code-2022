import os
import string
from pathlib import Path

INPUT_DIR = 'tests/input'


def test_day1_1():
    with open(f'{INPUT_DIR}/day1/input.txt', encoding='utf-8') as f:
        current_max = 0
        calories = 0
        for line in f:
            if line == '\n':
                current_max = max(current_max, calories)
                calories = 0
            else:
                calories += int(line.strip())
        print(f'Max calories: {current_max}')


def test_day1_2():
    with open(f'{INPUT_DIR}/day1/input.txt', encoding='utf-8') as f:
        lines = [line.strip() for line in f]

    all_elves = []
    calories = 0
    for line in lines:
        if line == '':
            all_elves.append(calories)
            calories = 0
        else:
            calories += int(line)
    all_elves.sort()
    top_three = sum(all_elves[-3:])
    print(f'Top three: {top_three}')


def test_day2_1():
    with open(f'{INPUT_DIR}/day2/input', encoding='utf-8') as f:
        lines = [line.strip() for line in f]

    # X=1, Y=2, Z=3
    # A,X=Rock, B,Y=Paper, C,Z=Scissors
    GAME_TO_SCORE = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6,
    }

    results = [GAME_TO_SCORE[round] for round in lines]
    print(f'Total score according to strategy: {sum(results)}')


def test_day2_2():
    with open(f'{INPUT_DIR}/day2/input', encoding='utf-8') as f:
        lines = [line.strip() for line in f]

    # Rock=1, Paper=2, Scissors=3
    # A=Rock, B=Paper, C=Scissors
    # X=lose, Y=draw, Z=win
    GAME_TO_SCORE = {
        'A X': 3,
        'A Y': 4,
        'A Z': 8,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 2,
        'C Y': 6,
        'C Z': 7,
    }

    results = [GAME_TO_SCORE[round] for round in lines]
    print(f'Total score according to new strategy: {sum(results)}')


def test_day3_1():
    with open(f'{INPUT_DIR}/day3/input', encoding='utf-8') as f:
        lines = [line.strip() for line in f]

    items = [(line[:int((len(line) - 1) / 2) + 1], line[int((len(line) - 1) / 2) + 1:]) for line in lines]
    common_items = [set(list(i[0])) & set(list(i[1])) for i in items]

    alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    priorities = [alphabet.index(i.pop()) + 1 for i in common_items]
    print(f'Sum of the priorities of item types: {sum(priorities)}')


def test_day3_2():
    with open(f'{INPUT_DIR}/day3/input', encoding='utf-8') as f:
        lines = [line.strip() for line in f]

    common_items = []
    for i in range(0, len(lines), 3):
        common_items.append(set(list(lines[i])) & set(list(lines[i + 1])) & set(list(lines[i + 2])))

    alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    priorities = [alphabet.index(i.pop()) + 1 for i in common_items]
    print(f'Part two: Sum of the priorities of item types of each three-Elf group: {sum(priorities)}')


def test_day4_1():
    with open(f'{INPUT_DIR}/day4/input', encoding='utf-8') as f:
        lines = [line.strip() for line in f]

    elf_pairs = [l.split(',') for l in lines]
    elf_ranges = [(pair[0].split('-'), pair[1].split('-')) for pair in elf_pairs]
    elf_ranges_enumerated = [
        (
            list(range(int(pair[0][0]), int(pair[0][1]) + 1)),
            list(range(int(pair[1][0]), int(pair[1][1]) + 1))
        )
        for pair in elf_ranges
    ]
    elf_ranges_sets = [
        (set(pair[0]), set(pair[1]))
        for pair in elf_ranges_enumerated
    ]
    count = [
        1
        for pair in elf_ranges_sets
        if len(pair[0] - pair[1]) == 0 or len(pair[1] - pair[0]) == 0
    ]

    print(f'Assignment pairs meeting condition: {sum(count)}')


def test_day4_2():
    with open(f'{INPUT_DIR}/day4/input', encoding='utf-8') as f:
        lines = [line.strip() for line in f]

    elf_pairs = [l.split(',') for l in lines]
    elf_ranges = [(pair[0].split('-'), pair[1].split('-')) for pair in elf_pairs]
    elf_ranges_enumerated = [
        (
            list(range(int(pair[0][0]), int(pair[0][1]) + 1)),
            list(range(int(pair[1][0]), int(pair[1][1]) + 1))
        )
        for pair in elf_ranges
    ]
    elf_ranges_sets = [
        (set(pair[0]), set(pair[1]))
        for pair in elf_ranges_enumerated
    ]
    count = [
        1
        for pair in elf_ranges_sets
        if len(pair[0].intersection(pair[1])) > 0
    ]

    print(f'Assignment pairs where ranges overlap: {sum(count)}')


def test_day5_1():
    with open(f'{INPUT_DIR}/day5/input', encoding='utf-8') as f:
        lines = [line.strip() for line in f]

    lines = lines[10:]
    stacks = [
        ['V', 'C', 'D', 'R', 'Z', 'G', 'B', 'W'],
        ['G', 'W', 'F', 'C', 'B', 'S', 'T', 'V'],
        ['C', 'B', 'S', 'N', 'W'],
        ['Q', 'G', 'M', 'N', 'J', 'V', 'C', 'P'],
        ['T', 'S', 'L', 'F', 'D', 'H', 'B'],
        ['J', 'V', 'T', 'W', 'M', 'N'],
        ['P', 'F', 'L', 'C', 'S', 'T', 'G'],
        ['B', 'D', 'Z'],
        ['M', 'N', 'Z', 'W']
    ]

    for line in lines:
        numbers = [n for n in line.split(' ') if n.isdigit()]
        quantity = int(numbers[0])
        move_from = int(numbers[1]) - 1
        move_to = int(numbers[2]) - 1
        for x in range(0, quantity):
            crate = stacks[move_from].pop()
            stacks[move_to].append(crate)

    result = [stack.pop() for stack in stacks]
    print(f'Crates on top: {"".join(result)}')


def test_day5_2():
    with open(f'{INPUT_DIR}/day5/input', encoding='utf-8') as f:
        lines = [line.strip() for line in f]

    lines = lines[10:]
    stacks = [
        ['V', 'C', 'D', 'R', 'Z', 'G', 'B', 'W'],
        ['G', 'W', 'F', 'C', 'B', 'S', 'T', 'V'],
        ['C', 'B', 'S', 'N', 'W'],
        ['Q', 'G', 'M', 'N', 'J', 'V', 'C', 'P'],
        ['T', 'S', 'L', 'F', 'D', 'H', 'B'],
        ['J', 'V', 'T', 'W', 'M', 'N'],
        ['P', 'F', 'L', 'C', 'S', 'T', 'G'],
        ['B', 'D', 'Z'],
        ['M', 'N', 'Z', 'W']
    ]

    for line in lines:
        numbers = [n for n in line.split(' ') if n.isdigit()]
        quantity = int(numbers[0])
        move_from = int(numbers[1]) - 1
        move_to = int(numbers[2]) - 1
        crates = stacks[move_from][-quantity:]
        del stacks[move_from][-quantity:]
        stacks[move_to] = stacks[move_to] + crates

    result = [stack.pop() for stack in stacks]
    print(f'Crates on top by CrateMover 9001: {"".join(result)}')


def test_day6_1():
    with open(f'{INPUT_DIR}/day6/input', encoding='utf-8') as f:
        input = f.read()

    buffer = []
    for index, i in enumerate(input):
        if len(set(buffer[-4:])) == 4:
            print(f'First start-of-packet marker detected after {index}')
            break
        buffer += i


def test_day6_2():
    with open(f'{INPUT_DIR}/day6/input', encoding='utf-8') as f:
        input = f.read()

    buffer = []
    for index, i in enumerate(input):
        if len(set(buffer[-14:])) == 14:
            print(f'First start-of-message marker detected after {index}')
            break
        buffer += i


# def test_day7():
#     with open(f'{INPUT_DIR}/day7/input', encoding='utf-8') as f:
#         lines = [line.strip() for line in f]
#
#     def is_command(line):
#         return line.startswith('$')
#
#     def get_size(start_path):
#         total_size = 0
#         for dirpath, dirnames, filenames in os.walk(start_path):
#             for f in filenames:
#                 fp = os.path.join(dirpath, f)
#                 total_size += os.path.getsize(fp)
#
#         return total_size
#
#     i = 1
#     path = Path('./tests/my_root')
#     path.mkdir()
#     dirs = [path]
#     while i < len(lines):
#         line = lines[i]
#         if is_command(line):
#             if 'cd ..' in line:
#                 path = path.parent
#             if 'cd ' in line and 'cd ..' not in line:
#                 path = path / (line.split(' ')[2])
#             if 'ls' in line:
#                 i += 1
#                 line = lines[i]
#                 while not is_command(line):
#                     if 'dir ' in line:
#                         p: Path = (path / line.split(' ')[1])
#                         p.mkdir()
#                         dirs.append(p)
#                     else:
#                         (size, file_name) = line.split(' ')
#                         with open(path / file_name, 'wb') as f:
#                             f.write(bytearray(int(size)))
#                     i += 1
#                     if i == 934:
#                         break
#                     line = lines[i]
#                 i -= 1
#         i += 1
#
#     result = [get_size(dir) for dir in dirs if get_size(dir) <= 100000]
#     print(f'Part 1: the sum of the total sizes of those directories: {sum(result)}')
#
#     total_size_outermost_dir = get_size(Path('./tests/my_root'))
#     free_space_now = 70000000 - total_size_outermost_dir
#     free_space_needed = 30000000 - free_space_now
#     result = [(dir, get_size(dir)) for dir in dirs if get_size(dir) >= free_space_needed]
#
#     print(f'Part 2: the sum of the total sizes of those directories: {min(result,key=lambda item:item[1])}')


def test_day8_1():
    with open(f'{INPUT_DIR}/day8/input', encoding='utf-8') as f:
        lines = [line.strip() for line in f]

    trees = [[int(height) for height in list(line)] for line in lines]
    # print(trees)
    max_y = len(trees)-1
    max_x = len(trees)-1

    def visible_north(y, x):
        i = y-1
        while i >= 0:
            if trees[x][i] >= trees[x][y]:
                return False
            i -= 1
        return True

    def visible_south(y, x):
        i = y+1
        while i <= max_y:
            if trees[x][i] >= trees[x][y]:
                return False
            i += 1
        return True

    def visible_east(y, x):
        i = x+1
        while i <= max_x:
            if trees[i][y] >= trees[x][y]:
                return False
            i += 1
        return True

    def visible_west(y, x):
        i = x-1
        while i >= 0:
            if trees[i][y] >= trees[x][y]:
                return False
            i -= 1
        return True

    def is_visible(y, x):
        result = None
        if visible_north(y, x) or visible_south(y, x) \
                or visible_east(y, x) or visible_west(y, x):
            result = True
        else:
            result = False

        # print(f'y{y}x{x} height: {trees[y][x]}, visible: {result}')
        return result

    visible_trees = len(trees[0]) * 2 - 4 + len(trees) * 2

    for y in range(1, len(trees)-1):
        for x in range(1, len(trees[y])-1):
            if is_visible(y, x):
                visible_trees += 1
    print(f"Trees visible from outside the grid: {visible_trees}")


def test_day8_2():
    with open(f'{INPUT_DIR}/day8/input', encoding='utf-8') as f:
        lines = [line.strip() for line in f]

    trees = [[int(height) for height in list(line)] for line in lines]
    max_y = len(trees)-1
    max_x = len(trees)-1

    def trees_north(y, x):
        i = y-1
        counter = 0
        while i >= 0:
            if trees[i][x] < trees[y][x]:
                counter += 1
            if trees[i][x] >= trees[y][x]:
                counter += 1
                return counter
            i -= 1
        return 1 if counter == 0 else counter

    def trees_south(y, x):
        i = y+1
        counter = 0
        while i <= max_y:
            if trees[i][x] < trees[y][x]:
                counter += 1
            if trees[i][x] >= trees[y][x]:
                counter += 1
                return counter
            i += 1
        return 1 if counter == 0 else counter

    def trees_east(y, x):
        i = x+1
        counter = 0
        while i <= max_x:
            if trees[y][i] < trees[y][x]:
                counter += 1
            if trees[y][i] >= trees[y][x]:
                counter += 1
                return counter
            i += 1
        return 1 if counter == 0 else counter

    def trees_west(y, x):
        i = x-1
        counter = 0
        while i >= 0:
            if trees[y][i] < trees[y][x]:
                counter += 1
            if trees[y][i] >= trees[y][x]:
                counter += 1
                return counter
            i -= 1
        return 1 if counter == 0 else counter

    def count_scenic_score(y, x):
        score = trees_north(y, x) * trees_south(y, x) * trees_east(y, x) * trees_west(y, x)
        return score

    highest_scenic_score = 0
    for y in range(1, len(trees)-1):
        for x in range(1, len(trees[y])-1):
            highest_scenic_score = max(highest_scenic_score, count_scenic_score(y, x))

    print(f"Tree with highest scenic score: {highest_scenic_score}")


def test_day10_1():
    with open(f'{INPUT_DIR}/day10/input', encoding='utf-8') as f:
        instructions = [line.strip() for line in f]

    cycle_no = 1
    instr_no = 0
    x = 1
    cycle_to_x = {}

    while instr_no < len(instructions):
        instruction = instructions[instr_no]

        if instruction == 'noop':
            cycle_to_x[cycle_no] = x
            cycle_no += 1
            instr_no += 1
        else:
            cycle_to_x[cycle_no] = x
            cycle_no += 1
            cycle_to_x[cycle_no] = x
            x += int(instruction.split(' ')[1])
            cycle_no += 1
            instr_no += 1

    sum = cycle_to_x[20]*20 + cycle_to_x[60]*60 + cycle_to_x[100]*100 + cycle_to_x[140]*140 \
        + cycle_to_x[180]*180 + cycle_to_x[220]*220
    print(f'Sum of six signal strengths: {sum}')


def test_day10_2():
    with open(f'{INPUT_DIR}/day10/input', encoding='utf-8') as f:
        instructions = [line.strip() for line in f]

    cycle_no = 1
    instr_no = 0
    x = 1
    cycle_to_x = {}
    crt_row = []

    def print_crt_row(crt_row, cycle_no, x):
        if ((cycle_no-1) % 40) in list(range(x - 1, x + 2)):
            crt_row.append("#")
        else:
            crt_row.append(".")

    while instr_no < len(instructions):
        print_crt_row(crt_row, cycle_no, x)

        instruction = instructions[instr_no]

        if instruction == 'noop':
            cycle_to_x[cycle_no] = x
            cycle_no += 1
            instr_no += 1
        else:
            cycle_to_x[cycle_no] = x
            cycle_no += 1
            cycle_to_x[cycle_no] = x
            print_crt_row(crt_row, cycle_no, x)
            x += int(instruction.split(' ')[1])
            cycle_no += 1
            instr_no += 1

    print("".join(crt_row[0:40]))
    print("".join(crt_row[40:80]))
    print("".join(crt_row[80:120]))
    print("".join(crt_row[120:160]))
    print("".join(crt_row[160:200]))
    print("".join(crt_row[200:240]))
    # EKRHEPUZ
