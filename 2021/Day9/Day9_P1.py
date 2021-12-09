file = "data9.txt"
test_file = "test_data9.txt"


# create a big array:
levels = []
with open(file) as f:
    for line in f:
        level_line = []
        for char in line.strip():  #remove new line
            if char != "":
                level_line.append(int(char))
        levels.append(level_line)

# for line in levels:
    # print(line)

list_low_points = []
for i in range(len(levels)):
    for j in range(len(levels[i])):
        # top row
        if i == 0:
            # corner point top left
            if j == 0:
                if levels[i][j] < levels[i+1][j] and levels[i][j] < levels[i][j+1]:
                    list_low_points.append(levels[i][j])
            # corner point top right
            elif j == len(levels[i])-1:
                if levels[i][j] < levels[i+1][j] and levels[i][j] < levels[i][j-1]:
                    list_low_points.append(levels[i][j])
            # row check
            elif levels[i][j] < levels[i][j-1] and levels[i][j] < levels[i][j+1] and levels[i][j] < levels[i+1][j]:
                list_low_points.append(levels[i][j])
        # bottom row
        elif i == len(levels)-1:
            # corner point bottom left
            if j == 0:
                if levels[i][j] < levels[i-1][j] and levels[i][j] < levels[i][j+1]:
                    list_low_points.append(levels[i][j])
            # corner point top right
            elif j == len(levels[i])-1:
                if levels[i][j] < levels[i-1][j] and levels[i][j] < levels[i][j-1]:
                    list_low_points.append(levels[i][j])
            # row check
            elif levels[i][j] < levels[i][j-1] and levels[i][j] < levels[i][j+1] and levels[i][j] < levels[i-1][j]:
                list_low_points.append(levels[i][j])
        # left  row
        elif j == 0:
            if levels[i][j] < levels[i-1][j] and levels[i][j] < levels[i][j+1] and levels[i][j] < levels[i+1][j]:
                list_low_points.append(levels[i][j])
        # right row
        elif j == len(levels[i])-1:
            if levels[i][j] < levels[i-1][j] and levels[i][j] < levels[i][j-1] and levels[i][j] < levels[i+1][j]:
                list_low_points.append(levels[i][j])
        # inner rows
        else:
            if levels[i][j] < levels[i-1][j] and levels[i][j] < levels[i][j-1] and levels[i][j] < levels[i+1][j] and levels[i][j] < levels[i][j+1]:
                list_low_points.append(levels[i][j])


# print(list_low_points)

counter = 0
for x in list_low_points:
    counter += int(x)+1

print(counter)
