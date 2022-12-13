class DeviceVideoSystem:
    def __init__(self, instructions):
        self._x = 1
        self._cycle = 0
        self._instructions = instructions
        self._ip = 0
        self._running_instruction = None
        self._x_while_in_circle = 1
        self._crt = [['.'] * 40 for i in range(6)]
        self._crt_x, self._crt_y = 0, 0

    def _run_cycle(self):
        self._crt[self._crt_y][self._crt_x] = '#' if self._crt_x - 1 <= self._x <= self._crt_x + 1 else '.'
        if self._running_instruction is not None:
            if self._running_instruction[0] == "addx":
                self._x += int(self._running_instruction[1])
            else:
                raise Exception("trying to complete unknown instruction")
            self._running_instruction = None
        else:
            if self._ip < len(self._instructions):
                instruction = self._instructions[self._ip].strip().split()
                if instruction[0] == "noop":
                    pass
                elif instruction[0] == "addx":
                    self._running_instruction = instruction
                else:
                    raise Exception("trying to run unknown instruction")
                self._x_while_in_circle = self._x
                self._ip += 1
            else:
                return False

        self._crt_x += 1
        if self._crt_x == len(self._crt[0]):
            self._crt_x = 0
            self._crt_y += 1
            if self._crt_y == len(self._crt):
                self._crt_y = 0
        self._cycle += 1

        return True

    def run_n_cycles(self, n):
        keep_running = True
        i = 0
        while keep_running and i < n:
            keep_running = self._run_cycle()
            i += 1

    @property
    def x(self):
        return self._x

    @property
    def x_while_in_last_circle(self):
        return self._x_while_in_circle

    def print_crt(self):
        for row in self._crt:
            print("".join(row))


def main():
    f = open("day10.txt")
    lines = f.readlines()

    dvs = DeviceVideoSystem(lines)
    total_signal_strength = 0
    total_cycles = 0
    for i in [20, 40, 40, 40, 40, 40]:
        dvs.run_n_cycles(i)
        total_cycles += i
        total_signal_strength += total_cycles * dvs.x_while_in_last_circle
    print(total_signal_strength)

    dvs = DeviceVideoSystem(lines)
    dvs.run_n_cycles(len(lines) * 2 + 1)
    print()
    dvs.print_crt()


if __name__ == '__main__':
    main()
