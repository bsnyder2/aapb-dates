file = open("./data-2024-08/years-all.tsv")
sum = 0
for line in file:
    if int(line[-5:-1]) == 2011:
        sum += 1

print(sum)
