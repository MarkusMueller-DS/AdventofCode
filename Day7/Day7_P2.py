import numpy as np
import pandas as pd

file = "data7.txt"
test_file = "test_data7.txt"

with open(file, "r") as f:
    data = f.readline().split(",")

# map data to ints
data = list(map(int, data))
# transform to numpy array for ease of use
np_data = np.array(data)

# print(np_data.min())
# print(np_data.max())

# possible position to meet
possible_positiones = range(np_data.min(), np_data.max()+1)

# function for sum of arithmetic series
def sumOfAP(a, d, n):
    return ((n / 2) * (2 * a + (n - 1) * d))

# calculate fuel consumption for position
fuel_consumption = []
for starting_point in np_data:
    fuel_consumption_list = []
    counter = 0
    for point in possible_positiones:
        distance = abs(starting_point - point)
        arith_sum = sumOfAP(1, 1, distance)
        fuel_consumption_list.append(arith_sum)
    fuel_consumption.append(fuel_consumption_list)


# for x in fuel_consumption:
    # print(x)
    # print("---")

# create pandas DataFrame from list
df = pd.DataFrame.from_records(fuel_consumption)
# print(df)

# calculate mean for every col
values = df.sum(axis=0).values
values = np.array(values)
print(np.min(values))


