import matplotlib.pyplot as plt
import numpy as np

# using 19% of records that have a date field

BIN_WIDTH = 1
START_YEAR = 1940

filepaths = [
    "./data-2025-01/years-all2025.tsv",
    "./data-2025-01/years-digitized2025.tsv",
    "./data-2025-01/years-online2025.tsv",
    # "./data-2024-08/years-all.tsv",
    # "./data-2024-08/years-digitized.tsv",
    # "./data-2024-08/years-online.tsv",
]
hist_datas = [[], [], []]
for hist_data_i, filepath in enumerate(filepaths):
    for line in open(filepath, "r"):
        year = int(line[-5:])
        if year < START_YEAR:
            continue
        hist_datas[hist_data_i].append(year)

bins1 = np.arange(START_YEAR, 2021, BIN_WIDTH)
bins2 = np.arange(2021, 2026, BIN_WIDTH)
bins = np.concatenate((bins1, bins2)) if BIN_WIDTH <= 4 else np.append(bins1, 2026)

fig, ax = plt.subplots()
# each bin's height = # points inside of that range
# so need to divide # points in each range by (# points in each range) of years-all
bin_vals_all, _, _ = ax.hist(hist_datas[0], bins)
bin_vals_digitized, _, _ = ax.hist(hist_datas[1], bins)
bin_vals_online, _, _ = ax.hist(hist_datas[2], bins)

bars_all = [float(a / b) for a, b in zip(bin_vals_all, bin_vals_all)]
bars_digitized = [float(a / b) for a, b in zip(bin_vals_digitized, bin_vals_all)]
bars_online = [float(a / b) for a, b in zip(bin_vals_online, bin_vals_all)]

labels = ["All Records", "All Digitized", "Available Online"]

ax.cla()
ticks = np.arange(START_YEAR, 2030, 10)
ax.set_xticks(ticks)
for i, bars in enumerate([bars_all, bars_digitized, bars_online]):
    ax.bar(
        (BIN_WIDTH / 2) + np.arange(START_YEAR, 2025, BIN_WIDTH),
        bars,
        width=BIN_WIDTH,
        label=labels[i],
    )
ax.legend()
fig.set_size_inches(9, 6)
plt.title("AAPB Dated Record Availability by Year (01/2025)")
plt.show()
