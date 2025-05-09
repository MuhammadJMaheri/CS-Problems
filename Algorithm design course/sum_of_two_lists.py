
n = int(input())
heights_1 = [int(i) for i in (input()).split()]
heights_2 = [int(i) for i in (input()).split()]

def maximize_team(h1, h2, num):
    if num == 0:
        return 0
    if num == 1:
        return max(h1[0], h2[0])
    if num == 2:
        return max(h1[0] + h2[1] ,h2[0] + h1[1])

    dp = [0]*num

    team = 0

    dp[0] = max(h1[0], h2[0])
    if h1[0] + h2[1] > h2[0] + h1[1]:
        dp[1] = h1[0] + h2[1]
        team = 2
    else:
        dp[1] = h2[0] + h1[1]
        team =1
    for i in range(2, num):

        if team == 1:
            m = max(h2[i]+dp[i-1], h2[i]+dp[i-2], h1[i]+dp[i-2])
            if m in (h2[i]+dp[i-1] ,h2[i]+dp[i-2]):
                team =2
            dp[i] = m
            continue
        if team == 2:
            m = max(h1[i]+dp[i-1], h1[i]+dp[i-2], h2[i]+dp[i-2])
            if m in (h1[i]+dp[i-1], h1[i]+dp[i-2]):
                team =1
            dp[i] = m
            continue

    return max(dp)

print(maximize_team(heights_1, heights_2, n))
