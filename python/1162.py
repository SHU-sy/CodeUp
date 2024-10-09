import sys
y, m, d = map(int, sys.stdin.readline().split())
if str(y - m + d)[-1:] == '0':
    print("대박")
else:
    print("그럭저럭")