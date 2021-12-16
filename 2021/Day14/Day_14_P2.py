from collections import Counter, defaultdict
import copy as cp

file = "data14.txt"
test_file = "test_data14.txt"

data = []
with open(file, "r") as f:
    for line in f:
        data.append(line.strip())


input_string = data[0]
insertions = data[2:]

# print(input_string)
# print(insertions)

# create defaultdict with pairs for input_string
start_dict = defaultdict(int)
for pair in range(len(input_string)-1):
    pair_ = input_string[pair:pair+2]
    start_dict[pair_] = 1

# print(start_dict)


# create defaultdict for rules
rules_dict = defaultdict()
for rules in insertions:
    key_ = rules[:2]
    value_ = rules[-1]
    rules_dict[key_] = value_

# print(rules_dict)


def find_and_replace(str_dict_count):
    new_str_dict_count = cp.copy(str_dict_count)
    for item in str_dict_count.items():
        for rule in rules_dict.items():
            if item[0] == rule[0]:
                # print("item: ", item, " rule: ", rule)
                # how many of are there
                num_occs = str_dict_count[item[0]]
                new_str_dict_count[item[0]] -= num_occs
                # create new pairs
                new_pair1 = item[0][0] + rule[1]
                new_pair2 = rule[1] + item[0][1]
                # print("creates tow new pairs: ", new_pair1, new_pair2)
                # add to new dict
                new_str_dict_count[new_pair1] += num_occs 
                new_str_dict_count[new_pair2] += num_occs
                # print(new_str_dict_count)
                break
    # remove keys with value 0
    for k, v in list(new_str_dict_count.items()):
        if v == 0:
            del new_str_dict_count[k]
    return new_str_dict_count




for i in range(40):
   start_dict = find_and_replace(start_dict)
   # print(star1_dict)

# count
count_dict = defaultdict(int)
for pair in start_dict.items():
    count_dict[pair[0][0]] += pair[1]
    count_dict[pair[0][1]] += pair[1]

# every char is counted twice
# only the char at the start and end the end is counted once
# to make it easy to process: increse these by one and devide by 2
# start and end chars are alwayse the same
count_dict[input_string[0]] += 1
count_dict[input_string[-1]] += 1

count_list = []
for count in count_dict.items():
    count_dict[count[0]] = count[1] // 2
    count_list.append(count[1] // 2)

print(count_dict)

print(max(count_list) - min(count_list))
