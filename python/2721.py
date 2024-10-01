import sys
s1, s2, s3 = [sys.stdin.readline().strip() for _ in range(3)]
if s1[-1] == s2[0] and s2[-1] == s3[0] and s3[-1] == s1[0]:
    print("good")
else:
    print("bad")