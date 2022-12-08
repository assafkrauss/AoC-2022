def main():
    f = open("day08.txt")
    lines = f.readlines()

    matrix = []
    for line in lines:
        matrix.append(list(map(lambda t: int(t), line.strip())))

    count = 0
    best_scenic_score = 0
    for y in range(len(matrix)):
        for x in range(len(matrix)):
            up_scene, down_scene, left_scene, right_scene = 0, 0, 0, 0
            # look up:
            seen = True
            added = False
            for i in range(y - 1, -1, -1):
                up_scene += 1
                if matrix[y][x] <= matrix[i][x]:
                    seen = False
                    break
            if seen and not added:
                count += 1
                added = True
            # look down:
            seen = True
            for i in range(y + 1, len(matrix)):
                down_scene += 1
                if matrix[y][x] <= matrix[i][x]:
                    seen = False
                    break
            if seen and not added:
                count += 1
                added = True
            # look left:
            seen = True
            for i in range(x - 1, -1, -1):
                left_scene += 1
                if matrix[y][x] <= matrix[y][i]:
                    seen = False
                    break
            if seen and not added:
                count += 1
                added = True
            # look right:
            seen = True
            for i in range(x + 1, len(matrix)):
                right_scene += 1
                if matrix[y][x] <= matrix[y][i]:
                    seen = False
                    break
            if seen and not added:
                count += 1
            scenic_score = up_scene * down_scene * left_scene * right_scene
            if best_scenic_score < scenic_score:
                best_scenic_score = scenic_score

    print(count)
    print(best_scenic_score)


if __name__ == '__main__':
    main()
