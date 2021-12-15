from collections import Counter

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


t = 0

def rec(r_string, t):
    help_string = ""
    if t >= 10:
        return r_string
    for pair in range(len(r_string)-1):
        for ins in insertions:
            if r_string[pair:pair+2] == ins[:2]:
               help_string += r_string[pair] + ins[6] 
    help_string += r_string[-1]
    # print(help_string)
    t += 1
    return rec(help_string, t)


test_str= rec(input_string, t)
print(len(test_str))

# use counter so count occurences of chars
c = Counter(test_str)
print(c.most_common())



min_ = 999999999999999999999
max_ = 0
for key in c.keys():
    if c[key] > max_:
        max_ = c[key]
    elif c[key] < min_:
        min_ = c[key]

print(max_ - min_)
