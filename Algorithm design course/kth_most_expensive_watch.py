'''kth most expensive element problem'''

NUMBER_OF_WATCHES = int(input())
watch_prices = [int(i) for i in (input()).split()]
k = int(input())


def quickselect(numbers, l, h):
    '''does selection'''

    p = l + 1
    r = h

    while True:

        while p <= r and numbers[p] <= numbers[l]:
            p += 1

        while r >= p and numbers[r] >= numbers[l]:
            r -= 1

        if p > r:
            break

        numbers[p], numbers[r] = numbers[r], numbers[p]

    numbers[l], numbers[r] = numbers[r], numbers[l]
    return r

k = NUMBER_OF_WATCHES - k
HIGH = NUMBER_OF_WATCHES - 1
LOW = 0

while LOW < HIGH:
    i = quickselect(watch_prices, LOW, HIGH)

    if i < k:
        LOW = i + 1

    elif i > k:
        HIGH = i - 1

    else:
        break

print(watch_prices[k])
