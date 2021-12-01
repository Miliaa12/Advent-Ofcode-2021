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
    newNumbers = []
    counter = 0
    sum = 0
    length = len(numbers)
    for number in numbers:
        if counter < length:
            if length - counter == 3:
                newNumbers.append(sum)
                sum = 0
            else:
                sum+=number
        counter+=1

    return part1(newNumbers)


def main():
    numbers = read()
    print(part1(numbers))
    print(part2(numbers))


if __name__ == "__main__":
    main()
