import pandas as pd

# Задання серії значень
some_series = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5]

# Задання кількості бінів
num_bins = 5

# Знаходження мінімального і максимального значень у серії
min_val = min(some_series)
max_val = max(some_series)

# Обчислення ширини біна
bin_width = (max_val - min_val) / num_bins

# Ініціалізація бінів та пустого словника для підрахунку кількості значень
bins = [min_val + i * bin_width for i in range(num_bins)]
histogram = {bin_: 0 for bin_ in bins}

# Обчислення гістограми
for value in some_series:
    for i in range(num_bins):
        if i == num_bins - 1:
            if value >= bins[i] and value <= max_val:
                histogram[bins[i]] += 1
        else:
            if value >= bins[i] and value < bins[i+1]:
                histogram[bins[i]] += 1

# Виведення результату
for bin_, count in histogram.items():
    print(f'{bin_} to {bin_ + bin_width}: {count}')


r = pd.Series(some_series).value_counts(bins=5)
