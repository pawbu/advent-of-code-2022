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

    items = [(line[:int((len(line)-1)/2)+1], line[int((len(line)-1)/2)+1:]) for line in lines]
    common_items = [set(list(i[0])) & set(list(i[1])) for i in items]

    alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    priorities = [alphabet.index(i.pop())+1 for i in common_items]
    print(f'Sum of the priorities of item types: {sum(priorities)}')


def test_day3_2():
    with open(f'{INPUT_DIR}/day3/input', encoding='utf-8') as f:
        lines = [line.strip() for line in f]

    common_items = []
    for i in range(0, len(lines), 3):
        common_items.append(set(list(lines[i])) & set(list(lines[i+1])) & set(list(lines[i+2])))

    alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    priorities = [alphabet.index(i.pop())+1 for i in common_items]
    print(f'Part two: Sum of the priorities of item types of each three-Elf group: {sum(priorities)}')
