from aocd import get_data, submit

def get_fuel_cost_from(position, submarines):
    fuel_cost = 0
    for submarine in submarines:
        distance = abs(submarine - position)
        fuel_cost += (distance * (distance + 1)) / 2

    return int(fuel_cost)

def main():
    positions = list(map(int, get_data().split(',')))

    min_fuel = float('inf')

    for position in range(min(positions), max(positions) + 1):
        fuel_cost = get_fuel_cost_from(position, positions)
        min_fuel = min(min_fuel, fuel_cost)

    submit(min_fuel)

if __name__ == '__main__':
    main()