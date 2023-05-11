'''sorting algorithm using permutations'''
from itertools import permutations
def check_sort(array):
    '''checks to see if list is sorted'''
    i = 0
    while i < (len(array) - 1):
        if array[i] > array[i+1]:
            return False
        i = i + 1
    return True
USER_IN = []
print('hit Enter after each integer, hit Enter twice to sort')
while True:
    n = input()
    if n == '':
        break
    USER_IN.append(int(n))
perm = permutations(USER_IN)
for j in perm:
    if check_sort(j) is True:
        print(j)
        break
