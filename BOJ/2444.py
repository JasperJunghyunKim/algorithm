import sys
n = int(sys.stdin.readline().strip())
for i in range(1, 2*n-1):
    print(' ' * (abs(n - i)), '*' * (2 * (n - abs(n - i))-1))
print(' ' * abs(n-1), '*', end='')