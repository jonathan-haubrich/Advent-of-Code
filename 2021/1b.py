from aocd import numbers, submit
from collections import deque

def main():
    increases = 0
    prev = deque(numbers[0:3], 3)
    for depth in numbers[3:]:
        n = prev.copy()
        n.append(depth)

        if sum(n) > sum(prev):
            increases += 1
        
        prev = n.copy()

    submit(increases)

if __name__ == '__main__':
    main()