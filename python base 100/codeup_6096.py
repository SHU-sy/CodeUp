d = [[0 for i in range(20)] for j in range(20)]

for x in range(1, 20):
    row = list(map(int, input().split()))
    for y in range(1, 20):
        d[x][y] = row[y-1]

n = int(input())

for i in range(n):
    x, y = list(map(int, input().split()))
    d[x] = [1-val for val in d[x]]
    for j in range(1, 20):
        d[j][y] = 1 - d[j][y]

for x in range(1, 20):
    for y in range(1, 20):
        print(d[x][y], end=' ')
    print()