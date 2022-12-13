class Monkey:
    def __init__(self, pack, items, worry_func, test, target_if_true, target_if_false):
        self._pack = pack
        self._items = items
        self._worry_func = worry_func
        self._test = test
        self._target_if_true = target_if_true
        self._target_if_false = target_if_false
        self._inspections = 0

    def add_item(self, item):
        self._items.append(item)

    def turn(self):
        self._inspections += len(self._items)
        for i in range(len(self._items)):
            self._items[i] = self._worry_func(self._items[i])
            self._items[i] //= 3
            if self._test(self._items[i]):
                self._pack[self._target_if_true].add_item(self._items[i])
            else:
                self._pack[self._target_if_false].add_item(self._items[i])
        self._items = []

    @property
    def inspections(self):
        return self._inspections


def main():
    # noinspection PyListCreation
    monkey_pack = []
    # monkey_pack.append(Monkey(monkey_pack, [79, 98], lambda w: w * 19, lambda w: w % 23 == 0, 2, 3))
    # monkey_pack.append(Monkey(monkey_pack, [54, 65, 75, 74], lambda w: w + 6, lambda w: w % 19 == 0, 2, 0))
    # monkey_pack.append(Monkey(monkey_pack, [79, 60, 97], lambda w: w * w, lambda w: w % 13 == 0, 1, 3))
    # monkey_pack.append(Monkey(monkey_pack, [74], lambda w: w + 3, lambda w: w % 17 == 0, 0, 1))
    monkey_pack.append(Monkey(monkey_pack, [85, 79, 63, 72], lambda w: w * 17, lambda w: w % 2 == 0, 2, 6))
    monkey_pack.append(Monkey(monkey_pack, [53, 94, 65, 81, 93, 73, 57, 92], lambda w: w * w,
                              lambda w: w % 7 == 0, 0, 2))
    monkey_pack.append(Monkey(monkey_pack, [62, 63], lambda w: w + 7, lambda w: w % 13 == 0, 7, 6))
    monkey_pack.append(Monkey(monkey_pack, [57, 92, 56], lambda w: w + 4, lambda w: w % 5 == 0, 4, 5))
    monkey_pack.append(Monkey(monkey_pack, [67], lambda w: w + 5, lambda w: w % 3 == 0, 1, 5))
    monkey_pack.append(Monkey(monkey_pack, [85, 56, 66, 72, 57, 99], lambda w: w + 6, lambda w: w % 19 == 0, 1, 0))
    monkey_pack.append(Monkey(monkey_pack, [86, 65, 98, 97, 69], lambda w: w * 13, lambda w: w % 11 == 0, 3, 7))
    monkey_pack.append(Monkey(monkey_pack, [87, 68, 92, 66, 91, 50, 68], lambda w: w + 2, lambda w: w % 17 == 0, 4, 3))

    for r in range(20):
        for monkey in monkey_pack:
            monkey.turn()

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
