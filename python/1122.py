import sys
second = int(sys.stdin.readline().strip())
minute = second//60
print(minute, second-(minute*60))
