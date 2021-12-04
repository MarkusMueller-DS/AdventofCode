import numpy as np
import pandas as pd

file = "data4.txt"
test_file = "test_data4.txt"

# open file to read first line with numbers
with open(test_file, "r") as f:
    numbers = f.readline()
f.close()
numbers_list = []
for num in numbers.split(","):
    numbers_list.append(int(num))


# get bingo boards
text_file = open(test_file, "r")
data = text_file.read()

dict_boards = {}
for idx, row in enumerate(data.split("\n\n")[1:]):
    inrows = []
    for inrow in list(row.split("\n")):
        inrows.append(inrow)
    inrows = inrows[:5]
    innernums = []
    for x in inrows:
        innernums.append(x.split(" "))
    dict_boards[str(idx)] = innernums

dict_c = {}
for key in dict_boards.keys():
    row_c = []
    for row in dict_boards[key]:
        row_c.append(' '.join(row).split())
    row_np = row_c
    row_np = np.array(row_np)
    row_np = row_np.astype(np.intc)
    dict_c[key] = row_np


# boardlist = [board1, board2, board3, board1t, board2t, board3t]


def bingoRow(board, name):
    num_counter = 0
    hit_counter_r0 = 0
    hit_counter_r1 = 0
    hit_counter_r2 = 0
    hit_counter_r3 = 0
    hit_counter_r4 = 0
    for num in numbers_list:
        num_counter += 1
        if num in board[0]:
            hit_counter_r0 += 1
            if hit_counter_r0 == 5:
                # print("Bingo")
                # print(name)
                # print(str(num_counter))
                return [name, 0, num_counter, num]

        if num in board[1]:
            hit_counter_r1 += 1
            if hit_counter_r1 == 5:
                # print("Bingo")
                # print(name)
                # print(str(num_counter))
                return [name, 1, num_counter, num]

        if num in board[2]:
            hit_counter_r2 += 1
            if hit_counter_r2 == 5:
                # print("Bingo")
                # print(name)
                # print(str(num_counter))
                return [name, 2, num_counter, num]

        if num in board[3]:
            hit_counter_r3 += 1
            if hit_counter_r3 == 5:
                # print("Bingo")
                # print(name)
                # print(str(num_counter))
                return [name, 3, num_counter, num]

        if num in board[4]:
            hit_counter_r4 += 1
            if hit_counter_r4 == 5:
                # print("Bingo")
                # print(name)
                # print(str(num_counter))
                return [name, 4, num_counter, num]



result_list = []
for key in dict_c.keys():
    r = bingoRow(dict_c[key], key)
    result_list.append(r)

result_list = np.array(result_list)
min_idx = result_list[:,2].argmin()
print(result_list[min_idx,:])

# # df = pd.DataFrame(result_list)
