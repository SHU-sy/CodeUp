box = [[0 for i in range(10+1)] for j in range(10+1)]

for i in range(1, 10+1):
    row = list(map(int, input().split()))
    for j in range(1, 10+1):
        box[i][j] = row[j-1]

# 개미 시작(2, 2)
x, y = 2, 2
box[x][y] = 9

while True:
    if box[x][y] == 2:
        box[x][y] = 9
        break

    if box[x][y+1] != 1:
        y += 1
    elif box[x+1][y] != 1:
        x += 1
    else:
        break

    if box[x][y] == 0:
        box[x][y] = 9


for i in range(1, 10+1):
    for j in range(1, 10+1):
        print(box[i][j], end=' ')
    print()