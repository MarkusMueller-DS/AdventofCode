from collections import Counter

file = "data5.txt"
test_file = "data5_test.txt"


num_list = []
with open(test_file, "r") as f:
    for line in f:
        num_list.append(line)

num_list_clean = []
for line in num_list:
    line_clean = line.replace("->", ",").replace(" ", "").replace("\n", "")
    num_list_clean.append(line_clean)

num_list_final = []
for line in num_list_clean:
    list_final = line.split(",")
    num_list_final.append(list_final)

# print(num_list_final)

# find lines which are horizontal or vertical
vert_hori_lines = []
for line in num_list_final:
    if line[0] == line[2] or line[1] == line[3]:
        vert_hori_lines.append(line)

# print(vert_hori_lines)




# diag lines
diag_lines = []
for line in num_list_final:
    if line[0] == line[1] and line[2] == line[3]:
        diag_lines.append(line)
    elif line[0]==line[3] and line[1] == line[2]:
        diag_lines.append(line)
    elif abs(int(line[0]) - int(line[2])) == abs(int(line[1]) -int(line[3])):
        diag_lines.append(line)


num_list_final = []
for line in vert_hori_lines:
    nums_map = map(int, line)
    num_list_final.append(list(nums_map))

# print("vert and horizontal: ", num_list_final)

num_list_diag_final = []
for line in diag_lines:
    nums_map = map(int, line)
    num_list_diag_final.append(list(nums_map))

# print("diag lines: ", num_list_diag_final)

# generate new points from coods
def generateCorrds(coords):
    new_coords_list = []
    # vertical lines
    if coords[0] == coords[2]:
        # print("vertical line detected")
        if coords[1] > coords[3]:
            # print("line goes up")
            new_coords = coords[1] - coords[3]
            coord_start = coords[:2]
            coord_end = coords[2:]
            new_coords_list.append(coord_start)
            y_start = coords[1]
            for x in range(new_coords-1):
                y_start -= 1
                new_coord = [coords[0], y_start]
                new_coords_list.append(new_coord)
            new_coords_list.append(coord_end)
        if coords[1] < coords[3]:
            # print("line goes down")
            # check how many new points need to be generated
            new_coords = coords[3] - coords[1]
            coord_start = coords[:2]
            coord_end = coords[2:]
            new_coords_list.append(coord_start)
            y_start = coords[1]
            for x in range(new_coords-1):
                y_start += 1
                new_coord = [coords[0], y_start]
                new_coords_list.append(new_coord)
            new_coords_list.append(coord_end)
    # horizontal
    if coords[1] == coords[3]:
        # print("horizontal line detected")
        if coords[0] > coords[2]:
            # print("line to the left")
            new_coords = coords[0] - coords[2]
            coord_start = coords[:2]
            coord_end = coords[2:]
            new_coords_list.append(coord_start)
            x_start = coords[0]
            for x in range(new_coords-1):
                x_start -= 1
                new_coord = [x_start, coords[1]]
                new_coords_list.append(new_coord)
            new_coords_list.append(coord_end)
        if coords[0] < coords[2]:
            # print("line to the right")
            new_coords = coords[2] - coords[0]
            coord_start = coords[:2]
            coord_end = coords[2:]
            new_coords_list.append(coord_start)
            x_start = coords[0]
            for x in range(new_coords-1):
                x_start += 1
                new_coord = [x_start, coords[1]]
                new_coords_list.append(new_coord)
            new_coords_list.append(coord_end)
    return new_coords_list

