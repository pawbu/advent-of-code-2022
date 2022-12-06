import string

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
        move_from = int(numbers[1])-1
        move_to = int(numbers[2])-1
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
        move_from = int(numbers[1])-1
        move_to = int(numbers[2])-1
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
