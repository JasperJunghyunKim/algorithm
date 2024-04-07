import sys
N = sys.stdin.readline().strip()
val = int(N)
N = list(N)
digits = len(N)

total = 0
for i in range(1, digits):
    total += 9 * (10 ** (i-1)) * i
total += (val - (10 ** (digits - 1)) + 1) * digits
print(total)