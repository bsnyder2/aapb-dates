import matplotlib.pyplot as plt
import numpy as np

# 19% of records have a date field

BIN_WIDTH = 1
START_YEAR = 1940

filepaths = [
    "./data/years-all.tsv",
    "./data/years-digitized.tsv",
    "./data/years-online.tsv",
]
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

labels = ["All Records", "All Digitized", "Available Online"]

fig, ax = plt.subplots()
ax.set_xticks(ticks)
for i, data in enumerate(hist_data):
    ax.hist(data, bins, label=labels[i])
ax.legend()
plt.show()
