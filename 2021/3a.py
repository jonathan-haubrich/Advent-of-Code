from aocd import lines, submit

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

    def calculate_rates(self):
        for line in self.report:
            for i, bit in enumerate(line):
                if bit == "0":
                    self.bit_counts[i] -= 1
                else:
                    self.bit_counts[i] += 1

def main():
    dr = DiagnosticReport(lines)

    submit(dr.get_power_consumption())

if __name__ == '__main__':
    main()