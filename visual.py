import matplotlib.pyplot as plt
import numpy as np

BIN_WIDTH = 1
START_YEAR = 1940


filepaths = ["./years-all.tsv", "./years-digitized.tsv", "./years-online.tsv"]

hist_data = [[], [], []]
for hist_data_i, filepath in enumerate(filepaths):
    for line in open(filepath, "r"):
        year = int(line[-5:])
        if year < START_YEAR:
            continue
        hist_data[hist_data_i].append(year)


bins1 = np.arange(START_YEAR, 2021, BIN_WIDTH)
bins2 = np.arange(2020, 2025, BIN_WIDTH)
bins = np.concatenate((bins1, bins2)) if BIN_WIDTH <= 4 else np.append(bins1, 2024)

ticks = np.arange(START_YEAR, 2030, 10)

fig, ax = plt.subplots()
# ax.set_xticks(ticks)

for data in hist_data:
    ax.hist(data, bins)

plt.show()

# Option to only show specific range (only having some x values, not using xlim)

# Right now- there are abuot 485,000 dated records
