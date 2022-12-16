import operator
from copy import copy, deepcopy
from functools import reduce
from typing import Callable


class Monkey:

    def __init__(self, starting_items: list[int], operation: Callable, test: Callable):
        starting_items.reverse()
        self.items: list = starting_items
        self.operation = operation
        self.test = test
        self.inspect_count = 0

    def turn(self):
        try:
            worry_level = self.items.pop()
            self.inspect_count += 1
            # Part two
            worry_level = self.operation(worry_level) % (3*11*7*2*19*5*17*13)
            # for test data
            # worry_level = self.operation(worry_level) % (23*19*13*17)

            # Part one
            # worry_level = self.operation(worry_level)
            # worry_level = math.floor(worry_level / 3)
            return self.test(worry_level), worry_level
        except IndexError:
            return None, None

    def catch_item(self, item):
        self.items.insert(0, item)

    def show_items(self):
        items = copy(self.items)
        items.reverse()
        print(items)

    def get_inspect_count(self):
        return self.inspect_count


monkeys_oryg = [
    # test data
    # Monkey([79, 98], lambda old: old * 19, lambda worry_level: 2 if worry_level % 23 == 0 else 3),
    # Monkey([54, 65, 75, 74], lambda old: old + 6, lambda worry_level: 2 if worry_level % 19 == 0 else 0),
    # Monkey([79, 60, 97], lambda old: old * old, lambda worry_level: 1 if worry_level % 13 == 0 else 3),
    # Monkey([74], lambda old: old + 3, lambda worry_level: 0 if worry_level % 17 == 0 else 1)
    Monkey([56, 56, 92, 65, 71, 61, 79], lambda old: old * 7, lambda worry_level: 3 if worry_level % 3 == 0 else 7),
    Monkey([61, 85], lambda old: old + 5, lambda worry_level: 6 if worry_level % 11 == 0 else 4),
    Monkey([54, 96, 82, 78, 69], lambda old: old * old, lambda worry_level: 0 if worry_level % 7 == 0 else 7),
    Monkey([57, 59, 65, 95], lambda old: old + 4, lambda worry_level: 5 if worry_level % 2 == 0 else 1),
    Monkey([62, 67, 80], lambda old: old * 17, lambda worry_level: 2 if worry_level % 19 == 0 else 6),
    Monkey([91], lambda old: old + 7, lambda worry_level: 1 if worry_level % 5 == 0 else 4),
    Monkey([79, 83, 64, 52, 77, 56, 63, 92], lambda old: old + 6, lambda worry_level: 2 if worry_level % 17 == 0 else 0),
    Monkey([50, 97, 76, 96, 80, 56], lambda old: old + 3, lambda worry_level: 3 if worry_level % 13 == 0 else 5),
]


def test_day11_1():
    monkeys = deepcopy(monkeys_oryg)
    for _ in range(0, 20):
        for monkey in monkeys:
            while True:
                receiver_monkey, worry_level = monkey.turn()
                if receiver_monkey is not None:
                    monkeys[receiver_monkey].catch_item(worry_level)
                else:
                    break

    level = reduce(operator.mul, sorted([monkey.get_inspect_count() for monkey in monkeys])[-2:])

    print(f'Inspect count: {[monkey.get_inspect_count() for monkey in monkeys]}')
    print(f'Monkey business level: {level}')


def test_day11_2():
    monkeys = deepcopy(monkeys_oryg)
    for _ in range(0, 10000):
        for monkey in monkeys:
            while True:
                receiver_monkey, worry_level = monkey.turn()
                if receiver_monkey is not None:
                    monkeys[receiver_monkey].catch_item(worry_level)
                else:
                    break

    level = reduce(operator.mul, sorted([monkey.get_inspect_count() for monkey in monkeys])[-2:])

    print(f'Part 2 Inspect count: {[monkey.get_inspect_count() for monkey in monkeys]}')
    print(f'Part 2 Monkey business level: {level}')
