count = int(input())
k = list(map(int, input().split()))
s = k[0]

for i in k:
    if i < s:
        s = i

print(s)