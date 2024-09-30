import sys

a = list(map(int, (sys.stdin.readline().strip() for i in range(7))))
print(max(a))
a.remove(max(a))
print(max(a))