day11_input = {
    "monkeys": {
        0: {"items": [85, 79, 63, 72],
            "worry_up_func": lambda w: w * 17,
            "test": lambda w: w % 2 == 0,
            "target_if_true": 2,
            "target_if_false": 6
            },
        1: {"items": [53, 94, 65, 81, 93, 73, 57, 92],
            "worry_up_func": lambda w: w * w,
            "test": lambda w: w % 7 == 0,
            "target_if_true": 0,
            "target_if_false": 2
            },
        2: {"items": [62, 63],
            "worry_up_func": lambda w: w + 7,
            "test": lambda w: w % 13 == 0,
            "target_if_true": 7,
            "target_if_false": 6
            },
        3: {"items": [57, 92, 56],
            "worry_up_func": lambda w: w + 4,
            "test": lambda w: w % 5 == 0,
            "target_if_true": 4,
            "target_if_false": 5
            },
        4: {"items": [67],
            "worry_up_func": lambda w: w + 5,
            "test": lambda w: w % 3 == 0,
            "target_if_true": 1,
            "target_if_false": 5
            },
        5: {"items": [85, 56, 66, 72, 57, 99],
            "worry_up_func": lambda w: w + 6,
            "test": lambda w: w % 19 == 0,
            "target_if_true": 1,
            "target_if_false": 0
            },
        6: {"items": [86, 65, 98, 97, 69],
            "worry_up_func": lambda w: w * 13,
            "test": lambda w: w % 11 == 0,
            "target_if_true": 3,
            "target_if_false": 7
            },
        7: {"items": [87, 68, 92, 66, 91, 50, 68],
            "worry_up_func": lambda w: w + 2,
            "test": lambda w: w % 17 == 0,
            "target_if_true": 4,
            "target_if_false": 3
            }
    },
    "worry_down_func": {
        1: lambda w: w // 3,
        2: lambda w: w % (2 * 7 * 13 * 5 * 3 * 19 * 11 * 17)
    },
    "rounds": {
        1: 20,
        2: 10000
    }
}


class Monkey:
    def __init__(self, pack, items, worry_up_func, worry_down_func, test, target_if_true, target_if_false):
        self._pack = pack
        self._items = items
        self._worry_up_func = worry_up_func
        self._worry_down_func = worry_down_func
        self._test = test
        self._target_if_true = target_if_true
        self._target_if_false = target_if_false
        self._inspections = 0

    def add_item(self, item):
        self._items.append(item)

    def turn(self):
        self._inspections += len(self._items)
        for i in range(len(self._items)):
            self._items[i] = self._worry_up_func(self._items[i])
            self._items[i] = self._worry_down_func(self._items[i])
            if self._test(self._items[i]):
                self._pack[self._target_if_true].add_item(self._items[i])
            else:
                self._pack[self._target_if_false].add_item(self._items[i])
        self._items = []

    @property
    def inspections(self):
        return self._inspections


def main():
    for part in [1, 2]:
        monkey_pack = []
        for i in day11_input["monkeys"].keys():
            monkey_pack.append(Monkey(monkey_pack, day11_input["monkeys"][i]["items"][:],
                                      day11_input["monkeys"][i]["worry_up_func"],
                                      day11_input["worry_down_func"][part],
                                      day11_input["monkeys"][i]["test"],
                                      day11_input["monkeys"][i]["target_if_true"],
                                      day11_input["monkeys"][i]["target_if_false"]))

        for r in range(day11_input["rounds"][part]):
            for i in range(len(monkey_pack)):
                monkey_pack[i].turn()

        most_active_1, most_active_2 = 0, 0
        for monkey in monkey_pack:
            inspections = monkey.inspections
            if inspections > most_active_1:
                most_active_2 = most_active_1
                most_active_1 = inspections
            elif inspections > most_active_2:
                most_active_2 = inspections
        monkey_business = most_active_1 * most_active_2
        print(monkey_business)


if __name__ == '__main__':
    main()
