file = "data3.txt"

# Test-data
# arr = [
    # "00100",
    # "11110",
    # "10110",
    # "10111",
    # "10101",
    # "01111",
    # "00111",
    # "11100",
    # "10000",
    # "11001",
    # "00010",
    # "01010"
# ]

arr = []
with open(file, "r") as f:
    for line in f:
        arr.append(line)

counter0 = 0
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0
counter7 = 0
counter8 = 0
counter9 = 0
counter10 = 0
counter11 = 0


for line in arr:
    counter0 += int(line[0])
    counter1 += int(line[1])
    counter2 += int(line[2])
    counter3 += int(line[3])
    counter4 += int(line[4])
    counter5 += int(line[5])
    counter6 += int(line[6])
    counter7 += int(line[7])
    counter8 += int(line[8])
    counter9 += int(line[9])
    counter10 += int(line[10])
    counter11 += int(line[11])


counter0 = "1" if counter0 > len(arr)/2 else "0"
counter1 = "1" if counter1 > len(arr)/2 else "0"
counter2 = "1" if counter2 > len(arr)/2 else "0"
counter3 = "1" if counter3 > len(arr)/2 else "0"
counter4 = "1" if counter4 > len(arr)/2 else "0"
counter5 = "1" if counter5 > len(arr)/2 else "0"
counter6 = "1" if counter6 > len(arr)/2 else "0"
counter7 = "1" if counter7 > len(arr)/2 else "0"
counter8 = "1" if counter8 > len(arr)/2 else "0"
counter9 = "1" if counter9 > len(arr)/2 else "0"
counter10 = "1" if counter10 > len(arr)/2 else "0"
counter11 = "1" if counter11 > len(arr)/2 else "0"

gamma = counter0 + counter1 + counter2 + counter3 + counter4 + counter5 + counter6 + counter7 + counter8 + counter9 + counter10 + counter11
print(gamma)

epsilon = ""
for char in gamma:
    if char == "0":
        epsilon += "1"
    else: 
        epsilon += "0"

print(epsilon)


print(len(arr))

result = int(gamma, 2) * int(epsilon, 2)

print(result)
