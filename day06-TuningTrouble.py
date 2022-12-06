def contains_duplicates(arr):
    for elem in arr:
        if arr.count(elem) > 1:
            return True
    return False


def main():
    f = open("day06.txt")
    line = f.readline()

    for limit in [4, 14]:
        for i in range(limit, len(line)):
            if not contains_duplicates(line[i - limit + 1:i + 1]):
                print(i + 1)
                break


if __name__ == '__main__':
    main()
