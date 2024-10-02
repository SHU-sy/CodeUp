import sys
a, b, c = map(int, sys.stdin.readline().split())
ave = (a+b+c)/3
print(f"{ave:.2f}")