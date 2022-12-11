class Knot:
    def __init__(self, following):
        self._following = following
        self._follower = None
        if self._following is not None:
            self._id = following.id + 1
            self._x, self._y = self._following.x, self._following.y
        else:
            self._id = 0
            self._x, self._y = 0, 0
        self._track = set()
        self._track.add((self._x, self._y))

    @property
    def id(self):
        return self._id

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def follower(self):
        return self._follower

    @follower.setter
    def follower(self, f):
        self._follower = f

    def is_safe(self):
        if self._following is None:
            return True
        return abs(self._following.x - self._x) <= 1 and abs(self._following.y - self._y) <= 1

    def step(self, x_diff, y_diff):
        if self._following is not None:
            raise Exception("Can't freely move a non-head Know")
        self._x += x_diff
        self._y += y_diff

        self._track.add((self._x, self._y))
        if self._follower is not None:
            self._follower.follow()

    def follow(self):
        if self._following is None:
            raise Exception("No one to follow!")
        if not self.is_safe():
            diff_x, diff_y = self._following.x - self._x, self._following.y - self._y
            if diff_x > 0:
                self._x += 1
            elif diff_x < 0:
                self._x -= 1
            if diff_y > 0:
                self._y += 1
            elif diff_y < 0:
                self._y -= 1

        self._track.add((self._x, self._y))
        if self._follower is not None:
            self._follower.follow()

    def count_positions(self):
        return len(self._track)


def main():
    f = open("day09.txt")
    lines = f.readlines()

    for part in [2, 10]:
        head = Knot(None)
        curr = head
        for i in range(part - 1):
            temp = Knot(curr)
            curr.follower = temp
            curr = temp
        tail = curr

        for line in lines:
            [direction, n] = line.strip().split()
            for i in range(int(n)):
                if direction == 'U':
                    head.step(0, 1)
                elif direction == 'D':
                    head.step(0, -1)
                elif direction == 'R':
                    head.step(1, 0)
                elif direction == 'L':
                    head.step(-1, 0)
                else:
                    raise Exception("Unknown direction")
        print(tail.count_positions())


if __name__ == '__main__':
    main()
