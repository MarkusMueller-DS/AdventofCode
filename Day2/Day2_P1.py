file = "data2.txt"

forward_arr = []
down_arr = []
up_arr = []

with open(file, "r") as f:
    for line in f:
        if "forward" in line:
            forward_arr.append(line)
        if "down" in line:
            down_arr.append(line)
        if "up" in line:
            up_arr.append(line)

print(forward_arr[:5])
print(down_arr[:5])
print(up_arr[:5])

# split arrays
forward_nums = []
for x in forward_arr:
    num = x.split(" ")[1]
    num = int(num.replace("\n", ""))
    forward_nums.append(num)

down_nums = []
for x in down_arr:
    num = x.split(" ")[1]
    num = int(num.replace("\n", ""))
    down_nums.append(num)

up_nums = []
for x in up_arr:
    num = x.split(" ")[1]
    num = int(num.replace("\n", ""))
    up_nums.append(num)

result = (sum(down_nums) - sum(up_nums)) * sum(forward_nums)
result1 = (sum(up_nums) - sum(down_nums)) * sum(forward_nums)

print(sum(down_nums))
print(sum(up_nums))
print(sum(forward_nums))
print(result)
print(result1)
