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
