from collections import Counter

file = "data5.txt"
test_file = "data5_test.txt"


num_list = []
with open(file, "r") as f:
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

# find lines which are horizontal or vertical
vert_hori_lines = []
for line in num_list_final:
    if (line[0] == line[2] or line[1] == line[3]):
        vert_hori_lines.append(line)

num_list_final = []
for line in vert_hori_lines:
    nums_map = map(int, line)
    num_list_final.append(list(nums_map))


# print(num_list_final)

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


final_coord_list = []
for line in num_list_final:
    r = generateCorrds(line)
    # print(r)
    # print("---")
    final_coord_list.append(r)

final_coord_list_1d = []
for line in final_coord_list:
    for item in line:
        final_coord_list_1d.append(item)


# trasfrom points to strings to Count them
point_str_list = []
for point in final_coord_list_1d:
    point_str = ""
    point_x = str(point[0])
    point_y = str(point[1])
    point_str += point_x + ", " + point_y
    point_str_list.append(point_str)

# print(point_str_list)


counter = Counter(point_str_list)

counter_dict = dict(counter)

count = 0
for key in counter_dict:
    if counter_dict[key] >= 2:
        count += 1

print(count)
