import sys
password = sys.stdin.readline().strip()
Encryption_1 = []
Encryption_2 = []

for i in range(len(password)):
    Encryption_1.append(chr(ord(password[i]) + 2))
    Encryption_2.append(chr((ord(password[i]) * 7)%80+48))
print("".join(Encryption_1))
print("".join(Encryption_2))