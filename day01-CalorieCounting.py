def main():
    f = open("day01.txt")
    lines = f.readlines()

    top3 = [0, 0, 0]
    current_count = 0
    for i in range(len(lines)):
        if len(lines[i].strip()) == 0:
            if current_count > top3[0]:
                top3[2] = top3[1]
                top3[1] = top3[0]
                top3[0] = current_count
            elif current_count > top3[1]:
                top3[2] = top3[1]
                top3[1] = current_count
            elif current_count > top3[2]:
                top3[2] = current_count
            current_count = 0
            continue
        current_count += int(lines[i].strip())
    # counting for that last elf:
    if current_count > top3[0]:
        top3[2] = top3[1]
        top3[1] = top3[0]
        top3[0] = current_count
    elif current_count > top3[1]:
        top3[2] = top3[1]
        top3[1] = current_count
    elif current_count > top3[2]:
        top3[2] = current_count

    print("#1: {0}".format(top3[0]))
    print("top 3 sum: {0}".format(sum(top3)))


if __name__ == '__main__':
    main()
