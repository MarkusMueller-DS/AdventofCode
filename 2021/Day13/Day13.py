import numpy as np

file = "data13.txt"
test_file = "test_data13.txt"

data = []
with open(file, "r") as f:
    for line in f:
        data.append(line.strip())

# get corrds and folds
# get idx of split
split_idx = data.index('')
corrds = data[:split_idx]
folds = data[split_idx+1:]
# print(corrds)
# print(folds)
#
# create tupel-list from corrds
tupel_list = []
for cor in corrds:
    tupel_ = (int(cor.split(",")[0]), int(cor.split(",")[1]))
    tupel_list.append(tupel_)

# print(tupel_list)

# find max for row and col
rows = 0 
cols = 0
for x in tupel_list:
    if x[0] > cols:
        cols = x[0]
    if x[1] > rows:
        rows = x[1]

# print('rows: ', rows)
# print('cols: ', cols)

# create array 
arr = np.full((rows+1, cols+1), 0)
# print(arr)

# fill array with values
for x, y in tupel_list:
    arr[y][x] = 1

# print(arr)

# find number and which way to fold
fold_tupel_list = []
for f in folds:
    tupel_ = (f.split(" ")[2].split("=")[0], int(f.split(" ")[2].split("=")[1]))
    fold_tupel_list.append(tupel_)

# print(fold_tupel_list)

def foldy(array, splitnr):
    for r in range(splitnr+1, len(array)):
        for c in range(len(array[0])):
            if array[r][c] == 1:
                # print("found ", r, c)
                diff = r - splitnr
                array[splitnr-diff][c] = 1
                array[r][c] = 0
    return array[:splitnr,]

def foldx(array, splitnr):
    for r in range(len(array)):
        for c in range(splitnr+1, len(array[r])):
            if array[r][c] == 1:
                diff = c - splitnr
                array[r][splitnr-diff] = 1
                array[r][c] = 0
    return array[:,:splitnr]


for fold in fold_tupel_list:
    if fold[0] == 'y':
        arr = foldy(arr, fold[1])
    elif fold[0] == 'x':
        arr = foldx(arr, fold[1])


counter = 0
for r in range (len(arr)):
    for c in range(len(arr[r])):
        if arr[r][c] == 1:
            counter += 1

for row in arr:
    print(row)
