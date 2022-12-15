def sand_drops(rock_points):
    rock_bottom = max([r[1] for r in rock_points]) + 1
    solid_rock_points = len(rock_points)

    while True:
        sand_point = (500, 0)
        while sand_point not in rock_points:
            if sand_point[1] > rock_bottom:
                break
            if (sand_point[0], sand_point[1] + 1) not in rock_points:
                sand_point = (sand_point[0], sand_point[1] + 1)
                continue
            if (sand_point[0] - 1, sand_point[1] + 1) not in rock_points:
                sand_point = (sand_point[0] - 1, sand_point[1] + 1)
                continue
            if (sand_point[0] + 1, sand_point[1] + 1) not in rock_points:
                sand_point = (sand_point[0] + 1, sand_point[1] + 1)
                continue
            rock_points.add(sand_point)
            break
        if sand_point[1] > rock_bottom or (500, 0) in rock_points:
            break

    return len(rock_points) - solid_rock_points


def main():
    f = open("day14.txt")
    lines = f.readlines()

    rock_points = set()
    for line in lines:
        points = line.strip().split(" -> ")
        for i in range(1, len(points)):
            point_fragments = points[i - 1].split(',')
            from_point = (int(point_fragments[0]), int(point_fragments[1]))
            point_fragments = points[i].split(',')
            to_point = (int(point_fragments[0]), int(point_fragments[1]))
            min_x, max_x = min(from_point[0], to_point[0]), max(from_point[0], to_point[0])
            min_y, max_y = min(from_point[1], to_point[1]), max(from_point[1], to_point[1])
            for x in range(min_x, max_x + 1):
                for y in range(min_y, max_y + 1):
                    rock_points.add((x, y))

    rock_points_copy = rock_points.copy()
    print(sand_drops(rock_points_copy))

    rock_bottom = max([r[1] for r in rock_points]) + 2
    for x in range(500 - rock_bottom, 500 + rock_bottom + 1):
        rock_points.add((x, rock_bottom))
    print(sand_drops(rock_points))


if __name__ == '__main__':
    main()
