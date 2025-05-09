'''number of equavilent lists to produce the same binary tree'''

LENGTH = int(input())
nums = [int(i) for i in (input()).split()]

def dfs(nums_in):

    if len(nums_in) < 2:
        return 1

    left = [x for x in nums_in if x < nums_in[0]]
    right = [x for x in nums_in if x > nums_in[0]]

    m = len(left)
    q = len(right)

    a = dfs(left)
    b = dfs(right)

    return (((c[m + q][m] * a) % MOD) * b) % MOD

MOD = 10**9 + 7
c = [[0] * LENGTH for _ in range(LENGTH)]
c[0][0] = 1

for i in range(1, LENGTH):

    c[i][0] = 1
    for j in range(1, i + 1):
        c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD

output = (dfs(nums) - 1 + MOD) % MOD
print(output)
