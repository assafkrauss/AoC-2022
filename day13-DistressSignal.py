import ast


# return <0 if p1 < p2
# return >0 if p1 > p2
# return 0 if p1 == p2
def compare_packet(p1, p2):
    if type(p1) is int and type(p2) is int:
        return p1 - p2
    if type(p1) is list and type(p2) is list:
        for i in range(len(p1)):
            if i >= len(p2):
                return 1
            temp = compare_packet(p1[i], p2[i])
            if temp != 0:
                return temp
        if len(p1) < len(p2):
            return -1
        return 0
    if type(p1) is int and type(p2) is list:
        return compare_packet([p1], p2)
    if type(p1) is list and type(p2) is int:
        return compare_packet(p1, [p2])
    raise Exception("Unknown type")


def main():
    f = open("day13.txt")
    lines = f.readlines()

    indices_sum = 0
    for i in range(0, len(lines), 3):
        p1 = ast.literal_eval(lines[i].strip())
        p2 = ast.literal_eval(lines[i + 1].strip())
        if compare_packet(p1, p2) < 0:
            indices_sum += (i // 3) + 1
    print(indices_sum)


if __name__ == '__main__':
    main()
