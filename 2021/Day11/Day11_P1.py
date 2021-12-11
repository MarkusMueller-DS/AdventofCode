import numpy as np

file = "data11.txt"
test_file = "test_data11.txt"

data = []
with open(test_file, "r") as f:
    for line in f:
        row = []
        for char in line.strip():
            row.append(int(char))
        data.append(row)
    
    # one line version:
    # for line in f:
    #     data.append(list(map(int, list(line.strip()))))

    # data = [[int(char) for char in line.rstrip()] for line in input]


# create array with indiater for flash
data = np.array(data)

rows = len(data)
cols = len(data[0])

flashes = np.full((rows,cols), False, dtype=bool)

counter_flashes = 0

# print(data)
# print(flashes)

flag = np.any(data >= 9)
# print(flag)


def step():
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] += 1

def check9():
    global counter_flashes
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data [i][j] > 9:
                 counter_flashes += 1
                 flashes[i][j] = True

def energyFlashes():
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] > 9:
                data[i][j] = 0
                try:
                    if flashes[i+1][j] == False:
                        data[i+1][j] += 1   # down
                except:
                    pass
                try:
                    if flashes[i-1][j] == False:
                        data[i-1][j] += 1   # up
                except:
                    pass
                try:
                    if flashes[i][j+1] == False:
                        data[i][j+1] += 1   # right
                except:
                    pass
                try:
                    if flashes[i][j-1] == False:
                        data[i][j-1] += 1   # left
                except:
                    pass
                try:
                    if flashes[i+1][j+1] == False:
                        data[i+1][j+1] += 1   # down right
                except:
                    pass
                try:
                    if flashes[i+1][j-1] == False:
                        data[i+1][j-1] += 1   # down left
                except:
                    pass
                try:
                    if flashes[i-1][j+1] == False:
                        data[i-1][j+1] += 1   # up right
                except:
                    pass
                try:
                    if flashes[i-1][j-1] == False:
                        data[i-1][j-1] += 1   # up left
                except:
                    pass


def setFalse():
    flashes = np.full((rows.cols), False, dtype=bool)
    
print(data)
print("\n")
step()
check9()
energyFlashes()
print(data)
print("\n")
step()
check9()
energyFlashes()
check9()
energyFlashes()
check9()
energyFlashes()
check9()
energyFlashes()
check9()
energyFlashes()
print(data)
print("\n")
flag = np.any(data >=9)
print(flag)


print(counter_flashes)









