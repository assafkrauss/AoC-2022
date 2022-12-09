class GameBoard:
    def __init__(self):
        self._head = (0, 0)
        self._tail = (0, 0)
        self._tail_track = set()
        self._tail_track.add(self._tail)

    def is_safe(self):
        return abs(self._head[0] - self._tail[0]) <= 1 and abs(self._head[1] - self._tail[1]) <= 1

    def step(self, direction):
        if direction == 'U':
            self._head = (self._head[0], self._head[1] + 1)
            if self.is_safe():
                return
            if self._head[1] - self._tail[1] == 2:
                self._tail = (self._tail[0], self._tail[1] + 1)
                if self._head[0] - self._tail[0] == 1:
                    self._tail = (self._tail[0] + 1, self._tail[1])
                elif self._head[0] - self._tail[0] == -1:
                    self._tail = (self._tail[0] - 1, self._tail[1])
        if direction == 'D':
            self._head = (self._head[0], self._head[1] - 1)
            if self.is_safe():
                return
            if self._head[1] - self._tail[1] == -2:
                self._tail = (self._tail[0], self._tail[1] - 1)
                if self._head[0] - self._tail[0] == 1:
                    self._tail = (self._tail[0] + 1, self._tail[1])
                elif self._head[0] - self._tail[0] == -1:
                    self._tail = (self._tail[0] - 1, self._tail[1])
        if direction == 'R':
            self._head = (self._head[0] + 1, self._head[1])
            if self.is_safe():
                return
            if self._head[0] - self._tail[0] == 2:
                self._tail = (self._tail[0] + 1, self._tail[1])
                if self._head[1] - self._tail[1] == 1:
                    self._tail = (self._tail[0], self._tail[1] + 1)
                elif self._head[1] - self._tail[1] == -1:
                    self._tail = (self._tail[0], self._tail[1] - 1)
        if direction == 'L':
            self._head = (self._head[0] - 1, self._head[1])
            if self.is_safe():
                return
            if self._head[0] - self._tail[0] == -2:
                self._tail = (self._tail[0] - 1, self._tail[1])
                if self._head[1] - self._tail[1] == 1:
                    self._tail = (self._tail[0], self._tail[1] + 1)
                elif self._head[1] - self._tail[1] == -1:
                    self._tail = (self._tail[0], self._tail[1] - 1)

        self._tail_track.add(self._tail)

    def count_tail_positions(self):
        return len(self._tail_track)


def main():
    f = open("day09.txt")
    lines = f.readlines()

    gm = GameBoard()
    for line in lines:
        [direction, n] = line.strip().split()
        for i in range(int(n)):
            gm.step(direction)
    print(gm.count_tail_positions())


if __name__ == '__main__':
    main()
