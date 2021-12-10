def problem1(commands):
    x , y = 0 , 0
    
    for i in commands:
        splitted = i.split()

        if splitted[0] == 'forward':
            x += int(splitted[1])
        elif splitted[0] == 'up':
            y -= int(splitted[1])
        elif splitted[0] == 'down':
            y += int(splitted[1])
    
    print(x * y)

def problem2(commands):
    x , y , aim = 0 , 0 , 0

    for i in commands:
        splitted = i.split()

        if splitted[0] == 'forward':
            x+= int(splitted[1])
            y += aim * int(splitted[1])
        elif splitted[0] == 'up':
            aim -= int(splitted[1])
        elif splitted[0] == 'down':
            aim += int(splitted[1])
    
    print(x * y)

if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read().splitlines()
    problem1(data) # 2039912
    problem2(data) # 1942068080
