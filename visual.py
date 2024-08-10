import matplotlib.pyplot as plt
import numpy as np

BIN_WIDTH = 1

START_YEAR = 1930


filepaths = ["./years-all.tsv", "./years-digitized.tsv", "./years-online.tsv"]

hist_data = [[], [], []]
for hist_data_i, filepath in enumerate(filepaths):
    for line in open(filepath, "r"):
        hist_data[hist_data_i].append(int(line[-5:]))


# for line in open(filepaths[0], "r"):
#     all_years.append(int(line[-5:]))
# digitized_years = []
# for line in open(filepaths[1], "r"):
#     digitized_years.append(int(line[-5:]))
# online_years = []
# for line in open(filepaths[2], "r"):
#     online_years.append(int(line[-5:]))


bins1 = np.arange(1900, 2021, BIN_WIDTH)
bins2 = np.arange(2020, 2025, BIN_WIDTH)
bins = np.concatenate((bins1, bins2)) if BIN_WIDTH <= 4 else np.append(bins1, 2024)

ticks = np.arange(1900, 2030, 10)

fig, ax = plt.subplots()
ax.set_xticks(ticks)

ax.hist(
    hist_data[0],
    bins,
)
ax.hist(
    hist_data[1],
    bins,
)
ax.hist(hist_data[2], bins)


# plt.xlim(left=START_YEAR)

plt.show()

# Option to only show specific range (only having some x values, not using xlim)

# Right now- there are abuot 485,000 dated records
