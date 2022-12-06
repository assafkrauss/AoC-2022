def main():
    f = open("day06.txt")
    line = f.readline()

    for i in range(3, len(line)):
        if line[i] not in line[i - 3:i] and line[i - 1] not in line[i - 3:i - 1] \
                      and line[i - 2] not in line[i - 3:i - 2]:
            print(i + 1)
            break


if __name__ == '__main__':
    main()
