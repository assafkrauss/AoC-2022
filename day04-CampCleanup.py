def main():
    f = open("day04.txt")
    lines = f.readlines()

    containing_pairs_count = 0
    for line in lines:
        [elf1, elf2] = line.split(',')
        [elf1_from, elf1_to] = map(lambda x: int(x), elf1.split('-'))
        [elf2_from, elf2_to] = map(lambda x: int(x), elf2.split('-'))
        if elf1_from >= elf2_from and elf1_to <= elf2_to or \
           elf2_from >= elf1_from and elf2_to <= elf1_to:
            containing_pairs_count += 1
    print(containing_pairs_count)


if __name__ == '__main__':
    main()
