# import copy

# data1 = [1, 2, 3]
# data2 = data1
# data3 = copy.copy(data1)
# data2.append(4)
# print(id(data1), data1)
# print(id(data2), data2)
# print(id(data3), data3)


# import copy

# data1 = [[1], [2]]
# data2 = data1
# data3 = copy.copy(data1)
# data2[1].append(3)
# print(id(data1), data1)
# print(id(data2), data2)
# print(id(data3), data3)


# import copy

# data1 = [1, 2, 3]
# data2 = data1
# data3 = copy.deepcopy(data1)
# data2.append(4)
# print(id(data1), data1)  # -> 4331999296 [1, 2, 3, 4]
# print(id(data2), data2)  # -> 4331999296 [1, 2, 3, 4]
# print(id(data3), data3)  # -> 4331997504 [1, 2, 3]


# import copy

# data1 = [[1], [2]]
# data2 = data1
# data3 = copy.deepcopy(data1)
# data2[1].append(3)
# print(id(data1), data1)  # -> 4306634048 [[1], [2, 3]]
# print(id(data2), data2)  # -> 4306634048 [[1], [2, 3]]
# print(id(data3), data3)  # -> 4305685184 [[1], [2]]


data = [[1, 2], [3, 4]]

new_data = data[:]

data[0][0] = 10
new_data[1][1] = 40
 
print(data)
print(new_data)