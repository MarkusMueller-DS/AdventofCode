import numpy as np

file = "data10.txt"
test_file = "test_data10.txt"


data = []
with open(file, "r") as f:
    for line in f:
        data.append(line.strip())

stack = []
open_list = ['{', '(', '[', '<']
close_list = ['}', ')', ']', '>']
corrupted_list = []

# identify corrupt lines
for row in data:
    flag = True
    for char in row:
        if flag:
            if char in open_list:
                stack.append(char)
            elif char in close_list:
                # get index of the list to identify the pair
                pos = close_list.index(char)
                if len(stack) > 0 and open_list[pos] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    corrupted_list.append(row)
                    flag = False

stack_list = []

for row in data:
    stack = []
    if row in corrupted_list:
        pass
    else:
        for char in row:
            if char in open_list:
                stack.append(char)
            elif char in close_list:
                pos = close_list.index(char)
                # remove open char from stack when closing is present
                if len(stack) > 0 and open_list[pos] == stack[len(stack) -1]:
                    stack.pop()
        stack_list.append(stack)
    
score_dcit = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4 
}

sum_list = []
for row in stack_list:
    sum_ = 0
    row.reverse()
    for char in row:
        sum_ *= 5
        sum_ += score_dcit[char]
    sum_list.append(sum_)

sum_list = np.array(sum_list)
print(np.median(sum_list))

