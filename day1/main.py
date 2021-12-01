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
    max = numbers[0] + numbers[1] + numbers[2]
    length = len(numbers)
    for i in range(length):
        if i  > length - 3:
            break
        current = numbers[i] + numbers[i + 1] + numbers[i + 2]
        if current > max:
            increase+=1
        max = current
    return increase


def main():
    numbers = read()
    print(part1(numbers))
    print(part2(numbers))


if __name__ == "__main__":
    main()
