def main():
    f = open("day03.txt")
    lines = f.readlines()

    total_priority = 0
    for line in lines:
        stripped = line.strip()
        part1 = stripped.strip()[:len(stripped)//2]
        part2 = stripped.strip()[len(stripped)//2:]
        if len(part2) != len(part1):
            raise Exception("unexpected line length")
        for c in part1:
            if c in part2:
                total_priority += ord(c) - ((97 - 1) if c.islower() else (65 - 27))
                break
    print(total_priority)

    total_priority = 0
    for i in range(0, len(lines), 3):
        for c in lines[i].strip():
            if c in lines[i + 1] and c in lines[i + 2]:
                total_priority += ord(c) - ((97 - 1) if c.islower() else (65 - 27))
                break
    print(total_priority)


if __name__ == '__main__':
    main()
