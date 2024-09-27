n = int(input())
d = [[0 for i in range(20)] for j in range(20)]

for i in range(n):
    x, y = list(map(int, input().split()))
    d[x][y] = 1

for x in range(1, 19+1):
    for y in range(1, 19+1):
        print(d[x][y], end=' ')
    print()
