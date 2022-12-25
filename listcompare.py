from collections import Counter

one = [33, 22, 11, 44, 55]
two = [22, 11, 44, 55, 33,33]

print("is two list are b equal",Counter(one) ,Counter(two) , Counter(one) == Counter(two))

print("is two list are b equal", (one) == (two))

print("****************************************************************")

currentEmployee = {1: 'Scott', 2: "Eric", 3:"Kelly"}
formerEmployee  = {2: 'Eric', 4: "Emma"}

allEmployee = {**currentEmployee, **formerEmployee}
print(allEmployee)




allEmployee = {**formerEmployee,**currentEmployee}
print(allEmployee)



print("****************************************************************")

ItemId = [54, 65, 76]
names = ["Hard Disk", "Laptop", "RAM","Rahul"]

itemDictionary = dict(zip(ItemId, names))

print(itemDictionary)


print("***************")


import numpy

arraySample = numpy.array([[1, 2], [3, 4], [4, 6], [7, 8]])

for value in arraySample[:, col_num]:
    print(value)
