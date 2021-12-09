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


shape_row = len(levels)-1
shape_col = len(levels[0])-1

def findBasinpoints(r, c):
    basin_list_points = set()
    def findBasin(r, c):
        if r < 0 or c < 0 or r > shape_row  or c > shape_col or levels[r][c] == 9 or (r,c) in basin_list_points:
            return

        else:
            basin_list_points.add((r,c))
            # go up
            findBasin(r-1, c)
            # go down
            findBasin(r+1, c)
            # go right
            findBasin(r, c+1)
            #go left
            findBasin(r, c-1)
    findBasin(r,c)

    return basin_list_points

# findBasin(4,6)

# print(basin_list_points)




result_list = []
for i in range(len(levels)):
    for j in range(len(levels[i])):
        # top row
        if i == 0:
            # # corner point top left
            if j == 0:
                if levels[i][j] < levels[i+1][j] and levels[i][j] < levels[i][j+1]:
                    result = findBasinpoints(i,j)
                    result_list.append(result)
            # corner point top right
            elif j == len(levels[i])-1:
                if levels[i][j] < levels[i+1][j] and levels[i][j] < levels[i][j-1]:
                    result = findBasinpoints(i,j)
                    result_list.append(result)
            # row check
            elif levels[i][j] < levels[i][j-1] and levels[i][j] < levels[i][j+1] and levels[i][j] < levels[i+1][j]:
                result = findBasinpoints(i,j)
                result_list.append(result)
        # bottom row
        elif i == len(levels)-1:
            # corner point bottom left
            if j == 0:
                if levels[i][j] < levels[i-1][j] and levels[i][j] < levels[i][j+1]:
                    result = findBasinpoints(i,j)
                    result_list.append(result)
            # corner point top right
            elif j == len(levels[i])-1:
                if levels[i][j] < levels[i-1][j] and levels[i][j] < levels[i][j-1]:
                    result = findBasinpoints(i,j)
                    result_list.append(result)
            # row check
            elif levels[i][j] < levels[i][j-1] and levels[i][j] < levels[i][j+1] and levels[i][j] < levels[i-1][j]:
                result = findBasinpoints(i,j)
                result_list.append(result)
        # left  row
        elif j == 0:
            if levels[i][j] < levels[i-1][j] and levels[i][j] < levels[i][j+1] and levels[i][j] < levels[i+1][j]:
                result = findBasinpoints(i,j)
                result_list.append(result)
        # right row
        elif j == len(levels[i])-1:
            if levels[i][j] < levels[i-1][j] and levels[i][j] < levels[i][j-1] and levels[i][j] < levels[i+1][j]:
                result = findBasinpoints(i,j)
                result_list.append(result)
        # inner rows
        else:
            if levels[i][j] < levels[i-1][j] and levels[i][j] < levels[i][j-1] and levels[i][j] < levels[i+1][j] and levels[i][j] < levels[i][j+1]:
                result = findBasinpoints(i,j)
                result_list.append(result)

len_list = []
for line in result_list:
    len_list.append(len(line))

len_list.sort(reverse = True)
final_sum = 1
for i in range(3):
    final_sum *= len_list[i]

print(final_sum)


# value_list = []
# for point in result:
    # value = levels[point[0]][point[1]]
    # value_list.append(value)

# print(value_list)
