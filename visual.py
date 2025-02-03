import matplotlib.pyplot as plt
import numpy as np

# using 19% of records that have a date field

BIN_WIDTH = 10
START_YEAR = 1940

filepaths = [
    # "./data-2025-01/years-all2025.tsv",
    # "./data-2025-01/years-digitized2025.tsv",
    # "./data-2025-01/years-online2025.tsv",
    "./data-2024-08/years-all.tsv",
    "./data-2024-08/years-digitized.tsv",
    "./data-2024-08/years-online.tsv",
]
# lastyear = 0
hist_datas = [[], [], []]
for hist_data_i, filepath in enumerate(filepaths):
    for line in open(filepath, "r"):
        year = int(line[-5:])
        if year < START_YEAR:
            continue
        hist_datas[hist_data_i].append(year)
        # if year == 2023 and hist_data_i == 0:
        # lastyear += 1
# print(lastyear)

print(hist_datas[2])
c = 0
for d in hist_datas[2]:
    if d == 2022:
        c += 1
print(c)


bins1 = np.arange(START_YEAR, 2021, BIN_WIDTH)
bins2 = np.arange(2021, 2026, BIN_WIDTH)
bins = np.concatenate((bins1, bins2)) if BIN_WIDTH <= 4 else np.append(bins1, 2026)
ticks = np.arange(START_YEAR, 2030, 10)
print(bins)

print(bins)

labels = ["All Records", "All Digitized", "Available Online"]

fig, ax = plt.subplots()
ax.set_xticks(ticks)
for i, data in enumerate(hist_datas):
    ax.hist(data, bins, label=labels[i])
ax.legend()

# how many from 2024? negligible? right now only includes up to 2023. so first after each tick is the decade mark

# decade bins
ax.set_ylim(0, 170000)
# year bins
# ax.set_ylim(0, 24000)

fig.set_size_inches(9, 6)
plt.title("AAPB Dated Record Count by Year (08/2024)")
plt.show()
