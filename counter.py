file = open("./data-2024-08/years-all.tsv")

sum = 0

lst = ["2020", "2021", "2022", "2023", "2024"]
# lst2 = ["1995", "1996", "1997", "1998", "1999"]


for line in file:
    if int(line[-5:-1]) == 2011:
        sum += 1

print(sum)

# 169 records before 1940

# TODO issue: online archive shows fewer records in x year than retrieved from api, e.g. 1992
# is this an issue?
# Actually, implication of this is that I don't know how many total undated records there are. But honestly it's fine
