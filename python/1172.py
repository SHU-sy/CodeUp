import sys
n = list(map(int, sys.stdin.readline().split()))
print(' '.join(map(str, sorted(n))))