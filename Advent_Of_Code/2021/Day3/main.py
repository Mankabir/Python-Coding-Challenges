def problem1(bin_numbers):
    gammabits = ''
    epsilonbits = ''
    for b in bits:
        if b.count('1') > b.count('0'):
            gammabits += '1'
            epsilonbits += '0'
        else:
            gammabits += '0'
            epsilonbits += '1'
    
    gamma = int(gammabits, 2)
    epsilon = int(epsilonbits, 2)

    print(gamma * epsilon)

if __name__ == '__main__':
    bits = []
    with open('input.txt') as f:
        data = f.read().splitlines()

        for i in range(12):
            bitString = ''
            for line in data:
                bitString += line[i]
            bits.append(bitString)

    problem1(data) # 2967914
    #problem2(data) # 1942068080