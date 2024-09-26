a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

def number(num):
    if(num%2==0):
        print("even")
    else:
        print("odd")

number(a)
number(b)
number(c)