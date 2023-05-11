'''some sorting algorithm'''
from math import floor
user_array = []
print('enter integers, press Enter twice to sort:')
while 1:
    user_in = input()
    if user_in == '':
        break
    user_array.append(int(user_in))

def left_right(array, from_i, to_i):
    '''smaller than middle to the left, greater to the right'''
    middle = array[floor((to_i + from_i)/2)]
    smaller = []
    equal = []
    greater = []
    for integer in array:
        if integer < middle:
            smaller.append(integer)
        if integer > middle:
            greater.append(integer)
        if integer == middle:
            equal.append(integer)
    new_array = smaller + equal + greater
    for index , value in enumerate(new_array):
        array[index] = value

def sort(array, from_i, to_i):
    '''sorts recursively'''
    if from_i >= to_i:
        return
    middle_i = floor((to_i + from_i)/2)
    sort(array, from_i, middle_i)
    sort(array, middle_i + 1, to_i)
    left_right(array, from_i, to_i)

sort(user_array,0,len(user_array)-1)
print(user_array)
