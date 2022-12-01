def main():
    f = open("day01.txt")
    lines = f.readlines()

    max_count = 0
    current_count = 0
    for i in range(len(lines)):
        if len(lines[i].strip()) == 0:
            if current_count > max_count:
                max_count = current_count
            current_count = 0
            continue
        current_count += int(lines[i].strip())
    # counting for that last elf:
    if current_count > max_count:
        max_count = current_count

    print(max_count)


if __name__ == '__main__':
    main()
