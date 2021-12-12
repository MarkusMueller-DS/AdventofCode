# after spending 3-4 hours trying to make it work
# I partially used code from:
# https://github.com/EnisBerk/adventofcode/blob/master/day11/tools.py
# I applied parts of the solution 


import numpy as np

file = "data11.txt"
test_file = "test_data11.txt"

data = []
with open(file, "r") as f:
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
print(rows, cols)


counter_flashes = 0

def flag():
    flag = np.any(data > 9)
    print(flag)


def step():
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] += 1

def energyFlashes(r,c):
    global counter_flashes
    counter_flashes += 1
    data[r][c] = -1
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            rr = r + dr
            cc = c + dc
            if 0<=rr<rows and 0<=cc<cols and data[rr][cc] != -1:
                data[rr][cc] += 1
                if data[rr][cc] > 9:
                    energyFlashes(rr, cc)

def check9():
    for i in range(rows):
        for j in range(cols):
            if data[i][j] > 9:
                energyFlashes(i,j)


def setFalse():
    global synchronized 
    for i in range(rows):
        for j in range(cols):
            if data[i][j] == -1:
                data[i][j] = 0
            else:
                synchronized = False

t = 0
while True:
    t += 1
    # print("Step: ", str(t))
    step()
    check9()
    synchronized = True     # flag to see if octupi flash simultaneously
    setFalse()
    # print(data)
    # print("---")
    if t == 100:            # Part 1
        pass
        # print(counter_flashes)
    if synchronized:        # Part 2
        print(t)
        break











