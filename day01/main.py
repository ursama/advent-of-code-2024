def part1():
    sum_distance = 0
    for i in range(0, len(left)):
        sum_distance += abs(left[i] - right[i])

    print(sum_distance)


def part2():
    similarity = 0
    for i in range(0, len(left)):
        multiplier = 0
        for j in range(0, len(right)):
            if right[j] == left[i]:
                multiplier += 1
        similarity += left[i] * multiplier

    print(similarity)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = str(file.read()).split()
        left, right = [], []
        for i in range(0, len(data)):
            if (i + 1) % 2 != 0:
                left.append(int(data[i]))
            else:
                right.append(int(data[i]))

        left.sort()
        right.sort()

    # part1()
    part2()
