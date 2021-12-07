from aocd import get_data, submit

def main():
    positions = list(map(int, get_data().split(',')))

    min_fuel = float('inf')

    for position in range(min(positions), max(positions) + 1):
        fuel_cost = sum(map(lambda x: abs(position - x), positions))
        min_fuel = min(min_fuel, fuel_cost)

    print(min_fuel)

if __name__ == '__main__':
    main()