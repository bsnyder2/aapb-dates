import matplotlib.pyplot as plt
import numpy as np

filepaths = ["./out1.tsv", "./out2.tsv"]

years = []

for filepath in filepaths:
    file = open(filepath, "r")
    for line in file:
        years.append(int(line[-5:]))

print(len(years))

bins = np.arange(1900, 2030, 10)

fig, ax = plt.subplots()
ax.set_xticks(bins)

ax.hist(
    years,
    bins,
)
plt.show()

# Right now- there are abuot 485,000 dated records
