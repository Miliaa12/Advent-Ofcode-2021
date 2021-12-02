def read():
    with open('input') as f:
        lines = f.readlines()

    return lines

def part1(lines):
    depth = 0
    position = 0
    for l in lines:
        direction, value = l.split(' ', 1)
        if direction == "forward":
            position += int(value)
        elif direction == "up":
            depth -= int(value)
        elif direction == "down":
            depth += int(value)

    return position*depth

def part2(lines):
    depth = 0
    position = 0
    aim = 0
    for l in lines:
        direction, value = l.split(' ', 1)
        if direction == "forward":
            position += int(value)
            depth += (aim*int(value))
        elif direction == "up":
            aim -= int(value)
        elif direction == "down":
            aim += int(value)
    return position*depth

def main():
    lines = read()
    print(part1(lines))
    print(part2(lines))

if __name__ == "__main__":
    main()
