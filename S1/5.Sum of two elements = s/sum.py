'''Finds out if there are two elements in a list that their sum equals a given input.'''
from math import floor
def recursive_func(from_index, to_index, element):
    '''recursively devides index space'''
    global SUM, LIST
    if from_index == to_index and SUM - element == LIST[from_index]:
        return 1
    if from_index == to_index:
        return 0
    middle_index = floor((from_index + to_index)/2)
    middle_element = LIST[middle_index]
    if SUM - element == middle_element:
        return 1
    if SUM - element < middle_element:
        return recursive_func(from_index, middle_index, element)
    if SUM - element > middle_element:
        return recursive_func(middle_index + 1, to_index, element)
SUM = float(input("Enter S: "))
LIST = []
MAX_INDEX = -1
print("Enter sequence of numbers one by one, hit enter twice to end: ")
while 1:
    USER_IN = input()
    if USER_IN == "":
        break
    LIST.append(float(USER_IN))
    MAX_INDEX += 1
LIST.sort()
OUTPUT = 0
for num in LIST:
    if recursive_func(0, MAX_INDEX, num) == 1:
        OUTPUT = 1
        break
if OUTPUT == 1:
    print("Output = 1")
else:
    print("Output = 0")
