file = "data13.txt"
test_file = "test_data13.txt"

data = []
with open(test_file, "r") as f:
    for line in f:
        data.append(line.strip())

# get corrds
corrds = []
for corrd in data:
    if corrd == '':
        break
    corrds.append(corrd)

# create array
# find max for row and col
rows = 0
cols = 0
for x in crrds:
    if x[]
