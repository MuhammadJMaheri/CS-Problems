"""worker problem"""
from math import ceil

K = int(input())
T = int(input())
W = list(map(int, input().split()))

worker_units = [0 for i in range(0, K)]
portion = ceil(sum(W)/K)
ind = 0

for i in range(0, len(worker_units)):
    if ind == len(W):
        break
    while abs(worker_units[i] - portion) >= abs(worker_units[i] + W[ind] - portion):
        worker_units[i] += W[ind]
        ind += 1
        if ind == len(W):
            break

print(max(worker_units) * T)
