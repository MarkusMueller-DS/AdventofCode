from collections import Counter, defaultdict
import copy as cp

file = "data14.txt"
test_file = "test_data14.txt"

data = []
with open(test_file, "r") as f:
    for line in f:
        data.append(line.strip())


input_string = data[0]
insertions = data[2:]

# print(input_string)
# print(insertions)

# create defaultdict for rules
rules_dict = defaultdict(int)
for rules in insertions:
    rules_dict[rules[:2]] = 0

# print(rules_dict)


def find_and_replace(input_str):
    for pair in range(len(input_str)-1):
        for ins in insertions:
            if input_str[pair:pair+2] == ins[:2]:
                key = input_str[pair:pair+2] 
                rules_dict[key] == 0
                str_1 = key[0] + ins[-1]
                rules_dict[str_1] += 1
                str_2 = ins[-1] + key[1]
                rules_dict[str_2] += 1
    retrun rules_dict


for i in range(2):
    dict_ = find_and_repalce(input_str)



find_and_replace(input_string)
print(rules_dict)


#
# # use counter so count occurences of chars
# c = Counter(test_str)
# print(c.most_common())
#
#
#
# min_ = 999999999999999999999
# max_ = 0
# for key in c.keys():
#     if c[key] > max_:
#         max_ = c[key]
#     elif c[key] < min_:
#         min_ = c[key]
#
# print(max_ - min_)
