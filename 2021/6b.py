from aocd import get_data, submit
from collections import deque

def main():
    ticks = 256
    num_days = 8

    days = deque([0] * (num_days + 1), num_days + 1)

    for day in get_data().split(","):
        days[int(day)] += 1

    for tick in range(ticks):
        new_fishes = days[0]
        days[0] = 0
        days.rotate(-1)
        days[6] += new_fishes
        days[8] += new_fishes

    fishes = sum(days)
    submit(fishes)

if __name__ == '__main__':
    main()