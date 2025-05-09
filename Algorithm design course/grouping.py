"""greedy grouping program"""

classroom = []
N = int(input())

for i in range(1, N + 1):
    classroom.append(i)

group_a = []
group_b = []

"""This optional line is only for making the output identical to the example output
 and is unnecessary for question's objectives."""
group_a.append(classroom.pop())

while len(classroom) > 0:
    if sum(group_a) < sum(group_b):
        group_a.append(classroom.pop())
    else:
        group_b.append(classroom.pop())

print(len(group_a))
print(*group_a)
print(len(group_b))
print(*group_b)
