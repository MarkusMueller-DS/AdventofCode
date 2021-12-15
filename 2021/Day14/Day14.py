file = "data14.txt"
test_file = "test_data14.txt"

data = []
with open(test_file, "r") as f:
    for line in f:
        data.append(line.strip())


input_string = data[0]
insertions = data[2:]

print(input_string)
print(insertions)

result_string = ""

for pair in range(len(input_string)-1):
    for ins in insertions:
        if input_string[pair:pair+2] == ins[:2]:
           result_string += input_string[pair] + ins[6] 

result_string += input_string[-1]

result_string2 = ""

for pair in range(len(result_string)-1):
    for ins in insertions:
        if result_string[pair:pair+2] == ins[:2]:
           result_string2 += result_string[pair] + ins[6] 

result_string2 += result_string[-1]

print(result_string2)
