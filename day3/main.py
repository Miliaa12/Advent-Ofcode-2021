from collections import Counter

def read():
    with open('input') as f:
        lines = f.readlines()
    return lines

def part1(lines):
    ones = 0
    zeros = 0
    gamma = ""
    epsilon = ""
    size = len(lines[0]) - 1
    for i in range(size):
        for l in lines:
            if l[i] == '1': ones +=1
            elif l[i] == '0': zeros +=1
        if ones > zeros: gamma +='1'; epsilon +='0'
        if ones < zeros: gamma +='0'; epsilon +='1'
        ones = 0
        zeros = 0

    return int(gamma, 2) * int(epsilon, 2)

def calc_bit_criteria(lines: str, type: str):
    print(len(lines))
    if type == "oxygen": return Counter(lines).most_common(1)[0][0]
    if type == "co2": return Counter(lines).most_common(-1)

def calculate_generator(lines: str, type: str):
    temp=[]
    criteria = 0
    for i in range(len(lines[0])-1):
        for l in lines: temp.append(l[i])
        criteria = calc_bit_criteria(temp, type)
        for li in lines:
            if li[i] != criteria: lines.remove(li)
        temp.clear()
    return lines

def part2(lines: str):
    print(calculate_generator(lines[:], "co2"))
    #print(calculate_generator(lines[:], "oxygen"))

def main():
    print(part1(read()))
    part2(read())

if __name__ == "__main__":
    main()
