from collections import Counter
import math

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(self.sum() / self.count())

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def mode(self):
        freq = Counter(self.data)
        mode_val = freq.most_common(1)[0]
        return {'mode': mode_val[0], 'count': mode_val[1]}

    def var(self):
        mean = self.mean()
        return round(sum((x - mean) ** 2 for x in self.data) / self.count(), 1)

    def std(self):
        return round(math.sqrt(self.var()), 1)

    def freq_dist(self):
        freq = Counter(self.data)
        return sorted([(v * 100 / self.count(), k) for k, v in freq.items()], reverse=True)

    def describe(self):
        print("Count:", self.count())
        print("Sum:", self.sum())
        print("Min:", self.min())
        print("Max:", self.max())
        print("Range:", self.range())
        print("Mean:", self.mean())
        print("Median:", self.median())
        print("Mode:", tuple(self.mode().values()))
        print("Variance:", self.var())
        print("Standard Deviation:", self.std())
        print("Frequency Distribution:", self.freq_dist())

# Sample usage
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32,
        33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)
data.describe()