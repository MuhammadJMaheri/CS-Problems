'''max sum of array with changing signs of adjacent arrays'''

n = int(input())
nums = [int(i) for i in (input()).split()]

negative_count = 0
max_sum = 0
smallest = 0
SUM = 0

for i in range(n):

    if nums[i] < 0:
        negative_count += 1

    SUM += abs(nums[i]) 
    smallest = min(smallest, abs(nums[i]))

max_sum = SUM

if negative_count & 1:
    max_sum -= 2 * smallest

print(max_sum)
