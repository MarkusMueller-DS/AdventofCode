file = "data3.txt"

arr = []
with open(file, "r") as f:
    for line in f:
        arr.append(line)

# print(arr)

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

# Oxygen generator rating -> most comman and keep those
# equal ammounts only keep the ones with a 1
def oxygen(arr, idx):
    criteria = ""
    # Abbruchbedingung
    if len(arr) == 1:
        return arr[0]

    col = ""
    for number in arr:
        counter1 = 0
        counter0 = 0
        col += number[idx]
        for char in col:
            if "1" in char:
                counter1 += 1
            else:
                counter0 += 1
        if counter1 > counter0:
            criteria = "1"
        elif counter1 == counter0:
            criteria = "1"
        else:
            criteria = "0"
        # criteria = "1" if counter > len(col)/2 else "0"
    # print(criteria)
    list_remove = []
    for number in arr:
        if criteria != number[idx]:
            list_remove.append(number)
    reduced_arr = [item for item in arr if item not in list_remove]
    # print(reduced_arr)
    idx += 1
    return oxygen(reduced_arr, idx)

oxygen_value = oxygen(arr, 0)


# CO2 -> least common, equal onyl keep the ones with a 0
def co2(arr, idx):
    criteria = ""
    # Abbruchbedingung
    if len(arr) == 1:
        return arr[0]

    col = ""
    for number in arr:
        counter1 = 0
        counter0 = 0
        col += number[idx]
        for char in col:
            if "1" in char:
                counter1 += 1
            else:
                counter0 += 1
        if counter1 < counter0:
            criteria = "1"
        elif counter1 == counter0:
            criteria = "0"
        else:
            criteria = "0"
        # criteria = "1" if counter > len(col)/2 else "0"
    # print(criteria)
    list_remove = []
    for number in arr:
        if criteria != number[idx]:
            list_remove.append(number)
    reduced_arr = [item for item in arr if item not in list_remove]
    # print(reduced_arr)
    idx += 1
    return co2(reduced_arr, idx)

co2_value = co2(arr, 0)

print(oxygen_value)
print(co2_value)

result = int(oxygen_value, 2) * int(co2_value, 2)
print(result)
