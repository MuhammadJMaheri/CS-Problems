'''insertion sort algorithm'''
USER_IN = []
print('hit Enter after each integer, hit Enter twice to sort')
while True:
    n = input()
    if n == '':
        break
    USER_IN.append(int(n))

SORTED_OUT = [USER_IN.pop()]
SORTED_SIZE = 1
for i in USER_IN:
    for j in range(0,SORTED_SIZE):
        if i <= SORTED_OUT[j]:
            SORTED_OUT.insert(j,i)
            SORTED_SIZE = SORTED_SIZE +1
            break
        if j == SORTED_SIZE - 1:
            SORTED_OUT.append(i)
            SORTED_SIZE = SORTED_SIZE +1
            break
print(SORTED_OUT)
