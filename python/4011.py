import sys
n = sys.stdin.readline().split()
odd = []
even = []
for i in range(len(n)):
    if int(n[i])%2==0:
        even.append(n[i])
    else:
        odd.append(n[i])
if odd and even:
    print(int(max(odd))+ int(max(even)))
elif odd:
    print(int(max(odd)))
elif even:
    print(int(max(even)))