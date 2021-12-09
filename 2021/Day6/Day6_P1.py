file = "data6.txt"
test_file = "test_data6.txt"

input_list = []
with open(file, "r") as f:
    for char in f:
        input_list = char.split(",")

input_list = [x.strip() for x in input_list] 
input_list = [int(x) for x in input_list]

counter = 0 
result_list = []

def generateFisch(data, counter):
    if counter == 80:
        return data
    counter += 1
    helper_list = []
    for x in data:
        if x != 0:
            x -= 1
            helper_list.append(x)
        else:
            helper_list.append(6)
            helper_list.append(8)
    print(helper_list)
    return generateFisch(helper_list, counter)


data = generateFisch(input_list, 0)

print(len(data))
