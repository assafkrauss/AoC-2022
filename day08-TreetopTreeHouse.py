def main():
    f = open("day08.txt")
    lines = f.readlines()

    matrix = []
    for line in lines:
        matrix.append(list(map(lambda t: int(t), line.strip())))

    count = 0
    for y in range(len(matrix)):
        for x in range(len(matrix)):
            # search up:
            seen = True
            for i in range(y - 1, -1, -1):
                if matrix[y][x] <= matrix[i][x]:
                    seen = False
                    break
            if seen:
                count += 1
                continue
            # search down:
            seen = True
            for i in range(y + 1, len(matrix)):
                if matrix[y][x] <= matrix[i][x]:
                    seen = False
                    break
            if seen:
                count += 1
                continue
            # search left:
            seen = True
            for i in range(x - 1, -1, -1):
                if matrix[y][x] <= matrix[y][i]:
                    seen = False
                    break
            if seen:
                count += 1
                continue
            # search right:
            seen = True
            for i in range(x + 1, len(matrix)):
                if matrix[y][x] <= matrix[y][i]:
                    seen = False
                    break
            if seen:
                count += 1
                continue

    print(count)


if __name__ == '__main__':
    main()
