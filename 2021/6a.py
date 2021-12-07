from aocd import get_data, submit

class FishTank:
    def __init__(self, timer_str, ticks):
        self.ticks = ticks
        self.fishes = []
        self.parse_data(timer_str)

    def parse_data(self, timer_str):
        timers = map(int, timer_str.split(','))
        for timer in timers:
            self.fishes.append(LanternFish(timer))
        
        #print(self.fishes)

    def run(self):
        while self.ticks > 0:
            new_fishes = []
            for fish in self.fishes:
                new_fish = fish.tick()
                if new_fish:
                    new_fishes.append(new_fish)

            self.fishes.extend(new_fishes)
            self.ticks -= 1

    def fish_count(self):
        return len(self.fishes)

class LanternFish:
    def __init__(self, timer):
        self.timer = timer

    def tick(self):
        if self.timer == 0:
            self.timer = 6
            return LanternFish(8)

        self.timer -= 1
        return None

def main():
    ft = FishTank(get_data(), 80)

    ft.run()

    submit(ft.fish_count())

if __name__ == '__main__':
    main()