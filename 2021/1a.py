from aocd import numbers, submit

def main():
    increases = 0
    prev = numbers[0]
    for depth in numbers[1:]:
        if depth > prev:
            increases += 1
        prev = depth

    submit(increases)

if __name__ == '__main__':
    main()