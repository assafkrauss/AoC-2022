shape_score_sheet = {'X': 1, 'Y': 2, 'Z': 3}


def rps_round(his, mine):
    score = shape_score_sheet[mine]
    if his == 'A' and mine == 'X' or his == 'B' and mine == 'Y' or his == 'C' and mine == 'Z':
        return score + 3
    elif his == 'A' and mine == 'Z' or his == 'B' and mine == 'X' or his == 'C' and mine == 'Y':
        return score
    return score + 6


def main():
    f = open("day02.txt")
    lines = f.readlines()

    total = 0
    for line in lines:
        parts = line.split()
        total += rps_round(parts[0], parts[1])

    print(total)


if __name__ == '__main__':
    main()
