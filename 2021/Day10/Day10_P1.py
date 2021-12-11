file = "data10.txt"
test_file = "test_data10.txt"


data = []
with open(file, "r") as f:
    for line in f:
        data.append(line.strip())

stack = []
open_list = ['{', '(', '[', '<']
close_list = ['}', ')', ']', '>']

iligal_chars_list = []

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
                    # print("found iligal character", char)
                    iligal_chars_list.append(char)
                    flag = False

print(iligal_chars_list)

score_dcit = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

iligal_sum = 0
for char in iligal_chars_list:
    iligal_sum += score_dcit[char]

print(iligal_sum)
