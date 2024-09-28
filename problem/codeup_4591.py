import sys

a = list(map(int, (sys.stdin.readline().strip() for i in range(9))))
print(max(a))
print(a.index(max(a))+1)