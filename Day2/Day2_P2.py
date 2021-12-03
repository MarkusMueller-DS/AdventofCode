file = "data2.txt"

horizontal_counter = 0
depth_counter = 0
aim_counter = 0


with open(file, "r") as f:
    for line in f:
        if "forward" in line:
            horizontal_counter += int(line.split(" ")[1])
            if (aim_counter > 0):
                depth_counter += aim_counter * int(line.split(" ")[1])
        if "down" in line:
            aim_counter += int(line.split(" ")[1])
        if "up" in line:
            aim_counter -= int(line.split(" ")[1])

# print(horizontal_counter)
# print(depth_counter)
# print(aim_counter)
print(horizontal_counter * depth_counter)
