from aocd import lines, submit
from operator import ge, le

class DiagnosticReport:
    def __init__(self, report):
        self.report = report.copy()
        self.rate_width = len(self.report[0])
        self.bit_counts = [0] * self.rate_width
        self.calculate_rates()

    def get_gamma_rate(self):
        gamma_rate = 0
        for i, bit_count in enumerate(reversed(self.bit_counts)):
            if bit_count > 0:
                gamma_rate += (1 << i)

        return gamma_rate

    def get_epsilon_rate(self):
        gamma_rate = self.get_gamma_rate()
        epsilon_rate = gamma_rate ^ ((2 ** self.rate_width) - 1)
        return epsilon_rate

    def get_power_consumption(self):
        return self.get_gamma_rate() * self.get_epsilon_rate()

    def get_rating(self, bit_target, comp):
        current_bit = 0
        numbers = self.report.copy()
        while len(numbers) > 1:
            #print(numbers)
            matches = []
            misses = []
            for line in numbers:
                if line[current_bit] == bit_target:
                    matches.append(line)
                else:
                    misses.append(line)

            if comp(len(matches), len(misses)):
                numbers = matches
            else:
                numbers = misses

            current_bit += 1

        return int(numbers[0], 2)

    def get_oxygen_rating(self):
        return self.get_rating("1", ge)

    def get_cO2_rating(self):
        return self.get_rating("0", le)

    def get_lifesupport_rating(self):
        return self.get_oxygen_rating() * self.get_cO2_rating()

    def calculate_rates(self):
        for line in self.report:
            for i, bit in enumerate(line):
                if bit == "0":
                    self.bit_counts[i] -= 1
                else:
                    self.bit_counts[i] += 1

def main():
    dr = DiagnosticReport(lines)

    submit(dr.get_lifesupport_rating())

if __name__ == '__main__':
    main()