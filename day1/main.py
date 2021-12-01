def read():
    with open('input', 'r') as f:
        numbers = [int(number) for number in f.readlines()]

    return numbers

def part1(numbers):
    last = numbers[0]
    higher = 0
    for number in numbers:
        if number > last:
            higher += 1
        last = number

    return higher

def part2(numbers):
    increase = 0
    max = 0
    length = len(numbers)
    for i in range(length - 3):
        current = numbers[i] + numbers[i + 1] + numbers[i + 2]
        if current > max:
            increase+=1
        max = current
    return increase

def part1v2(numbers):
    return sum([x < y for x, y in zip(numbers[:-1], numbers[1:])])

def part2v2(numbers):
    return sum([x < y for x, y in zip(numbers[:-3], numbers[3:])])

def main():
    numbers = read()
    print("v1", part1(numbers))
    print("v1", part2(numbers))
    print("v2", part1v2(numbers))
    print("v2", part2v2(numbers))



if __name__ == "__main__":
    main()
