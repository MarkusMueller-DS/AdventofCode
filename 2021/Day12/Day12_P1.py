# https://www.redblobgames.com/pathfinding/a-star/introduction.html
# https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python
# https://www.reddit.com/r/adventofcode/comments/rf1oi7/2021_day_12_part_1_ive_implemented_bfs_but_stuck/
# DFS
file = "data12.txt"
test_file = "test_data12.txt"

data = []
with open(test_file, "r") as f:
    for line in f:
        data.append(line.strip())

# transfrom input to a list fo tuples
tuple_list = [] 
for link in data:
    tuple_ = tuple(link.split("-"))
    tuple_list.append(tuple_)

print(tuple_list)


# print(data)

start_list = []
def findStart():
    for x in data:
        if 'start' in x:
            start_list.append(x)

end_list = []
def findEnd():
    for x in data:
        if 'end' in x:
            end_list.append(x)

# stopping condition: when queue is empty

# return number of times wo got to the end node


# if nex node is lowercas and already in path:
#     just dont do anything


# findStart()
# findEnd()
# print(start_list)
# print(end_list)


# def path():
#     for x in data:




