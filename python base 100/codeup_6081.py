a = int(input(), 16)
for i in range(1, 16):
    print(f"{hex(a)[2:].upper()}", "*", f"{hex(i)[2:].upper()}", "=", f"{hex(a*i)[2:].upper()}", sep='')