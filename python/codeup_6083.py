r, g, b = input().split()
num = 0
for i in range(int(r)):
    for j in range(int(g)):
        for k in range(int(b)):
            print(i, j, k)
            num += 1
print(num)