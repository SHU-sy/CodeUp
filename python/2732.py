import sys
input = sys.stdin.readline
n = int(input().strip())
c = [0] * 7

day_dic = [
    '월요일에 가능',
    '화요일에 가능',
    '수요일에 가능',
    '목요일에 가능',
    '금요일에 가능',
    '토요일에 가능',
    '일요일에 가능'
]

for _ in range(n):
    a = list(map(int, input().strip()))

    for i in range(7):
        c[i] += a[i]

all_unavailable = True
for i in range(7):
    if c[i] == n:
        print(day_dic[i])
        all_unavailable = False

if all_unavailable:
    print("다음에 만나요~")