file = "data8.txt"
test_file = "test_data8.txt"

input_data = []
with open(file, "r") as f:
    for line in f:
        input_data.append(line)

result_list = []
for line in input_data:

    # test_line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
    input_ = set(filter(None, line.split("|")[0].split(" ")))
    output_ = line.split("|")[1].split(" ")
    output_strip = []
    for x in output_:
        if x != "":
            output_strip.append(x.strip())

    output_ = output_strip
    print(output_)

    # idendify unique lens and assign a value to them
    value_patter_dict = {}
    list_to_delete = []
    for num in input_:
        if len(num) == 2:
            value_patter_dict["1"] = set([char for char in num])
            list_to_delete.append(num)
        if len(num) == 3:
            value_patter_dict["7"] = set([char for char in num])
            list_to_delete.append(num)
        if len(num) == 4:
            value_patter_dict["4"] = set([char for char in num])
            list_to_delete.append(num)
        if len(num) == 7:
            value_patter_dict["8"] = set([char for char in num])
            list_to_delete.append(num)

    # delete unique values from input_
    for pattern in list_to_delete:
        input_.remove(pattern)

# find new number
# get 3
    for x in input_:
        if len(x) == 5:
            x_ = set([char for char in x])
            y = x_.difference(value_patter_dict["1"])
            if len(y) == 3:
                value_patter_dict["3"] = y.union(value_patter_dict["1"])
                item_to_delete = x

    input_.remove(item_to_delete)

# get 2 and 5
    item_to_remove = []
    for x in input_:
        if len(x) == 5:
            x_ = set([char for char in x])
            y = x_.intersection(value_patter_dict["4"])
            if len(y) == 2:
                # got 2
                value_patter_dict["2"] = x_
                item_to_remove.append(x)
            if len(y) == 3:
                # got 5
                value_patter_dict["5"] = x_
                item_to_remove.append(x)


# delete unique values from input_
    for pattern in item_to_remove:
        input_.remove(pattern)


# get 6
    for x in input_:
        if len(x) == 6:
            x_ = set([char for char in x])
            y = x_.intersection(value_patter_dict["1"])
            if len(y) == 1:
                value_patter_dict["6"] = x_
                item_to_remove = x

    input_.remove(item_to_remove)


# get 0 and 9
    item_to_remove = []
    for x in input_:
        if len(x) == 6:
            x_ = set([char for char in x])
            y = x_.intersection(value_patter_dict["4"])
            if len(y) == 3:
                # got 0
                value_patter_dict["0"] = x_
                item_to_remove.append(x)
            if len(y) == 4:
                # got 9
                value_patter_dict["9"] = x_
                item_to_remove.append(x)


# delete unique values from input_
    for pattern in item_to_remove:
        input_.remove(pattern)

# order String in value_patter_dict
    for key in value_patter_dict.keys():
        sorted_pattern = sorted(value_patter_dict[key])
        x_string = "".join(sorted_pattern)
        value_patter_dict[key] = x_string

# oder Strings in output
    output_sorted = []
    for x in output_:
        sorted_output = sorted(x)
        list_sorted = "".join(sorted_output)
        output_sorted.append(list_sorted)

# get number
    num_list = []
    for x in output_sorted:
        for key in value_patter_dict.keys():
            if value_patter_dict[key] == x:
                num_list.append(key)


    num_list = "".join(num_list)
    # print(num_list)
    result_list.append(num_list)

counter = 0
for x in result_list:
    counter += int(x)

print(counter)
