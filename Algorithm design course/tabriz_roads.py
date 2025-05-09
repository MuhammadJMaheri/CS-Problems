'''tabriz roads problem'''

no_villages = int(input())
pair_sp = [list(map(int, input().split())) for _ in range(no_villages)]
no_newroads = int(input())
new_roads = [tuple(map(int, input().split())) for _ in range(no_newroads)]

SUM = 0
output = []
for i in range(no_villages):
    for j in range(no_villages):
        if i > j:
            SUM += pair_sp[i][j]
for query in new_roads:
    a, b, c = query
    a -= 1
    b -= 1
    if c < pair_sp[a][b]:
        for i in range(no_villages):
            for j in range(no_villages):
                new_distance = pair_sp[i][a] + c + pair_sp[b][j]
                if new_distance < pair_sp[i][j]:
                    SUM -= (pair_sp[i][j] - new_distance)
                    pair_sp[i][j] = new_distance
                    pair_sp[j][i] = new_distance
    output.append(SUM)

print(" ".join(map(str, output)))
