file = open("years-all.tsv")

sum = 0

lst = ["2020", "2021", "2022", "2023", "2024"]
# lst2 = ["1995", "1996", "1997", "1998", "1999"]


for line in file:
    if int(line[-5:-1]) < 1940:
        sum += 1

print(sum)

# 169 records before 1940
