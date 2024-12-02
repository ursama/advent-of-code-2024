def is_safe(report):
    inc, dec = True, True
    for i in range(len(report) - 1):
        diff = calc_diff(report, i)

        if abs(diff) > 3 or diff == 0:
            return False
        if diff > 0:
            inc = False
        if diff < 0:
            dec = False

    return inc or dec


def calc_diff(x, i):
    return int(x[i]) - int(x[i + 1])


def part1():
    safe_sum = sum(1 for report in data if is_safe(report))
    print(safe_sum)


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = [line.split() for line in file.readlines()]

    part1()