def generateDiagCorrds(coords):
    new_coords_list = []
    # diagonal 1,1 -> 3,3
    if ((coords[0] == coords[1]) and (coords[2] == coords[3])):
        # print("diagonal")
        if coords[0] > coords[2]:
            # print("up")
            new_coords = coords[0] - coords[2]
            coord_start = coords[:2]
            coord_end = coords[2:]
            new_coords_list.append(coord_start)
            x_start = coords[0]
            y_start = coords[1]
            for x in range(new_coords-1):
                x_start -= 1
                y_start -= 1
                new_coord = [x_start, y_start]
                new_coords_list.append(new_coord)
            new_coords_list.append(coord_end)
        if coords[0] < coords[2]:
            # print("down")
            new_coords = coords[2] - coords[1]
            coord_start = coords[:2]
            coord_end = coords[2:]
            new_coords_list.append(coord_start)
            x_start = coords[0]
            y_start = coords[1]
            for x in range(new_coords-1):
                x_start += 1
                y_start += 1
                new_coord = [x_start, y_start]
                new_coords_list.append(new_coord)
            new_coords_list.append(coord_end)
    #diganoal 9,7 -> 7,9
    elif coords[0] == coords[3] and coords[1] == coords[2]:
        if coords[0] > coords[1]:
            new_coords = coords[0] - coords[1]
            coord_start = coords[:2]
            coord_end = coords[2:]
            new_coords_list.append(coord_start)
            x_start = coords[0]
            y_start = coords[1]
            for x in range(new_coords-1):
                x_start -= 1
                y_start += 1
                new_coord = [x_start, y_start]
                new_coords_list.append(new_coord)
            new_coords_list.append(coord_end)
        if coords[0] < coords[1]:
            new_coords = coords[1] - coords[0]
            coord_start = coords[:2]
            coord_end = coords[2:]
            new_coords_list.append(coord_start)
            x_start = coords[0]
            y_start = coords[1]
            for x in range(new_coords-1):
                x_start += 1
                y_start -= 1
                new_coord = [x_start, y_start]
                new_coords_list.append(new_coord)
            new_coords_list.append(coord_end)

    elif abs(coords[0] - coords[2]) == abs(coords[1] - coords[3]):
        print("diga extra")
        # 6,4 -> 2,0
        if coords[0] > coords[2] and coords[1] > coords[3]:
            # print("up")
            new_coords = coords[0] - coords[2]
            coord_start = coords[:2]
            coord_end = coords[2:]
            new_coords_list.append(coord_start)
            x_start = coords[0]
            y_start = coords[1]
            for x in range(new_coords-1):
                x_start -= 1
                y_start -= 1
                new_coord = [x_start, y_start]
                new_coords_list.append(new_coord)
            new_coords_list.append(coord_end)
        # 2,0 -> 6,4
        if coords[0] < coords[2] and coords[1] < coords[3]:
            # print("down")
            new_coords = coords[2] - coords[0]
            coord_start = coords[:2]
            coord_end = coords[2:]
            new_coords_list.append(coord_start)
            x_start = coords[0]
            y_start = coords[1]
            for x in range(new_coords-1):
                x_start += 1
                y_start += 1
                new_coord = [x_start, y_start]
                new_coords_list.append(new_coord)
            new_coords_list.append(coord_end)
        # 5,5 -> 8,2
        if coords[0] == coords[1] and coords[0] < coords[2] and coords[1] > coords[3]:
            # print("up")
            new_coords = coords[2] - coords[1]
            coord_start = coords[:2]
            coord_end = coords[2:]
            new_coords_list.append(coord_start)
            x_start = coords[0]
            y_start = coords[1]
            for x in range(new_coords-1):
                x_start += 1
                y_start -= 1
                new_coord = [x_start, y_start]
                new_coords_list.append(new_coord)
            new_coords_list.append(coord_end)
        # 8,2 -> 5,5
        if coords[2] == coords[3] and coords[1] < coords[3] and coords[0] > coords[2]:
            # print("down")
            new_coords = coords[0] - coords[2]
            coord_start = coords[:2]
            coord_end = coords[2:]
            new_coords_list.append(coord_start)
            x_start = coords[0]
            y_start = coords[1]
            for x in range(new_coords-1):
                x_start -= 1
                y_start += 1
                new_coord = [x_start, y_start]
                new_coords_list.append(new_coord)
            new_coords_list.append(coord_end)
    return new_coords_list

# test_coord = [1,5,3,7]
# r = generateDiagCorrds(test_coord)
# print(r)



final_coord_list = []
for line in num_list_final:
    r = generateCorrds(line)
    # print(r)
    # print("---")
    final_coord_list.append(r)

print(final_coord_list)

final_coord_diag_list = []
for line in num_list_diag_final:
    r = generateDiagCorrds(line)
    # print(r)
    # print("---")
    final_coord_diag_list.append(r)

# print(final_coord_diag_list)


final_coord_list_1d = []
for line in final_coord_list:
    for item in line:
        final_coord_list_1d.append(item)

final_coord_list_1d_diag = []
for line in final_coord_diag_list:
    for item in line:
        final_coord_list_1d_diag.append(item)

# trasfrom points to strings to Count them
point_str_list = []
for point in final_coord_list_1d:
    point_str = ""
    point_x = str(point[0])
    point_y = str(point[1])
    point_str += point_x + ", " + point_y
    point_str_list.append(point_str)

point_str_list_diag = []
for point in final_coord_list_1d_diag:
    point_str = ""
    point_x = str(point[0])
    point_y = str(point[1])
    point_str += point_x + ", " + point_y
    point_str_list_diag.append(point_str)
# print(point_str_list)

# print(len(point_str_list))
# print("---")
# print(len(point_str_list_diag))

#join both list of strings
for item in point_str_list_diag:
    point_str_list.append(item)

# print("\n")
# print(len(point_str_list))

counter = Counter(point_str_list)

# print("\n")
# print(counter)

counter_dict = dict(counter)

count = 0
for key in counter_dict:
    if counter_dict[key] >= 2:
        count += 1

print(count)
