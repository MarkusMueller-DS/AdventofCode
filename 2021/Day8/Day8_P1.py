file = "data8.txt"
test_file = "test_data8.txt"

result_list = []
with open(file, "r") as f:
    for line in f:
        x = line.split("|")[1]
        for num in x.split(" "):
            result_list.append(num.strip())

# remove empty strings
result_list = [string for string in result_list if string != ""]

# print(result_list)

counter = 0
for num in result_list:
    # print(num, " ", len(num))
    if len(num) == 2 or len(num) == 3 or len(num) ==7 or len(num) == 4:
        counter += 1

print(counter)
