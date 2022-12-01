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

