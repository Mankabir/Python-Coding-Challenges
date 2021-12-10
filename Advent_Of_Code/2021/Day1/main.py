def problem1(measurements):
    last = 1000
    counter = 0
    for i in measurements:
        if i > last:
            counter = counter + 1
        last = i
    print(counter)

def problem2(measurements):
    counter = 0
    for i in range(len(measurements) - 3):
        if sum(measurements[i + 1 : i + 4]) > sum(measurements[i : i +3]):
            counter = counter + 1
    print(counter)


if __name__ == '__main__':
    with open('input.txt') as f:
        data = list(map(int, f.read().splitlines()))
    problem1(data) # 1529
    problem2(data) # 1567
