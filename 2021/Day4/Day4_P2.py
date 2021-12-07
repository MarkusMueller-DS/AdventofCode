import numpy as np

file = "data4.txt"
test_file = "test_data4.txt"

# open file to read first line with numbers
with open(file, "r") as f:
    numbers = f.readline()
f.close()
numbers_list = []
for num in numbers.split(","):
    numbers_list.append(int(num))


# get bingo boards
text_file = open(file, "r")
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

# print(dict_c)

dict_transpose = {}
# Transpose Data inside dict
for key in dict_c.keys():
    dict_transpose[key] = np.transpose(dict_c[key])


# print(dict_c["0"])
# print(dict_transpose["0"])

def bingoRow(board, name):
    num_counter = 0
    hit_counter_r0 = 0
    hit_counter_r1 = 0
    hit_counter_r2 = 0
    hit_counter_r3 = 0
    hit_counter_r4 = 0
    num_list = []
    for num in numbers_list:
        num_list.append(num)
        num_counter += 1
        if num in board[0]:
            hit_counter_r0 += 1
            if hit_counter_r0 == 5:
                return [name, 0, num_counter, num, num_list]

        if num in board[1]:
            hit_counter_r1 += 1
            if hit_counter_r1 == 5:
                return [name, 1, num_counter, num, num_list]

        if num in board[2]:
            hit_counter_r2 += 1
            if hit_counter_r2 == 5:
                return [name, 2, num_counter, num, num_list]

        if num in board[3]:
            hit_counter_r3 += 1
            if hit_counter_r3 == 5:
                return [name, 3, num_counter, num, num_list]

        if num in board[4]:
            hit_counter_r4 += 1
            if hit_counter_r4 == 5:
                return [name, 4, num_counter, num, num_list]




result_list_c = []
for key in dict_c.keys():
    r = bingoRow(dict_c[key], key)
    result_list_c.append(r)

result_list_t = []
for key in dict_transpose.keys():
    r = bingoRow(dict_transpose[key], key)
    result_list_t.append(r)


combined_results = []
for row_c, row_t in zip(result_list_c, result_list_t):
    if row_c[2] < row_t[2]:
        combined_results.append(row_c)
    else:
        combined_results.append(row_t)

# print(combined_results)

result_list = np.array(combined_results, dtype=object)
max_idx = result_list[:,2].argmax()
result_list = result_list[max_idx,:]

print(result_list)

result_board = dict_c[result_list[0]]   # dosent matter if normal or transposed
result_board_flatten = result_board.flatten()

unmarked_nums = []
for num in result_board_flatten:
    if num not in result_list[4]:
        unmarked_nums.append(num)


# print(result_list)
# print(result_board)
# print(result_board_flatten)
# print(sum(unmarked_nums))


print(sum(unmarked_nums) * result_list[3])

# # df = pd.DataFrame(result_list)
