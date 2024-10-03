import sys
def kaprekar_steps(n):
    count = 0

    if n < 1000 or n > 9999:
        return -1

    if len(set(str(n))) == 1:
        return -1

    while n != 6174:
        str_n = str(n).zfill(4)
        ascending = int("".join(sorted(str_n)))
        descending = int("".join(sorted(str_n, reverse=True)))

        n = descending - ascending
        count += 1

    return count

n = int(sys.stdin.readline().strip())
result = kaprekar_steps(n)
print(result)