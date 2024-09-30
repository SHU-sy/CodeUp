h, w = map(int, input().split()) # 세로, 가로
n = int(input()) # 놓을 수 있는 막대 개수

board = [[0 for i in range(w+1)] for j in range(h+1)]

for i in range(n):
    l, d, x, y = map(int, input().split())  # 막대 길이, 방향(가로0 세로1), 좌표(x,y)

    if d == 0:
        for k in range(l):
            board[x][y+k] = 1

    else : # 막대가 세로일 때
        for k in range(l):
            board[x+k][y] = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        print(board[i][j], end=' ')
    print()