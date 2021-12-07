import pandas as pd

file = "data.txt"
arr = []

with open(file, "r") as f:
    for line in f:
        arr.append(int(line))

data = pd.Series(arr).rolling(3).sum()

# print(type(data[1]))

prev = 0
counter = 0
for x in data:
    curr = x
    # print(curr)
    if (curr > prev):
        counter += 1
        # print(counter)
    prev = x

print(counter)
