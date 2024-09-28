num = list(map(int, input().split()))
s = 0
c = 1
for i in range(7):
    if num[i]%2!=0 :
        s += num[i]
    else:
        c +=1
        if c == 7:
            s = -1
            break
        continue
print(s)