class DeviceVideoSystem:
    def __init__(self, instructions):
        self._x = 1
        self._cycle = 0
        self._instructions = instructions
        self._ip = 0
        self._running_instruction = None
        self._x_while_in_circle = 1

    def _run_cycle(self):
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

        self._cycle += 1

    def run_n_cycles(self, n):
        for i in range(n):
            self._run_cycle()

    @property
    def x(self):
        return self._x

    @property
    def x_while_in_last_circle(self):
        return self._x_while_in_circle


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


if __name__ == '__main__':
    main()
