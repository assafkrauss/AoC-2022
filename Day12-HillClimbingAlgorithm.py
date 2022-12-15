def find_neighbors(v, limit_x, limit_y):
    neighbors = [(v[0], v[1] + 1), (v[0], v[1] - 1),
                 (v[0] - 1, v[1]), (v[0] + 1, v[1])]
    return [n for n in neighbors if 0 <= n[0] < limit_x and 0 <= n[1] < limit_y]


def bfs(root, goal, elevation_map):
    q = [root]
    explored = {root}
    back_steps = {root: None}

    while len(q) != 0:
        v = q.pop(0)
        if v == goal:
            break
        for w in find_neighbors(v, len(elevation_map[0]), len(elevation_map)):
            if elevation_map[w[1]][w[0]] - elevation_map[v[1]][v[0]] > 1:
                continue
            if w in explored:
                continue
            explored.add(w)
            back_steps[w] = v
            q.append(w)

    if goal not in back_steps.keys():
        return -1

    trail = 0
    v = goal
    while v != root:
        v = back_steps[v]
        trail += 1
    return trail


def main():
    f = open("day12.txt")
    lines = f.readlines()
    elevation_map: list[list[int]] = []

    root = None
    goal = None
    for y in range(len(lines)):
        elevation_map.append([])
        line = lines[y].strip()
        for x in range(len(line)):
            if line[x] == 'S':  # found root!
                root = (x, y)
                elevation_map[y].append(1)
            elif line[x] == 'E':  # found goal!
                goal = (x, y)
                elevation_map[y].append(26)
            else:
                elevation_map[y].append(ord(line[x]) - ord('a') + 1)

    steps = bfs(root, goal, elevation_map)
    print(steps)

    for y in range(len(elevation_map)):
        for x in range(len(elevation_map[y])):
            if elevation_map[y][x] == 1:
                s = bfs((x, y), goal, elevation_map)
                if s != -1 and s < steps:
                    steps = s
    print(steps)


if __name__ == '__main__':
    main()
