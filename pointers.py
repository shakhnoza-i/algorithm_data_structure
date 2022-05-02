num1 = 11
num2 = num1

print("num1 = ", num1)
print("num2 = ", num2)

print("num1 points to: ", id(num1)) # they are pointing to the same place in memory
print("num2 points to: ", id(num2))
num2 = 12 # now pointing to the another place in memory - cause int() immutable
# and num1 and num2 have different values, also there are point to the different
# place in memory




dict1 = {'value': 11}
dict2 = dict1 #  pointing to the same place in memory
dict2['value'] = 12 # after the value is updated, both dict1 and dict2 have value 12
# and point to the same place in memory - cause dictionary is a mutable data type
print("dict1 = ", dict1) # dict1 = {'value': 12}
print("dict2 = ", dict2) # dict2 = {'value': 12}

print("dict1 points to: ", id(dict1)) # they are pointing to the same place in memory
print("dict2 points to: ", id(dict2))

# if you don't have any variable pointing to the  existing dictionary - in this 
# situation Python will remove this through a process called garbage collection.
