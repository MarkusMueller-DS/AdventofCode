file = "data.txt"
prev = 0 
counter = 0

with open(file, "r") as f:
    for line in f:
        item = int(line)
        if (item > prev):
            counter += 1
        prev = item

print(counter-1)
