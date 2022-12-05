from collections import deque


def parse_crate_stacks(lines):
    stacks = [0]

    index_line = 0
    for i in range(len(lines)):
        if lines[i].strip()[0].isdigit():
            index_line = i
            break
    for i in range(len(lines[index_line])):
        if not lines[index_line][i].isdigit():
            continue
        crate_stack = deque()
        for j in range(index_line - 1, -1, -1):
            if i < len(lines[j]) and lines[j][i] != ' ':
                crate_stack.append(lines[j][i])
        stacks.append(crate_stack)

    return stacks


def main():
    f = open("day05.txt")
    lines = f.readlines()

    crate_stacks = parse_crate_stacks(lines)
    for line in lines:
        if not line.startswith("move"):
            continue
        line_parts = line.strip().split()
        n, org, dest = int(line_parts[1]), int(line_parts[3]), int(line_parts[5])
        for i in range(n):
            crate_stacks[dest].append(crate_stacks[org].pop())

    message = []
    for i in range(1, len(crate_stacks)):
        message.append(crate_stacks[i].pop())
    print("".join(message))


if __name__ == '__main__':
    main()
