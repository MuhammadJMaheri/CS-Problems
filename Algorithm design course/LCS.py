'''LCS of three lists problem'''

Sara_Length, Sina_Length, Saba_Length = map(int, input().split())
Sara_Scores = list(map(str, input().split()))
Sina_Scores = list(map(str, input().split()))
Saba_Scores = list(map(str, input().split()))

SARA_STRING = ''.join(Sara_Scores)

SINA_STRING = ''.join(Sina_Scores)

SABA_STRING = ''.join(Saba_Scores)

L = [[[0 for i in range(Saba_Length+1)] for j in range(Sina_Length+1)]
        for k in range(Sara_Length+1)]

for i in range(Sara_Length+1):
    for j in range(Sina_Length+1):
        for k in range(Saba_Length+1):
            if (i == 0 or j == 0 or k == 0):
                L[i][j][k] = 0

            elif (SARA_STRING[i-1] == SINA_STRING[j-1] and
                    SARA_STRING[i-1] == SABA_STRING[k-1]):
                L[i][j][k] = L[i-1][j-1][k-1] + 1

            else:
                L[i][j][k] = max(L[i - 1][j][k], L[i][j - 1][k], L[i][j][k - 1])

print(L[Sara_Length][Sina_Length][Saba_Length])
