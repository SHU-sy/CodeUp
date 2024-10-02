import sys
s = sys.stdin.readline().strip()
a = []
for i in range(len(s)):
    if 65 <= ord(s[i]) <= 90:
        a.append(s[i].lower())
    else:
        a.append(s[i].upper())
print("".join(a))